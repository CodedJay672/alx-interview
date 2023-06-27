#!/usr/bin/node

// import the request
const request = require('request');

// save command line argument
const arg = process.argv[2];

// request from the api and store result in response
const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;

// request for the url
request(url, async (error, response, body) => {
  if (error) { console.log(error); }

  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) { console.log(error); }
        console.log(JSON.parse(body).name);
      });
      resolve();
    });
  }
});
