require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
const sequalize = require('./init/sequalize');
const morgan = require('morgan');
// Middleware
app.use(cors());
app.use(express.json());
app.use(morgan('combined'))
app.use(express.urlencoded({ extended: true }));

// Routes

app.get('/',(req,res) => res.status(200).send({message: "Welcome to CloudGhost API"}));

app.use('/cq/api', require('./api/steampipe/routes'));

app.get('/cq/api/status', (req, res) => {
    res.send('Ready to Query Steampipe on this Route!');
}
);




module.exports = app;



