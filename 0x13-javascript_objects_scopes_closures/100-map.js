#!/usr/bin/node
const list = require('./100-data').list;
const newlist = list.map((num, idx) => { return num * idx; });
console.log(list);
console.log(newlist);
