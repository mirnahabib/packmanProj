const Notification = require('../models/Notification');
const { StatusCodes } = require('http-status-codes');


// Create a new notification
const createNotification = async (user, text) => {
  try{
    const notification = new Notification({
      user,
      text
    });
    await notification.save();
  } catch (err) {
    console.log(' create notification error: ' + err); 
}
};

// Get all notifications for a user
const getNotifications = async (req, res) => {
  const userId = req.body;
  try {
    const notifications = await Notification.find({ userId })
      .sort({ date: -1 }) 
      .limit(20); // Retrieve only the most recent 20 notifications

    res.status(StatusCodes.OK).json(notifications);
  } catch (error) {
    console.error('Error retrieving notifications:', error);
    res.status(500).json({ error: 'An error occurred while retrieving notifications' });
  }
  };
  

const notificationsSeen = async (req, res) => {
    try {
        const userId = req.body;
        const filter = { user: userId };
        const update = { read: true };
    
        await Notification.updateMany(filter, update);
        res.status(StatusCodes.OK);
      } catch (err) {
        console.log('Failed to mark notifications as seen: ', err);
        res.status();
      }
  };
  
  module.exports = {getNotifications, notificationsSeen, createNotification};
