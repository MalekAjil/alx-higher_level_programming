#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const x of list) {
    if (x === searchElement) {
      c++;
    }
  }
  return c;
};
