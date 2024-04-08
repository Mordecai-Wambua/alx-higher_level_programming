#!/usr/bin/node
const { argv } = require('node:process');

let number;
let i;
if (parseInt(argv[2])) {
  number = parseInt(argv[2]);
  for (i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
