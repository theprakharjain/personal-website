// The functions which run windows load event

window.addEventListener("load", () => {
  // Function to check whether script is running or not
  console.log("helloooooooooo");

  // Setting the value in localstorage/cookies to check whether the page is loaded for the
  // first time or not
  // also sends an alert if the page is loaded for the first time
  var second_time = localStorage.getItem("first_time");

  if (!second_time) {
    localStorage.setItem("first_time", "1");
    window.alert("This Project sometimes may not work on small touch devices");
  }

    // Making html elements ---- "loader", "loader_text", "mousepos" visible while drawing on canvas
    document.getElementById("loader").style.visibility = "visible";
    document.getElementById("loader_text").style.visibility = "visible";
    document.getElementById("mousepos").style.visibility = "visible";

  // calling the "inactivityTime" function
  inactivityTime();

// Sets the responsiveness to the canvas
// Gives the prediction in the alert box on small screen
// for the improve visibility on small screens
  var canvas = document.getElementById("canvas");
  if (window.innerWidth < 500 || window.innerHeight < 500){
        var canvas = document.getElementById("canvas");
        var height_ratio = 1;
        // 12px is deducted in order to remove the spacing issue in mobile site
        // if we'll not deduct the border then canvas will take the extra space of 12px (6px of right and 6px of left)
        // and will not fit in the mobile/tab window
        // Another way is to set the border as none for the canvas in the media query *currently commented out*
        canvas.width = window.innerWidth - 12;
        canvas.height = canvas.width * height_ratio;
        // console.log(canvas.width, canvas.height, window.innerWidth, "hua kyaaaa");

        // Sets the prediction display as none and
        // transfers the value of prediction to the alert box and displays it
        var answer = document.getElementById("answer");
        answer.style.display = "none";

        window.confirm(answer.textContent);

  } else {
      canvas.width = 500;
      canvas.height = 500;
    //   console.log("nai hua kyaaaa");
  }


});



// ---------------------------------------------------------------------------------------------------------------------------

// Variables for referencing the canvas and 2dcanvas context
var canvas, ctx;

// Variables to keep track of the mouse position and left-button status 
var mouseX, mouseY, mouseDown = 0;

// Variables to keep track of the touch position
var touchX, touchY;

// Draws a dot at a specific position on the supplied canvas name
// Parameters are: A canvas context, the x position, the y position, the size of the dot
function drawDot(ctx, x, y, size) {
    // Let's use black by setting RGB values to 0, and 255 alpha (completely opaque)
    r = 255; g = 255; b = 255; a = 255;

    // Select a fill style
    ctx.fillStyle = "rgba(" + r + "," + g + "," + b + "," + (a / 255) + ")";

    // Draw a filled circle
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fill();
}

// Clear the canvas context using the canvas width and height
function clearCanvas(canvas, ctx) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Keep track of the mouse button being pressed and draw a dot at current location
function sketchpad_mouseDown() {
    mouseDown = 1;
    drawDot(ctx, mouseX, mouseY, 12);
}

// Keep track of the mouse button being released
function sketchpad_mouseUp() {
    mouseDown = 0;
}

// Keep track of the mouse position and draw a dot if mouse button is currently pressed
function sketchpad_mouseMove(e) {
    // Update the mouse co-ordinates when moved
    getMousePos(e);

    // Draw a dot if the mouse button is currently being pressed
    if (mouseDown == 1) {
        drawDot(ctx, mouseX, mouseY, 12);
    }
}

// Get the current mouse position relative to the top-left of the canvas
function getMousePos(e) {
    if (!e)
        var e = event;

    if (e.offsetX) {
        mouseX = e.offsetX;
        mouseY = e.offsetY;
    }
    else if (e.layerX) {
        mouseX = e.layerX;
        mouseY = e.layerY;
    }
}

// Draw something when a touch start is detected
function sketchpad_touchStart() {
    // Update the touch co-ordinates
    getTouchPos();

    drawDot(ctx, touchX, touchY, 12);

    // Prevents an additional mousedown event being triggered
    event.preventDefault();
}

// Draw something and prevent the default scrolling when touch movement is detected
function sketchpad_touchMove(e) {
    // Update the touch co-ordinates
    getTouchPos(e);

    // During a touchmove event, unlike a mousemove event, we don't need to check if the touch is engaged, since there will always be contact with the screen by definition.
    drawDot(ctx, touchX, touchY, 12);

    // Prevent a scrolling action as a result of this touchmove triggering.
    event.preventDefault();
}

// Get the touch position relative to the top-left of the canvas
// When we get the raw values of pageX and pageY below, they take into account the scrolling on the page
// but not the position relative to our target div. We'll adjust them using "target.offsetLeft" and
// "target.offsetTop" to get the correct values in relation to the top left of the canvas.
function getTouchPos(e) {
    if (!e)
        var e = event;

    if (e.touches) {
        if (e.touches.length == 1) { // Only deal with one finger
            var touch = e.touches[0]; // Get the information for finger #1
            touchX = touch.pageX - touch.target.offsetLeft;
            touchY = touch.pageY - touch.target.offsetTop;
        }
    }
}


