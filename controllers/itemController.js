const Item = require('../models/Item');
const favourite = require('../models/Favourite');
const { StatusCodes } = require('http-status-codes');
const CustomError = require('../errors');
const {
  checkPermissions,
} = require('../utils');

const addITem = async (req) => {
  const { title, price, link, img, category } = req.body;
  if (!link) {
    throw new CustomError.BadRequestError('You can\'t add an item without link');
  }
  const item = await Item.findOne({ link });
  if (item){
    next();
  }
  const newItem = await Item.create({
    title,
    link,
    price,
    img,
    category,
  });
  next();
}

const removeItem = async (req) => {
  const { link } = req.body;
  if (!link) {
    throw new CustomError.BadRequestError('Item Doesn\'t exist');
  }
  const item = await Item.deleteOne({ link });
  next();
}

module.exports = {
  addITem,
  removeItem,
};