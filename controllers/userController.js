const User = require('../models/User');
const { StatusCodes } = require('http-status-codes');
const CustomError = require('../errors');
const {
  createTokenUser,
  attachCookiesToResponse,
  checkPermissions,
} = require('../utils');

const getAllUsers = async (req, res) => {
  console.log(req.user);
  const users = await User.find({ role: 'user' }).select('-password');
  console.log(users);
  res.status(StatusCodes.OK).json({ users });
};

const addUser = async(req, res)=>{
    console.log("adduser called.")
    const newUser = new User({
        name: 'paccers',
        email: 'pacyadmin@example.com',
        password: 'password123',
      });
      try {
        const savedUser = await newUser.save();
        console.log(`User with ID ${savedUser._id} has been inserted into the database.`);
        res.status(StatusCodes.OK).json({ newUser });
      } catch (err) {
        console.error(err);
      }
};


//find one user by their email.
const getSingleUserbyemail = async (req, res) => {
    const user = await User.findOne({ email: req.params.email }).select('-password');
    if (!user) {
      throw new CustomError.NotFoundError(`No user with email : ${req.params.email}`);
    }
    //checkPermissions(req.user, user._id);
    res.status(StatusCodes.OK).json({ user });
  };

const getSingleUserbyId = async (req, res) => {
  const user = await User.findOne({ _id: req.params.id }).select('-password');
  if (!user) {
    throw new CustomError.NotFoundError(`No user with id : ${req.params.id}`);
  }
  checkPermissions(req.user, user._id);
  res.status(StatusCodes.OK).json({ user });
};

const showCurrentUser = async (req, res) => {
  res.status(StatusCodes.OK).json({ user: req.user });
};


// update user with user.save()
const updateUser = async (req, res) => {
  const { email, name } = req.body;
  if (!email || !name) {
    throw new CustomError.BadRequestError('Please provide all values');
  }
  const user = await User.findOne({ _id: req.user.userId });

  user.email = email;
  user.name = name;

  await user.save();

  const tokenUser = createTokenUser(user);
  attachCookiesToResponse({ res, user: tokenUser });
  res.status(StatusCodes.OK).json({ user: tokenUser });
};


const updateUserPassword = async (req, res) => {
  const { oldPassword, newPassword } = req.body;
  if (!oldPassword || !newPassword) {
    throw new CustomError.BadRequestError('Please provide both values');
  }
  const user = await User.findOne({ _id: req.user.userId });

  const isPasswordCorrect = await user.comparePassword(oldPassword);
  if (!isPasswordCorrect) {
    throw new CustomError.UnauthenticatedError('Invalid Credentials');
  }
  user.password = newPassword;

  await user.save();
  res.status(StatusCodes.OK).json({ msg: 'Success! Password Updated.' });
};

module.exports = {
  getAllUsers,
  getSingleUserbyId,
  getSingleUserbyemail,
  showCurrentUser,
  updateUser,
  updateUserPassword,
  addUser,
};

