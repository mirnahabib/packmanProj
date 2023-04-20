const express = require('express');
const router = express.Router();

const {crawlbyCategory, crawlbyCategoryandUsed} = require('../controllers/crawlController')

router
    .route('/:cat/:search')
    .get(crawlbyCategory);

router
    .route('/used/:cat/:search')
    .get(crawlbyCategoryandUsed);


//this line is for test and should be removed
router.route('/').get(crawlbyCategory);

module.exports = router;