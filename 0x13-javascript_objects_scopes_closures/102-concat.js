#!/usr/bin/node
const fs = require('fs');
const txt1 = fs.readFileSync(process.argv[2], 'utf8');
const txt2 = fs.readFileSync(process.argv[3], 'utf8');
const txt3 = txt1 + txt2;
fs.writeFileSync(process.argv[4], txt3, 'utf8');
