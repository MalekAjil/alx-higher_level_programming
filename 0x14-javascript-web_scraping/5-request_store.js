#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function webContent (url, fPath) {
  request(url, (err, res, content) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else if (res.statusCode === 200) {
      fs.writeFile(fPath, content, 'utf-8', (err) => {
        if (err) {
          console.error(`Error: ${err.message}`);
        }
      });
    } else {
      console.error(`Error: ${res.statusCode}`);
    }
  });
}

const url = process.argv[2];
const fPath = process.argv[3];
webContent(url, fPath);
