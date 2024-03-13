#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
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
