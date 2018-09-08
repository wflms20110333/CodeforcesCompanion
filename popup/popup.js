document.getElementById('options').addEventListener('click', openOptions);

function openOptions() {
    var win = window.open("../options/options.html", '_blank');
    win.focus();
}