const mongoose = require('mongoose');

const NotificationSchema = mongoose.Schema({
    user: {
        type: mongoose.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    item: { 
        type: mongoose.Types.ObjectId,
        ref: 'Item',
    },
    text: { type: String, required: true },
    seen: { type: Boolean, default: false,},
    date: { type: Date, default: Date.now}
});

NotificationSchema.pre('save', async function (){
    this.date = new Date();
});

module.exports = mongoose.model('Notification', NotificationSchema);