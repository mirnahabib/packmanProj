const express = require('express');
const router = express.Router();

const {crawlbyCategory} = require('../controllers/crawlController')

router
    .route('/:cat/:search')
    .get(crawlbyCategory);

//this line is for test and should be removed
router.route('/').get(crawlbyCategory);

module.exports = router;