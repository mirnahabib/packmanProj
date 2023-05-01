const mongoose = require('mongoose');

const FavSchema = mongoose.Schema({
    user: {
        type: mongoose.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    item: {
        type: mongoose.Types.ObjectId,
        ref: 'Item',
        required: true,
    },
});


module.exports = mongoose.model('favourite', FavSchema);