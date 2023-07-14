const express = require('express');
const { PythonShell } = require('python-shell');
const app = express();

app.use(express.json());

app.post('/recipes', (req, res) => {
    console.log(req.body);
    const url = req.body['request-url'];

    if (!url) {
        res.status(400).send(
            'Invalid request, please ensure the proper format is followed'
        );
    }

    const options = {
        args: [url],
        pythonPath:
            '/Users/nkapur/Local/kapur-home-stuff/recipe-scraper-rest-api/.venv/bin/python3.11',
        stdio: ['pipe', 'pipe', 'pipe', 'pipe'],
    };

    // Running the python script with the url passed
    const pyshell = new PythonShell(
        '/Users/nkapur/Local/kapur-home-stuff/recipe-scraper-rest-api/main.py',
        options
    );

    pyshell.on('message', (message) => {
        try {
            obj = JSON.parse(message);
            console.log(obj);
            res.send({
                response: `Your url is: ${url}`,
                recipe: obj,
            }).status(200);
            pyshell.end(function (err, code, signal) {
                if (err) throw err;
                console.log('The exit code was: ' + code);
                console.log('The exit signal was: ' + signal);
                console.log('finished');
            });
        } catch (e) {
            if (e instanceof SyntaxError)
                console.log(
                    "Text isn't valid JSON\n",
                    message,
                    '\nTrying the next message...'
                );
            else {
                console.log('\nUnknown Error\n', e);
            }
        }
    });

    pyshell.on('pythonError', (err) => {
        console.log(err);
        res.status(500).send('Uh oh');
    });

    pyshell.on('close', () => {
        console.log('Scraper ended');
    });

    // PythonShell.run('../main.py', options).then((messages) => {
    // });
});

// Starting server
const port = 3000;
app.listen(port, () =>
    console.log(`Recipe Scrapper API listening on port ${port}`)
);
