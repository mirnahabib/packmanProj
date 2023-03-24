const express = require('express')
const {items} = require('./data')
require('express-async-errors');

const app = express();
const connectDB = require('./db/connect');

const notFoundMiddleware = require('./middleware/not-found');
const errorMiddleware = require('./middleware/error-handler');


//this line allows all files in public folder to be accesible to users
app.use(express.static('public'));


app.get('/', (req, res) => {
  console.log('client request received')
  res.status(200).send('Home Page')
})

app.get('/api/query', (req, res) => {
  console.log(req.query)
  const { search } = req.query
  let sortedItems = [...items]

  if (search) {
    sortedItems = sortedItems.filter((item) => {
      return item.name.includes(search)
    })
    if (sortedItems.length < 1) {
      return res.status(200).send('no products matched your search');
    }
  }
  res.status(200).json(sortedItems)
})

app.get('/about', (req, res) => {
  res.status(200).send('About Page')
})

app.all('*', (req, res) => {
  res.status(404).send('<h1>404 Not Found!</h1>')
})


const start = async () => {
  try {
    app.listen(3000, () => console.log('Server is listening port 3000...'));
    // connectDB
    await connectDB("mongodb://127.0.0.1:27017/packmandb");
  } catch (error) {
    console.log(error);
  }
};

start();