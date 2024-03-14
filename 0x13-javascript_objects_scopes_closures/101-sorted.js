#!/usr/bin/node
const dict = require('./101-data').dict;
const sorted = {};
Object.keys(dict).map(id => {
  const occ = dict[id];
  if (!sorted[occ]) {
    sorted[occ] = [];
  }
  sorted[occ].push(id);
  return sorted;
});
console.log(sorted);
