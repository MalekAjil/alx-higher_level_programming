#!/usr/bin/node
const SQ = require('./5-square');
class Square extends SQ {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (isNaN(c))
      c = 'X';
    for (let i = 0; i < this.size; i++)
      console.log(c.repeat(this.size));
  }
}
module.exports = Square;
