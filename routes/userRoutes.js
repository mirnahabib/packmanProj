const express = require('express');
const router = express.Router();

const {
  authenticateUser,
  authorizePermissions,
} = require('../middleware/authentication');

const {
  getAllUsers,
  showCurrentUser,
  updateUser,
  updateUserPassword,
  getSingleUserbyId,
  getSingleUserbyemail,
  addUser,
} = require('../controllers/userController');

router
  .route('/')
  .get(getAllUsers);

router.route('/showMe').get(authenticateUser,showCurrentUser);
router.route('/updateProfile').patch(authenticateUser, updateUser);
router.route('/updatePassword').patch(authenticateUser, updateUserPassword);

router.route('/:id').get(authenticateUser, getSingleUserbyId);
router.route('/findbyemail/:email').get(getSingleUserbyemail);

//router.route('/addUser').post(addUser);

module.exports = router;
