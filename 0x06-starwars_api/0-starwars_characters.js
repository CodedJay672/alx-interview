#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid Status Code Returned:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error(
            'Invalid Status Code Returned:',
            response.statusCode
          );
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
