#!/usr/bin/node
const request = require('request');

function starwarsCount () {
  request(`https://swapi-api.alx-tools.com/api/films`, (err, res, content) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else if (res.statusCode === 200) {
      const movies = JSON.parse(content);
      let count = 0;
      for (movie in movies) {
	if (movie.charcter === 'Wedge Antilles') {
	  count++;
	}
      }
      console.log(count);
    } else {
      console.error(`Error: ${res.statusCode}`);
    }
  });
}

starwarsCount();
