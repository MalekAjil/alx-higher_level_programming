$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function(data, textStatus) {
    data.results.forEach(function(film) {
      const Item = $('<li></li>').text(film.title);
      $('UL#list_movies').append(Item);
    });
  });
});
