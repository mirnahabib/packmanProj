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

PriceSchema.pre('save', async function (){
    this.date = new Date();
});

module.exports = mongoose.model('price', PriceSchema);