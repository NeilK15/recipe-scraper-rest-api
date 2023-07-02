const express = require('express');
const app = express();

app.get('/', (req, res) => {});

// Starting server
const port = 3000;
app.listen(port, () =>
	console.log(`Recipe Scrapper API listening on port ${port}`)
);
