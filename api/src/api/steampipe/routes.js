const express = require('express');
const router = express.Router();
const controller = require('./controllers');


router.get('/', (req, res) => { res.send('Ready to Query Steampie. Switch to POST Request Method');});
router.post('/query', controller.query);
router.post('/dynamic', controller.dynamicQuery);

module.exports = router;
