var latest_response;

$(document).ready(function() {
  $("#search").keyup(function() {
      typewatch(get_titles, 300 );
  });
  input_search = $("#search");
  search_results = $(".search-results");
  search_results.hide();
  search_results.width($("#search").width());
  search_results.css("top",input_search.position().top+input_search.height());
  search_results.css("left",input_search.position().left);
  
  $("#grab").click(function() {
      grab_movies($("#search").val());
  });
});
var typewatch = function(){
    var timer = 0;
    return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    }
}();
function get_titles() {
  title = $('#search').val();
  if (title.length < 4) {
    return;
  }
  $(".search-results").empty();
  url = '/json/imdb?method=get_matching_titles&title='+encodeURIComponent(title);
  $.get(url, function(data) {
      if (data == '') {
        return;
      }
      var movie_list = JSON.parse(data);
      latest_response = movie_list;
      for (i in movie_list) {
        if (movie_list[i].title.toLowerCase().indexOf(title.toLowerCase()) == -1) {
          delete movie_list[i];
        }
      }
      for (i in movie_list) {
        var result = '<p class="search-result">'+movie_list[i].title+'</p>';
        $(".search-results").append(result);
      }
      $(".search-result").click(function() {
          $("#search").val($(this).html());
          $(".search-results").hide();
      });
      $(".search-results").show();
  });
}

function grab_movies(title) {
  $('#big-results').empty();
  if (!latest_response) {
    get_titles();
  }
  if (latest_response.length == 1) {
    window.location = 'dsadasdas';
  }
  for (i in latest_response) {
    movie = latest_response[i];
    var big_result = '<p><a href="http://www.imdb.com'+movie.link+'">'+movie.title+'</a></p>';
    $('#big-results').append(big_result);
  }
}
