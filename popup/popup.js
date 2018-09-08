chrome.runtime.sendMessage({task: "checkState"}, function(response) {
    if (response.handle == null)
        displayLogin(true);
    else
        displayLogout(true, response.handle);
});

document.getElementById('login').addEventListener('submit', changeHandle);
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

function changeHandle() {
    var handle = document.getElementById('handle').value;
    alert(handle);
    /*
    $.ajax({
        type: "POST",
        url: "../server/cf_api.py",
        data: {param: handle}
    }).done(function(o) {
        alert(o);
        if (!o.isValidUser(handle))
            return;
    });
    alert("hi");
    */

    
    /*
    $.ajax({
        type:'get',
        url:'/URLToTriggerGetRequestHandler',
        cache:false,
        async:'asynchronous',
        dataType:'json',
        success: function(data) {
            console.log(JSON.stringify(data))
        },
        error: function(request, status, error) {
            console.log("Error: " + error)
        }
    });
    */
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