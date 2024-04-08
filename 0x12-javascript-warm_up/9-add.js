#!/usr/bin/node
const { argv } = require('node:process');

const x = parseInt(argv[2]);
const y = parseInt(argv[3]);

add(x, y);
function add (a, b) {
  const c = a + b;
  console.log(c);
}
