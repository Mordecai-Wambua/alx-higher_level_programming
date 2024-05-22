#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const output = JSON.parse(body).characters;
  output.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  });
});
