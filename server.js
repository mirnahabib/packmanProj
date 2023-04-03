const express = require('express')
const crawlerRouter = require('./routes/crawlerRoutes')
require('express-async-errors');

const app = express();
const connectDB = require('./db/connect');

const notFoundMiddleware = require('./middleware/not-found');
const errorMiddleware = require('./middleware/error-handler');

app.use(express.json());

//this line allows all files in public folder to be accesible to users
app.use(express.static('public'));


//search example on url 'http://localhost:5000/api/search/general/playstation'
app.use('/api/search', crawlerRouter);

app.use('/', (req, res) =>{
  res.status(200).send('Home Page')
})

app.use(notFoundMiddleware);

const start = async () => {
  try {
    app.listen(5000, () => console.log('Server is listening port 5000...'));
    // connectDB
    //await connectDB("mongodb://127.0.0.1:27017/packmandb");
  } catch (error) {
    console.log(error);
  }
};

start();