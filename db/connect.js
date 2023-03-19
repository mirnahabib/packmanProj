const mongoose = require('mongoose');

//mongodb://localhost:27017/packmandb
//connection should be established using process.env variable MONGO_URI
const connectDB = (url) => {
  
  return mongoose.connect(url, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useFindAndModify: false,
    useUnifiedTopology: true,
  }).then( result => console.log("database connected"))
  .catch(err => console.log(err));
};

module.exports = connectDB;
