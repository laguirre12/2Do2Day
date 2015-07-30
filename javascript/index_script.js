function make_home_Appear()
{
  $('#home').addClass('appear');
  $('#home').removeClass('hidden');
  $('#about').removeClass('appear');
  $('#about').addClass('hidden');
};

function make_about_Appear()
{
  $('#about').addClass('appear');
  $('#about').removeClass('hidden');
  $('#home').removeClass('appear');
  $('#home').addClass('hidden');
};

console.log("hello");

$(document).ready(function(){
  pos = $("#work").position()
  $("#work").mouseover(function(){
      console.log("hello2");
      /*$("#index table").animate({bottom: '150px'});
      $("#work").animate({left: '15px'});
      $("#work").backgroundImage = "url('/images/exercise.png')";*/
      $("#work").addClass("angled");
  });
});

$(document).ready(function(){
  pos = $("#work").position()
  $("#work").mouseleave(function(){
      console.log("hello3");
      /*$("#index table").animate({bottom: '100px'});
      $("#work").animate({left: '10px'});
      $("#work").backgroundImage = "url('/images/suitcase.png')";*/
      $("#work").removeClass("angled");
  });
});
