process.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');
process.stdin.on('data', (data) => {
    const name = data.trim();
    process.write(`Your name is: ${name}\n`);
    process.exit();
    }
);
