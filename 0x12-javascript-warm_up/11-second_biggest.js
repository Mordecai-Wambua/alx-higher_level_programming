#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;

argv.forEach((val, index) => {
  count += 1;
});

if (count <= 3) {
  console.log(0);
} else {
  const j = argv.map(Number)
    .slice(2, argv.length)
    .sort((x, y) => x - y);
  console.log(j[j.length - 2]);
}
