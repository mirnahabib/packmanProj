const express = require('express');
const router = express.Router();

const { authenticateUser } = require('../middleware/authentication');
const { addITem } = require('../controllers/itemController');
const { fav, favList } = require('../controllers/favouriteController');

router.post('/addOrRemove', authenticateUser, fav);
router.get('/', authenticateUser, favList);

module.exports = router;
