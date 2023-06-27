const mongoose = require('mongoose');

const PriceSchema = mongoose.Schema({
    item: {
        type: mongoose.Types.ObjectId,
        ref: 'Item',
        required: true,
    },
    price: { type: Number },
    date: { type: Date }
});


module.exports = mongoose.model('price', PriceSchema);