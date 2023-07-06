const express = require('express');
const { PythonShell } = require('python-shell');
const app = express();

app.use(express.json());

app.post('/recipes', (req, res) => {
	const url = req.body['request-url'];

	const options = {
		args: [url],
		stdio: ['pipe', 'pipe', 'pipe', 'pipe'],
	};

	// Running the python script with the url passed
	const pyshell = new PythonShell('../main.py', options);

	pyshell.on('message', (message) => {
		try {
			obj = JSON.parse(message);
			console.log(obj);
			res.send({
				response: `Your url is: ${url}`,
				recipe: obj,
			}).status(200);
		} catch (err) {
			console.log(message, err);
		}
	});

	// PythonShell.run('../main.py', options).then((messages) => {
	// });
});

// Starting server
const port = 3000;
app.listen(port, () =>
	console.log(`Recipe Scrapper API listening on port ${port}`)
);
