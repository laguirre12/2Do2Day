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


$(document).ready(function(){
  pos = $("#work").position()
  $("#work").mouseover(function(){
      $("#work").addClass("left_angled");
  });
});

$(document).ready(function(){
  pos = $("#work").position()
  $("#work").mouseleave(function(){
      $("#work").removeClass("left_angled");
  });
});

$(document).ready(function(){
  pos = $("#school").position()
  $("#school").mouseover(function(){
      $("#school").addClass("right_angled");
  });
});

$(document).ready(function(){
  pos = $("#school").position()
  $("#school").mouseleave(function(){
      $("#school").removeClass("right_angled");
  });
});


/* -------------------------------------------------------- */
$(document).ready(function(){
  pos = $("#exercise").position()
  $("#exercise").mouseover(function(){
      $("#exercise").addClass("left_angled");
  });
});

$(document).ready(function(){
  pos = $("#exercise").position()
  $("#exercise").mouseleave(function(){
      $("#exercise").removeClass("left_angled");
  });
});

$(document).ready(function(){
  pos = $("#stay_home").position()
  $("#stay_home").mouseover(function(){
      $("#stay_home").addClass("right_angled");
  });
});

$(document).ready(function(){
  pos = $("#stay_home").position()
  $("#stay_home").mouseleave(function(){
      $("#stay_home").removeClass("right_angled");
  });
});
