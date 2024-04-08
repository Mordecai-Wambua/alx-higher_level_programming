#!/usr/bin/node
const { argv } = require('node:process');

let number;
let i;
if (parseInt(argv[2])) {
  number = parseInt(argv[2]);
  for (i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
