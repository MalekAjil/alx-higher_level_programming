#!/usr/bin/node
const request = require('request');

function starwarsTitle (id) {
  request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, content) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else if (res.statusCode === 200) {
      console.log(JSON.parse(content).title);
    } else {
      console.error(`Error: ${res.statusCode}`);
    }
  });
}

const id = process.argv[2];
starwarsTitle(id);
