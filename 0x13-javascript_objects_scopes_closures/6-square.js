#!/usr/bin/node
const Square = require('./5-square');
class MySquare extends Square {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (typeof(c) == 'undefined' || c === null) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = MySquare;
