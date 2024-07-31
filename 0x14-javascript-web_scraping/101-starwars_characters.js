#!/usr/bin/node
const request = require('request');

function starwarsCount (url) {
  request(url, (err, res, content) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else if (res.statusCode === 200) {
      const movies = JSON.parse(content);
      const character = 'https://swapi-api.alx-tools.com/api/people/18/';
      const WAMovies = movies.results.filter((movie) =>
        movie.characters.includes(character)
      );
      console.log(WAMovies.length);
    } else {
      console.error(`Error: ${res.statusCode}`);
    }
  });
}

const url = process.argv[2];
starwarsCount(url);
