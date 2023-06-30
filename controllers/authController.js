const User = require('../models/User');
const Token = require('../models/Token');
const sendWelcomeEmail = require("../utils/sendWelcomeEmail");
const { StatusCodes } = require('http-status-codes');
const CustomError = require('../errors');
const jwt_decode = require('jwt-decode');
const {createNotification} = require('./NotificationCrontroller');
const {
  attachCookiesToResponse,
  createTokenUser,
  sendVerificationEmail,
  sendResetPasswordEmail,
  createHash,
} = require('../utils');

const crypto = require('crypto');

const register = async (req, res) => {
  const { email, name, password } = req.body;


  const emailAlreadyExists = await User.findOne({ email });
  if (emailAlreadyExists) {
    throw new CustomError.BadRequestError('Email already exists');
  }

  // first registered user is an admin
  const isFirstAccount = (await User.countDocuments({})) === 0;
  const role = isFirstAccount ? 'admin' : 'user';

  const verificationToken = crypto.randomBytes(40).toString('hex');

  const user = await User.create({
    name,
    email,
    password,
    role,
    verificationToken,
  });
  if (user){
    console.log(`User created : ${user.email}`);
  }

  const tokenUser = createTokenUser(user);

  // create refresh token
  let refreshToken = '';
  refreshToken = crypto.randomBytes(40).toString('hex');

  const userAgent = req.headers['user-agent'];
  const ip = req.ip;
  const userToken = { refreshToken, ip, userAgent, user: user._id };

  await Token.create(userToken);
  createNotification(user, `Welcome to Packman ${user.name}! You will be receiving updates on your wishlist items here!`);
  attachCookiesToResponse({ res, user: tokenUser, refreshToken });
  await sendWelcomeEmail({
    name: user.name, 
    email: user.email
  });
  res.status(StatusCodes.CREATED).json({ user: tokenUser, msg: 'Success! You\'re now registered and logged in. Please confirm Email. '});

};

const verifyEmail = async (req, res) => {
  const { verificationToken, email } = req.body;
  const user = await User.findOne({ email });

  if (!user) {
    throw new CustomError.UnauthenticatedError('Verification Failed');
  }

  if (user.verificationToken !== verificationToken) {
    throw new CustomError.UnauthenticatedError('Verification Failed');
  }

  (user.isVerified = true), (user.verified = Date.now());
  user.verificationToken = '';

  await user.save();

  res.status(StatusCodes.OK).json({ msg: 'Email Verified' });
};

const login = async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    throw new CustomError.BadRequestError('Please provide email and password');
  }
  const user = await User.findOne({ email });

  if (!user) {
    throw new CustomError.UnauthenticatedError('Invalid Credentials');
  }
  const isPasswordCorrect = await user.comparePassword(password);

  if (!isPasswordCorrect) {
    throw new CustomError.UnauthenticatedError('Invalid Credentials');
  }
  // if (!user.isVerified) {
  //   throw new CustomError.UnauthenticatedError('Please verify your email');
  // }
  const tokenUser = createTokenUser(user);

  // create refresh token
  let refreshToken = '';
  // check for existing token
  const existingToken = await Token.findOne({ user: user._id });

  if (existingToken) {
    const { isValid } = existingToken;
    if (!isValid) {
      throw new CustomError.UnauthenticatedError('Invalid Credentials');
    }
    refreshToken = existingToken.refreshToken;
    attachCookiesToResponse({ res, user: tokenUser, refreshToken });
    res.status(StatusCodes.OK).json({ user: tokenUser });
    return;
  }

  refreshToken = crypto.randomBytes(40).toString('hex');
  const userAgent = req.headers['user-agent'];
  const ip = req.ip;
  const userToken = { refreshToken, ip, userAgent, user: user._id };

  await Token.create(userToken);

  attachCookiesToResponse({ res, user: tokenUser, refreshToken });

  res.status(StatusCodes.OK).json({ user: tokenUser });
};

const gLogin = async (req, res) => {
  const { authCode } = req.body;
  googleUser = jwt_decode(authCode);
  if (!authCode) {
     throw new CustomError.BadRequestError('Google account Invalid');
   }
  try {
    // Check if user is already registered
    let user = await User.findOne({ googleId: googleUser.sub });
    // If user is not registered, create new user
    let registeringNewUser;
    if (!user) {
        registeringNewUser = true;
        user = new User({
            googleId: googleUser.sub,
            email: googleUser.email,
            name: googleUser.name,
            isVerified: true
        });
        console.log(User);
        await user.save();
    }
    const tokenUser = createTokenUser(user);
    // create refresh token
    let refreshToken = '';
    // check for existing token
    const existingToken = await Token.findOne({ user: user._id });
  
    if (existingToken) {
      const { isValid } = existingToken;
      if (!isValid) {
        throw new CustomError.UnauthenticatedError('Invalid Credentials');
      }
      refreshToken = existingToken.refreshToken;
      attachCookiesToResponse({ res, user: tokenUser, refreshToken });
      res.status(StatusCodes.OK).json({ user: tokenUser });
      return;
    }
  
    refreshToken = crypto.randomBytes(40).toString('hex');
    const userAgent = req.headers['user-agent'];
    const ip = req.ip;
    const userToken = { refreshToken, ip, userAgent, user: user._id };
    await Token.create(userToken);
    attachCookiesToResponse({ res, user: tokenUser, refreshToken });
    
    if(registeringNewUser){
      createNotification(user, `Welcome to Packman ${user.name}! You will be receiving updates on your wishlist items here!`);
      await sendWelcomeEmail({
        name: user.name, 
        email: user.email
      });
    }

    res.status(StatusCodes.OK).json({ user: userToken });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error authenticating with Google.');
  }
};

const logout = async (req, res) => {
  await Token.findOneAndDelete({ user: req.user.userId });

  res.cookie('accessToken', 'logout', {
    httpOnly: true,
    expires: new Date(Date.now()),
  });
  res.cookie('refreshToken', 'logout', {
    httpOnly: true,
    expires: new Date(Date.now()),
  });
  res.status(StatusCodes.OK).json({ msg: 'user logged out!' });
};

const forgotPassword = async (req, res) => {
  const { email } = req.body;
  if (!email) {
    throw new CustomError.BadRequestError('Please provide valid email');
  }

  const user = await User.findOne({ email });

  if (user) {
    const passwordToken = crypto.randomBytes(70).toString('hex');
    // send email
    const origin = 'http://localhost:3000';
    await sendResetPasswordEmail({
      name: user.name,
      email: user.email,
      token: passwordToken,
      origin,
    });

    const tenMinutes = 1000 * 60 * 10;
    const passwordTokenExpirationDate = new Date(Date.now() + tenMinutes);

    user.passwordToken = createHash(passwordToken);
    user.passwordTokenExpirationDate = passwordTokenExpirationDate;
    await user.save();
  }

  res
    .status(StatusCodes.OK)
    .json({ msg: 'Please check your email for reset password link' });
};
const resetPassword = async (req, res) => {
  const { token, email, password } = req.body;
  if (!token || !email || !password) {
    throw new CustomError.BadRequestError('Please provide all values');
  }
  const user = await User.findOne({ email });

  if (user) {
    const currentDate = new Date();

    if (
      user.passwordToken === createHash(token) &&
      user.passwordTokenExpirationDate > currentDate
    ) {
      user.password = password;
      user.passwordToken = null;
      user.passwordTokenExpirationDate = null;
      await user.save();
    }
  }

  res.send('reset password');
};

module.exports = {
  register,
  login,
  gLogin,
  logout,
  verifyEmail,
  forgotPassword,
  resetPassword,
};
