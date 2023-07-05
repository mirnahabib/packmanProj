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
  const userId = req.user.userId;
  try {
    const notifications = await Notification.find({ user:userId })  
      .populate('item', 'link')
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
      const userId = String(req.user.userId);
      const response = await Notification.updateMany( {user: userId}, {$set: {seen: true}}, {upsert: true});
      res.status(StatusCodes.OK).json({msg: "notifications updated."});
      } catch (err) {
        console.log('Failed to mark notifications as seen: ', err);
        res.status(StatusCodes.BAD_REQUEST);
      }
  };
  
  module.exports = {getNotifications, notificationsSeen, createNotification};
