const Item = require('../models/Item');
const favourite = require('../models/Favourite');
const { StatusCodes } = require('http-status-codes');
const CustomError = require('../errors');

const fav = async (req, res) => {
    try{
        const { userId, link } = req.body;
        if (!link) {
            throw new CustomError.BadRequestError('You can\'t fav an item without link');
        }
        const item = await Item.findOne({ link });
        const fav = {user: userId, item: item._id};
        const existingFav = await favourite.findOne(fav);
        if(existingFav){
            await favourite.deleteOne(fav);
        }else{
            await favourite.create(fav);
        }
        res.status(StatusCodes.OK);
        
    }catch (error){
        console.log(error);
    }
}

const favList = async (req, res) => {
    try{
        const { userId } = req.body;
        const favlist = await favourite.find({ user: userId });
        res.status(StatusCodes.OK).json({favlist});
        
    }catch (error){
        console.log(error);
    }

}
module.exports = {
    fav,
    favList
  };