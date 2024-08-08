$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function(data, textStatus) {
    const name = data.name;
    $('DIV#character').text(data.name);
    alert("Done, with the following status: " + textStatus + ". Here is the response: " + data);
  });
});
