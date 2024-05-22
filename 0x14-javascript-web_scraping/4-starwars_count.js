#!/usr/bin/node
const request = require('request');
let counter = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const output = JSON.parse(body).results;
  output.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(18)) {
        counter++;
      }
    });
  });
  console.log(counter);
});
