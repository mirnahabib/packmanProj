const Item = require('../models/Item');
const favourite = require('../models/Favourite');
const { StatusCodes } = require('http-status-codes');
const CustomError = require('../errors');
const {
  checkPermissions,
} = require('../utils');

const addITem = async (req, res, next) => {
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


async function updatePriceIfChanged(item) {
  const existingItem = await Item.findOne({ link: item.link });
  if (existingItem && existingItem.currentPrice != item.currentPrice) {
      console.log(`Unmatching prices curr: ${existingItem.currentPrice} new: ${item.Price}`);
      const oldPrice = existingItem.currentPrice;
      await Item.findOneAndUpdate({ link: item.link }, { $set: { currentPrice: item.currentPrice, lastFetched: Date.now() } });
      const price = new Price({
          item: existingItem,
          price: oldPrice,
      });
      await Price.create(price);
  }
}

async function storeItems(itemsJson, category) {
  for (let i = 0; i < itemsJson.length; i++) {
      const item = new Item({
          title: itemsJson[i].Title,
          currentPrice: itemsJson[i].Price,
          link: itemsJson[i].Link,
          img: itemsJson[i].Img,
          store: itemsJson[i].Shop,
          category: category,
      });
      const existingItem = await Item.findOne({ link: item.link });
      if(existingItem){
          await updatePriceIfChanged(item);
      }
      if (!existingItem && item.currentPrice != null && item.currentPrice != 0) {
          await Item.create(item);
      }
  }
}


module.exports = {
  addITem,
  removeItem,
  storeItems,
  updatePriceIfChanged,
};