const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ItemSchema = mongoose.Schema({
    title: { type: String },
    store: { type: String },
    currentPrice: { 
        type: Number,
        default: 0.00 
    },
    link: { type: String },
    img: { 
        type: String,
        default: '/public/productDefault.jpeg' 
    },   
    category: {
        type: String,
        enum: ['electronics', 'grocery', 'clothing', 'furniture', 'cosmetics', 'toys', 'used', 'games', 'other'],
    },   
    lastFetched: { type: Date},
});

ItemSchema.pre('save', async function (){
    this.lastFetched = new Date();
});

ItemSchema.post('findOne', function(next) {
    this.update({}, { $set: { lastFetched: new Date() } });
  });
  
module.exports = mongoose.model('Item', ItemSchema);
