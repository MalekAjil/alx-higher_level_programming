$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function(data, textStatus) {
    for (let film in data.results) {
      const Item = $('<li></li>').text(film.title);
      $('UL#list_movies').append(Item);
    }
  });
});
