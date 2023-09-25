require('dotenv').config();
const fs = require('fs');
const db = require('./connect');

const sql = fs.readFileSync('./database/setup.sql').toString();

db.query(sql)
    .then((data) => {
        db.end();
        console.log('DB setup complete');
    })
    .catch((error) => {
        console.log(error);
    });
