function make_home_Appear()
{
  $('#home').addClass('appear');
  $('#home').removeClass('hidden');
  $('#about').removeClass('appear');
  $('#about').addClass('hidden');
  $('#contact').removeClass('appear');
  $('#contact').addClass('hidden');
};

function make_about_Appear()
{
  $('#about').addClass('appear');
  $('#about').removeClass('hidden');
  $('#home').removeClass('appear');
  $('#home').addClass('hidden');
  $('#contact').removeClass('appear');
  $('#contact').addClass('hidden');
};

function make_contact_Appear()
{
  $('#contact').addClass('appear');
  $('#contact').removeClass('hidden');
  $('#home').removeClass('appear');
  $('#home').addClass('hidden');
  $('#about').removeClass('appear');
  $('#about').addClass('hidden');
};


/* -------------  makes work tilt on mouseover  ---------------------- */

$(document).ready(function(){
  $("#work").mouseover(function(){
      $("#work").addClass("left_angled");
  });
});

$(document).ready(function(){
  $("#work").mouseleave(function(){
      $("#work").removeClass("left_angled");
  });
});

/* -------------  makes school tilt on mouseover  ---------------------- */

$(document).ready(function(){
  $("#school").mouseover(function(){
      $("#school").addClass("right_angled");
  });
});

$(document).ready(function(){
  $("#school").mouseleave(function(){
      $("#school").removeClass("right_angled");
  });
});


/* -------------  makes exercise tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#exercise").mouseover(function(){
      $("#exercise").addClass("left_angled");
  });
});

$(document).ready(function(){
  $("#exercise").mouseleave(function(){
      $("#exercise").removeClass("left_angled");
  });
});

/* -------------  makes stay_home tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#stay_home").mouseover(function(){
      $("#stay_home").addClass("right_angled");
  });
});

$(document).ready(function(){
  $("#stay_home").mouseleave(function(){
      $("#stay_home").removeClass("right_angled");
  });
});


/* -------------  makes music tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#music").mouseover(function(){
      $("#music").addClass("right_angled");
  });
});

$(document).ready(function(){
  $("#music").mouseleave(function(){
      $("#music").removeClass("right_angled");
  });
});


/* -------------  makes stress tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#stress").mouseover(function(){
      $("#stress").addClass("left_angled");
  });
});

$(document).ready(function(){
  $("#stress").mouseleave(function(){
      $("#stress").removeClass("left_angled");
  });
});


/* -------------  makes chill tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#chill").mouseover(function(){
      $("#chill").addClass("right_angled");
  });
});

$(document).ready(function(){
  $("#chill").mouseleave(function(){
      $("#chill").removeClass("right_angled");
  });
});


/* -------------  makes crazy tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#crazy").mouseover(function(){
      $("#crazy").addClass("left_angled");
  });
});

$(document).ready(function(){
  $("#crazy").mouseleave(function(){
      $("#crazy").removeClass("left_angled");
  });
});
