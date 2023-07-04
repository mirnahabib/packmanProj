const path = require('path');
const {spawn} = require("child_process");
const {  updatePriceIfChanged,
  } = require('../controllers/itemController');
const Item = require('../models/Item');
const Price = require('../models/Price');
const Favourite = require('../models/Favourite');

async function checkPriceFetch(link, store) {
  return new Promise((resolve, reject) => {
      const script = spawn('python', [path.join(__dirname, './checkprice/checkprice.py'), link, store]);
      script.stdout.on('data', (data) => {
      //console.log(data.toString());
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
    const favourites = await Favourite.find()
      .populate('item'); // Populate the 'item' field with the corresponding Item document

    const itemIds = favourites.map(favourite => favourite.item._id); // Get the item IDs from the favorites

    const items = await Item.find({
      _id: { $in: itemIds },
      lastFetched: { $lt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000) } // 2 days
    });
    //console.log(items);
    //price check each item then update in the database
    items.forEach(async (item) => {
      let storeName= item.store; //store names in the database aren't similar to store list in priceCheck
      checkPriceFetch(item.link, storeName)
      .then(async (result) => {
        jsonresult = JSON.parse(result);
        const newPrice = jsonresult[0].Price;
        console.log('new price found ' + newPrice);
        item.currentPrice = newPrice;
        await updatePriceIfChanged(item);
      })
      .catch((error) =>{
          console.log('price check method error: ' + error);
      });  
    });
  
  } catch (error) {
    console.error('Error retrieving favorite items:', error);
  }
}
  
function scheduleDailyPriceCheck() {
  setTimeout(function(){
    priceCheck();
    setInterval(priceCheck, 2 * 60 * 60 * 1000); // repeat every 2 hours
  });
}

module.exports = scheduleDailyPriceCheck;