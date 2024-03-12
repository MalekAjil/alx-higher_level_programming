#!/usr/bin/node
const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(n1, n2);
