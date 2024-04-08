#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;

argv.forEach((val, index) => {
	count += 1;
});

if (count <= 2)
{
	console.log('No argument');
}
else if (count <= 3)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
