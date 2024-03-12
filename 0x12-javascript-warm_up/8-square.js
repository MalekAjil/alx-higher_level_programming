#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  let s = '';
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      s += 'X';
    }
    if (i < n - 1) {
      s += '\n';
    }
  }
  console.log(s);
}
