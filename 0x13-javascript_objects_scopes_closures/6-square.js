#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
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
module.exports = Square;
