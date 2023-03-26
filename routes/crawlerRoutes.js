const express = require('express');
const router = express.Router();

const {crawl} = require('../controllers/crawlController')

router
    .route('/:cat/:search')
    .get(crawl);

router.route('/').get(crawl);

module.exports = router;