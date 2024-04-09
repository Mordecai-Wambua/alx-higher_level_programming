#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list2 = list.map((x, idx) => x * idx);
console.log(list2);
