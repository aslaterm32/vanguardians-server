require('dotenv').config()
const { Pool } = require('pg')

 const db = new Pool({
    connectionString: process.env.DB_URL
 })

 console.log('Connect to DB')

 module.exports = db