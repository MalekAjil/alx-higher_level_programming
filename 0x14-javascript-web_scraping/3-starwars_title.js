#!/usr/bin/node
const request = require('request');

function starwarsTitle (id) {
  request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else {
      console.log(`${res.title}`);
    }
  });
}

const id = process.argv[2];
starwarsTitle(id);
