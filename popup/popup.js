chrome.runtime.sendMessage({task: "checkState"}, function(response) {
    if (response.handle == null)
        displayLogin(true);
    else
        displayLogout(true, response.handle);
});

document.getElementById('login').addEventListener('submit', tryToChangeHandle);
document.getElementById('logout').addEventListener('click', logout);

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

function tryToChangeHandle() {
    var handle = document.getElementById('handle').value;
    $.ajax({
        dataType: "json",
        url: 'http://127.0.0.1:5000/checkHandle?handle=' + handle,
        data: null,
        async: false,
        success: function(data) {
            if (data.valid)
                changeHandle(handle);
            else
                alert("Invalid Handle!");
        }
    });

    //fetch('http://127.0.0.1:5000/checkHandle?handle=' + handle).then(fcn).catch((err) => {alert(JSON.stringify(error))});
    /*
    fetch('http://127.0.0.1:5000/checkHandle?handle=' + handle).then(
        function(response){
            return response.json();
        }
    ).then(fcn);
    */
    //$.getJSON('http://127.0.0.1:5000/checkHandle?handle=' + handle, null, fcn);
}

function changeHandle(handle) {
    chrome.runtime.sendMessage({task: "changeHandle", handle: handle}, function(response) {
        displayLogin(false);
        displayLogout(true, handle);
    });
}

function logout() {
    chrome.runtime.sendMessage({task: "logout"}, function(response) {
        displayLogin(true);
        displayLogout(false, null);
    });
}

function openOptions() {
    var win = window.open("../options/options.html", '_blank');
    win.focus();
}