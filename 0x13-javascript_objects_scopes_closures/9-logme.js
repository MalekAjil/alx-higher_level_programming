#!/usr/bin/node
exports.logMe = function (item) {
  let n = 0;
  return function () {
    console.log(n + ': ' + item);
    n++;
  };
};
