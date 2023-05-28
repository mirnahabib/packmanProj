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
            res.status(204).json({ msg: 'Favourite removed successfully' });

        }else{
            await favourite.create(fav);
            res.status(StatusCodes.CREATED).json({msg: 'Favourite Added successfully' });

        }
        
    }catch (error){
        console.log(error);
    }
}

const favList = async (req, res) => {
    try{
        const user = req.user.userId;
        const favItems = await favourite.find({ user: user });
        const itemId = favItems.map((favItem) => favItem.item);
        const favlist = await Item.find({ _id: { $in: itemId } });
        res.status(StatusCodes.OK).json({favlist});
        
    }catch (error){
        console.log(error);
    }
}
module.exports = {
    fav,
    favList
  };