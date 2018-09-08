chrome.runtime.sendMessage({task: "checkState"}, function(response) {
    if (response.handle == null)
        displayLogin(true);
    else
        displayLogout(true, response.handle);
});

// document.getElementById('login').addEventListener('click', openOptions);

document.getElementById('login').addEventListener('submit', changeHandle);

function displayLogin(on) {
    if (on)
        document.getElementById("login").style.display = "block";
    else
        document.getElementById("login").style.display = "none";
}

function displayLogout(on, handle) {
    if (on) {
        document.getElementById("logoutDisplay").style.display = "block";
        document.getElementById("handleDisplay").innerHTML = "Handle: " + handle;
    }
    else
        document.getElementById("logoutDisplay").style.display = "none";
}

function changeHandle() {
    var handle = document.getElementById('handle').value;
    //document.getElementById('wurl').value = "";
    chrome.runtime.sendMessage({task: "changeHandle", handle: handle}, function(response) {
        displayLogin(false);
        displayLogout(true, handle);
    });
}

function openOptions() {
    var win = window.open("../options/options.html", '_blank');
    win.focus();
}