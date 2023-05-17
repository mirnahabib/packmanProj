const path = require('path');
const {spawn} = require("child_process");
const {  updatePriceIfChanged,
  } = require('../controllers/itemController');
const Item = require('../models/Item');
const Price = require('../models/Price');


async function checkPriceFetch(link, store) {
  return new Promise((resolve, reject) => {
      const script = spawn('python', [path.join(__dirname, './checkprice/checkprice.py'), link, store]);
      script.stdout.on('data', (data) => {
      console.log(data.toString());
      resolve(data.toString());
      });
      script.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      reject(new Error(`Python check price script error: ${data}`));
      });
  
      script.on('close', (code) => {
      if (code !== 0) {
          reject(new Error(`Python check price script exited with code ${code}`));
      }
      //resolve();
      });
  });
  }


const priceCheck = async() => {
  try {
    const favorites = await Favorite.find({ user: userId })
      .populate('item'); // Populate the 'item' field with the corresponding Item document

    const itemIds = favorites.map(favorite => favorite.item._id); // Get the item IDs from the favorites

    const items = await Item.find({
      _id: { $in: itemIds },
      lastFetched: { $lt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000) } // 2 days
    });
    //price check each item then update in the database
    items.forEach(async (item) => {
      let storeName= item.store.toLowerCase().replace(/\s/g, ""); //store names in the database aren't similar to store list in priceCheck
      checkPriceFetch(item.link, storeName)
      .then(async (result) => {
        console.log(result);
        const newPrice = result[0].Price;
        console.log(newPrice);
        item.Price = newPrice;
        updatePriceIfChanged(item);
      })
      .catch((error) =>{
          console.log('price check method error: ' + error);
      });  
      try {
        await item.save(); // Save the updated item
      } catch (error) {
        console.log('Error updating item:', error);
      }
    });
  
  } catch (error) {
    console.error('Error retrieving favorite items:', error);
  }
}
  
function scheduleDailyPriceCheck() {
  const now = new Date();
  let millisTill6pm = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 18, 0, 0, 0) - now;
  if (millisTill6pm < 0) {
      millisTill6pm += 86400000; // it's after 6pm, try 6pm tomorrow.
  }
  setTimeout(function(){
    priceCheck();
    setInterval(priceCheck, 2 * 60 * 60 * 1000); // repeat every 2 hours
  }, millisTill6pm);
}

module.exports = scheduleDailyPriceCheck;