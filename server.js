const cors = require('cors')
const express = require('express')

const app = express()

app.use(cors)
app.use(express.static('.'));


const PORT = process.env.PORT || 3001

app.listen(PORT)
