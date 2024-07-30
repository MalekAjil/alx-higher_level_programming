#!/usr/bin/node
const fs = require('fs');

function writeFile (fPath, txt) {
  fs.writeFile(fPath, txt, 'utf-8', (err) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    }
  });
}

const fPath = process.argv[2];
const txt = process.argv[3];
writeFile(fPath, txt);
