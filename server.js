const express = require('express')
require('dotenv').config();//Set up env variables
require('express-async-errors');

//Api documentation
const swaggerUI = require('swagger-ui-express');
const YAML = require('yamljs');
const swaggerDocument = YAML.load('./swagger.yaml');


//Security packages
const helmet = require('helmet'); //Prevent Cross-Site Scripting (XSS), clickjacking
const cors = require('cors');
const xss = require('xss-clean');
const rateLimiter = require('express-rate-limit'); //Prevent abuse and overloading of the server
const mongoSanitize = require('express-mongo-sanitize');//Prevent NoSQL Injection attacks

const cookieParser = require('cookie-parser');//Automatically parsing cookies


//Routes
const authRouter = require('./routes/authRoutes');
const crawlerRouter = require('./routes/crawlerRoutes');
const userRouter = require('./routes/userRoutes');
const favouriteRouter = require('./routes/favRoutes');


//Database
const connectDB = require('./db/connect');

//Middlewares
const notFoundMiddleware = require('./middleware/not-found');
const errorHandlerMiddleware = require('./middleware/error-handler');
const authenticateUser = require('./middleware/authentication');
const { process_params } = require('express/lib/router');

//Automaters
const scheduleDailyPriceCheck = require('./automaters/dailyPriceCheck');

const app = express();

app.set('trust proxy', 1);
app.use(
  rateLimiter({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs (15mins)
  })
);

app.use(helmet());
app.use(cors());
app.use(xss());
app.use(mongoSanitize());

app.use(cookieParser(process.env.SECRET_KEY));

app.use(express.json());// Allows Json payload on requests.

//this line allows all files in public folder to be accesible to users
//app.use(express.static('public'));

app.get('/', (req, res) => {
  res.send('<h1>PACMAN PROJ API</h1><a href="/api-docs">Documentation</a>');
});
app.use('/api-docs', swaggerUI.serve, swaggerUI.setup(swaggerDocument));


//search default on url 'http://localhost:5000/api/search/general/playstation'
//added used products options 'http://localhost:5000/api/search/used/general/playstation'
app.use('/api/search', crawlerRouter);
//login and register 'http://localhost:5000/api/auth/login'
app.use('/api/auth', authRouter);
//Manage users data in db (requires admin role except for own profile)
app.use('/api/users', userRouter);
//Manage favourites (requires logged in user)
// '/' to retrieve user's favourites list, '/addOrRemove' to add or remmove one item to his favourites list.
app.use('/api/favourites', favouriteRouter);



app.use(notFoundMiddleware);
app.use(errorHandlerMiddleware);

scheduleDailyPriceCheck();

const start = async () => {
  try {
    app.listen(process.env.PORT, () => console.log(`Server is listening port ${process.env.PORT}...`)); //Port is 5000
    //connect db
    //comment next line in case you don't have database setup
    await connectDB(process.env.DATABASE_URI);
  } catch (error) {
    console.log(error);
  }
};

start();