// Set-up the canvas and add our event handlers after the page has loaded
function init() {
    // Get the specific canvas element from the HTML document
    canvas = document.getElementById('canvas');

    // Set the Background color of canvas black
    canvas.style.backgroundColor = "#000000";

    // If the browser supports the canvas tag, get the 2d drawing context for this canvas
    if (canvas.getContext)
        ctx = canvas.getContext('2d');

    // Check that we have a valid context to draw on/with before adding event handlers
    if (ctx) {
        // React to mouse events on the canvas, and mouseup on the entire document
        canvas.addEventListener('mousedown', sketchpad_mouseDown, false);
        canvas.addEventListener('mousemove', sketchpad_mouseMove, false);
        window.addEventListener('mouseup', sketchpad_mouseUp, false);

        // React to touch events on the canvas
        canvas.addEventListener('touchstart', sketchpad_touchStart, false);
        canvas.addEventListener('touchmove', sketchpad_touchMove, false);
    }
}


// ------------------------------------------------------------------------------------------------------------------

// Function to show mouse coordinates on screen
function showCoords(event) {
  var x = event.clientX;
  var y = event.clientY;
  var coor = "Calculating Mouse Position - X coords: " + x + ", Y coords: " + y;
  document.getElementById("mousepos").innerHTML = coor;
}

// Function to hide mouse coordinates from screen
function clearCoor() {
  document.getElementById("mousepos").innerHTML = "";
}

// Function to download the drawn image on canvas
function downloaded() {
  var download = document.getElementById("downloader");
  var image = document
    .getElementById("canvas")
    .toDataURL("image/jpeg")
    .replace("image/jpeg", "image/octet-stream");
  download.setAttribute("href", image);
}

// Function to transfer the DataURL of canvas to the value of "link" element
// It transforms the image of the canvas in encoded strings
// and then assigns the encoded value of canvas to "link" value
// It further get transferred to the "app.py" file upon the submission of form
// on the click of the "predict" button
function link_send() {
  var link_transfer = document.getElementById("link");
  var canvas = document.getElementById("canvas");
  var dataURL = canvas.toDataURL();
  link_transfer.setAttribute("value", dataURL);
}

// Manipulating the position of loader(dog animation) upon the show of prediction text
if (document.getElementById("answer").innerText != "") {
  document.getElementById("loader").style.top = "25%";
} else {
  document.getElementById("loader").style.top = "37%";
}



// Function to make the predict button blink upon the inactivity on screen
var inactivityTime = function () {
  // Variable to store inactivity time
  var time;

  // Events to restart/reset the inactivity time
  document.onload = resetTimer;
  document.onmousemove = resetTimer;
  document.onmousedown = resetTimer; // touchscreen presses
  document.ontouchstart = resetTimer;
  document.onclick = resetTimer; // touchpad clicks
  document.onkeypress = resetTimer;
  document.addEventListener("scroll", resetTimer, true); // improved; see comments

  // Function to add the glow animation to the predict button
  function btn_blink() {
    document.getElementById("submit_link").style.animation =
      "glowing 1300ms infinite";
    //location.href = 'logout.html'
  }

  // Function to reset time variable upon any activity on the screen
  function resetTimer() {
    // Method to clear out the value stored in the time variable upon the initiation of the function
    clearTimeout(time);
    // Assigning the Method "setTimeout" to the variable time
    // Setting the limit of 6 seconds to start the "btn_blink" function which sets the animation on the predict button
    time = setTimeout(btn_blink, 6000);
    // 1000 milliseconds = 1 second
  }
};


// // To position the canvas upon the change in the size of the window
// var positionCanvas = function(){
//     // canvas.style.position = 'absolute';
//     canvas.style.top = window.innerHeight / 2 - canvas.height / 2 + 'px';
//     canvas.style.left = window.innerWidth / 2 - canvas.width / 2 + 'px';
// };
 
// // attach position canvas method to window resize event
// window.addEventListener('resize', positionCanvas);
// // call it for the first time
// positionCanvas();

// function resize () {
//     var canvas = document.getElementById("canvas");
//     var canvasRatio = canvas.height /canvas.width;
//     var windowsRatio = window.innerHeight / window.innerWidth;
//     var width;
//     var height;

//     if (windowsRatio < canvasRatio){
//         height = window.innerHeight;
//         width = height / canvasRatio;
//     } else {
//         width = window.innerWidth;
//         height = width * canvasRatio;
//     }

//     canvas.style.width = width + "px";
//     canvas.style.height = height + "px";

// }

// window.addEventListener("resize", resize, false);


// function resize () {
//     var canvas = document.getElementById("canvas");

//     if (canvas.width > window.innerWidth){
//         canvas.width = window.innerWidth;
//     } else {
//         canvas.width = 500 + "px";
//     }
//     if (canvas.height > window.innerHeight){
//         canvas.height = window.innerHeight;
//     } else {
//         canvas.height = "500px";
//     }
// }

// window.addEventListener("resize", resize);



// function resize () {
//     var canvas = document.getElementById("canvas");

//     if (window.innerWidth < "500px" || window.innerHeight < "500px"){
//         var height_ratio = 1;
//         canvas.width = window.innerWidth;
//         canvas.height = canvas.width * height_ratio;
//         console.log("hua kyaaaa");
//     }

//     // var height_ratio = 1;

//     // canvas.height = canvas.width * height_ratio;
// }

// window.addEventListener("resize", resize);


// if (window.innerWidth < "500" || window.innerHeight < "500"){
//         var canvas = document.getElementById("canvas");
//         var height_ratio = 1;
//         canvas.width = window.innerWidth;
//         canvas.height = canvas.width * height_ratio;
//         console.log("hua kyaaaa");
//     }