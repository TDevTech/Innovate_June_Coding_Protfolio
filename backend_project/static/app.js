
function darkMode()
{
let element = document.body;
// let element.classList.toggle("dark-mode");
let mainBox = document.getElementsByClassName ("main-box");
let mainText = document.getElementsByClassName ("main-text");
let exampleText = document.getElementsByClassName("example-text");
let state = localStorage.getItem("state")


element.classList.toggle("dark-mode");
for (const i of mainBox)
{
    i.classList.toggle("dark-mode")
}

for (const x of mainText){
    x.classList.toggle("dark-mode")
}

for (const y of exampleText)
{
    y.classList.toggle("dark-mode")
}

if (state !== "dark")
{
    localStorage.setItem("state","dark")
}  
else
{
    localStorage.setItem("state","light")
}

}

function darkCheck()
{
    let element = document.body;
    // let element.classList.toggle("dark-mode");
    let mainBox = document.getElementsByClassName ("main-box");
    let mainText = document.getElementsByClassName ("main-text");
    let exampleText = document.getElementsByClassName("example-text");
    let state = localStorage.getItem("state") 

    if (state === "dark")
    {
        element.classList.toggle("dark-mode");
        for (const i of mainBox)
        {
            i.classList.toggle("dark-mode")
        }
        
        for (const x of mainText){
            x.classList.toggle("dark-mode")
        }  
    }
}

// ------------
// const toggleBtn = document.getElementById("toggle-btn");
// const theme = document.getElementById("theme");
// let darkMode = localStorage.getItem("dark-mode");
// 
// const enableDarkMode = () => {
//   theme.classList.add("dark-mode-theme");
//   toggleBtn.classList.remove("dark-mode-toggle");
//   localStorage.setItem("dark-mode", "enabled");
// };
// 
// const disableDarkMode = () => {
//   theme.classList.remove("dark-mode-theme");
//   toggleBtn.classList.add("dark-mode-toggle");
//   localStorage.setItem("dark-mode", "disabled");
// };
// 
// if (darkMode === "enabled") {
//   enableDarkMode(); // set state of darkMode on page load
// }
// 
// toggleBtn.addEventListener("click", (e) => {
//   darkMode = localStorage.getItem("dark-mode"); // update darkMode when clicked
//   if (darkMode === "disabled") {
    // enableDarkMode();
//   } else {
    // disableDarkMode();
//   }
// });
// ------------

function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}


function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}


function checkCookies() {
    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
}


function mOver(obj) {
   obj.innerHTML = "<br> HELLO"
}

function mOut(obj) {
    obj.innerHTML = ""
}


function sendAlert() {
    alert(location.hostname);
}

