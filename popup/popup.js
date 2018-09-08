chrome.runtime.sendMessage({task: "checkState"}, function(response) {
    if (response.handle == null)
        document.getElementById("login").style.display = "block";
    else
        document.getElementById("logout").style.display = "block";
});

// document.getElementById('login').addEventListener('click', openOptions);

function openOptions() {
    var win = window.open("../options/options.html", '_blank');
    win.focus();
}