// -----------------------------------------------------------------------

// Countdown Timer --version 1 (It starts back on every reload and automatically submits form when the countdown ends)

var div = document.getElementById('display');
// var submitted = document.getElementById('submitted');

// function CountDown(duration, display) {

//     var timer = duration, minutes, seconds;

//     var interVal = setInterval(function () {
//         minutes = parseInt(timer / 60, 10);
//         seconds = parseInt(timer % 60, 10);

//         minutes = minutes < 10 ? "0" + minutes : minutes;
//         seconds = seconds < 10 ? "0" + seconds : seconds;
//         display.innerHTML = "<b>" + minutes + "m : " + seconds + "s" + "</b>";
//         if (timer > 0) {
//             --timer;
//         } else {
//             clearInterval(interVal)
//             SubmitFunction();
//         }

//     }, 1000);

// }

// function SubmitFunction() {
//     submitted.innerHTML = "Time is up!";
//     document.getElementById('timeover').submit();

// }
// CountDown(10, div);

// ---------------------------------------------------------------------------

// 24 hours Countdown Timer --version 2 (It doesn't starts back on every reload)


setInterval(function time(){
  var d = new Date();
  var hours = 24 - d.getHours();
  var min = 60 - d.getMinutes();
  if((min + '').length == 1){
    min = '0' + min;
  }
  var sec = 60 - d.getSeconds();
  if((sec + '').length == 1){
        sec = '0' + sec;
  } div.innerHTML = hours+':'+min+':'+sec;
}, 1000);

//   jQuery('#the-final-countdown p').html(hours+':'+min+':'+sec)