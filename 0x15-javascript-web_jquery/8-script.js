$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const output = data.results;
    for (let i = 0; i < output.length; i++) {
      $('UL#list_movies').append(`<li>${output[i].title}</li>`);
    }
  });
});
