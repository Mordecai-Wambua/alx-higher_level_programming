#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const output = JSON.parse(body);
  const completed = {};
  output.forEach((todo) => {
    if (todo.completed) {
      if (!completed[todo.userId]) {
        completed[todo.userId] = 0;
      }
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
