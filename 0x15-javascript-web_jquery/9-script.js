$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function(data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
