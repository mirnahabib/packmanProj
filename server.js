const express = require('express')
require('dotenv').config();//Set up env variables
require('express-async-errors');

//Security packages
const helmet = require('helmet'); //For Cross-Site Scripting (XSS), clickjacking
const cors = require('cors');
const xss = require('xss-clean');
const rateLimiter = require('express-rate-limit'); //Prevent abuse and overloading of the server
const mongoSanitize = require('express-mongo-sanitize');//Prevent NoSQL Injection attacks

const cookieParser = require('cookie-parser');//Automatically parsing cookies


//Routes
const authRouter = require('./routes/authRoutes');
const crawlerRouter = require('./routes/crawlerRoutes')

//Database
const connectDB = require('./db/connect');

//Middlewares
const notFoundMiddleware = require('./middleware/not-found');
const errorHandlerMiddleware = require('./middleware/error-handler');
const authenticateUser = require('./middleware/authentication');
const { process_params } = require('express/lib/router');


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


//search example on url 'http://localhost:5000/api/search/general/playstation'
app.use('/api/search', crawlerRouter);
//login and register
app.use('/api/auth', authRouter);


app.use('/', (req, res) =>{
  res.status(200).send('Home Page')
})

app.use(notFoundMiddleware);
app.use(errorHandlerMiddleware);

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