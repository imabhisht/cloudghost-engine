require('dotenv').config();
const express = require('express');
const app = require('./app');

const port = process.env.API_PORT;

app.listen(port, () => {
    console.log(`[CloudGhost-API]: Listening on port ${port}`);
});