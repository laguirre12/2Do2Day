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
  pos = $(".button").position()
  $(".button").mouseover(function(){
      console.log("hello2");
      /*$("#index table").animate({bottom: '150px'}); */
      $(".button").animate({bottom: '150px'});
  });
});

$(document).ready(function(){
  pos = $(".button").position()
  $(".button").mouseleave(function(){
      console.log("hello3");
      /*$("#index table").animate({bottom: '100px'});*/
      $(".button").animate({bottom: ("100px")});
  });
});
