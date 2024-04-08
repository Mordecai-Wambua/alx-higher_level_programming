#!/usr/bin/node
const { argv } = require('node:process');

let number;
if (parseInt(argv[2])) {
  number = parseInt(argv[2]);
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
