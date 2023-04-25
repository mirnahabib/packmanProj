const mongoose = require('mongoose');

const ItemSchema = mongoose.Schema({
    title: { type: String },
    price: { 
        type: String,
        default: '0.00' 
    },
    link: { type: String },
    img: { 
        type: String,
        default: '/public/productDefault.jpeg' 
    },   
    category: {
        type: String,
        enum: ['electronics', 'grocery', 'clothing', 'furniture', 'cosmetics', 'toys', 'used','other'],
    },   
    createdAt: { type: Date},
    available: { type: Boolean}
});

ItemSchema.pre('save', async function (){
    this.createdAt = new Date();
    this.available = true;
});

module.exports = mongoose.model('savedItem', ItemSchema);
