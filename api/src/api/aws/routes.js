const express = require('express');
const router = express.Router();
const controller = require('./controllers');


router.get('/', (req, res) => { res.send('Ready to Query AWS. Switch to POST Request Method');});
router.post('/test', controller.test);

router.post('/query', controller.query_aws);

module.exports = router;
