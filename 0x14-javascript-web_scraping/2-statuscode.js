#!/usr/bin/node
const request = require('request');

function displaySC (url) {
  request(url, (err, res) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else {
      console.log(`code: ${res.statusCode}`);
    }
  });
}

const url = process.argv[2];
displaySC(url);
