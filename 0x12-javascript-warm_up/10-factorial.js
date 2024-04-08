#!/usr/bin/node
const { argv } = require('node:process');
const x = parseInt(argv[2]);
console.log(factorial(x));

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
