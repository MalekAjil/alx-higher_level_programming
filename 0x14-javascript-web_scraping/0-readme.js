#!/usr/bin/node
const fs = require('fs');

function printFile(fPath) {
  fs.readFile(fPath, 'utf-8', (err, txt) => {
    if (err) {
      console.error('Error: ${err.message}');
    } else {
      console.log(txt);
    }
  });
}

const fPath = process.argv[2];
printFile(fPath);
