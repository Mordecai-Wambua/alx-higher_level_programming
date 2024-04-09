#!/usr/bin/node
const Sq = require('./5-square.js');

module.exports = class Square extends Sq {
  charPrint (c = 'X') {
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.width));
    }
  }
};
