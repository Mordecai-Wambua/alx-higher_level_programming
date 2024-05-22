#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/'

request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const output = JSON.parse(body)
  console.log(output.title)
});
