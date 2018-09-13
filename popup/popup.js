/*
 * This file is part of Codeforces Companion (Coco),
 * Copyright (C) 2018-present Aditya Arjun, Richard Guo, An Nguyen, Elizabeth Zou
 */

var server_url = "http://127.0.0.1:5000/";

chrome.runtime.sendMessage({task: "checkState"}, function(response) {
    displayProblemSuggestion(response.number, response.letter);
    if (response.handle == null)
        displayLogin(true);
    else
        displayLogout(true, response.handle);
});

$('#openProblem')[0].addEventListener('click', openSuggestedProblem);
$('#selectCategory')[0].addEventListener('submit', selectCategory);
$('#login')[0].addEventListener('submit', tryToChangeHandle);
$('#logout')[0].addEventListener('click', logout);

function displayProblemSuggestion(number, letter) {
    if (number == null)
        document.getElementById("suggested").innerHTML = "Suggested Problem: N/A";
    else
        document.getElementById("suggested").innerHTML = "Suggested Problem: " + number + letter;
}

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
<<<<<<< HEAD
    var heh = $.getJSON('http://server-20-annguyencompsci.c9users.io:8080/checkHandle?handle=' + handle, null,
    function(data) {
        alert(JSON.stringify(data))
        if (data.yay)
            changeHandle(handle);
        else
            alert("Invalid Handle!");
    }).fail(() => {alert("fail")});
=======
    $.ajax({
        dataType: "json",
        url: server_url + 'checkHandle?handle=' + handle,
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
>>>>>>> 13821c26932f1678af8cd706f376d94d3fe2a619
}

function changeHandle(handle) {
    chrome.runtime.sendMessage({task: "changeHandle", handle: handle}, function(response) {
        displayLogin(false);
        displayLogout(true, handle);
    });
}

function selectCategory() {
    if (document.getElementById("login").style.display == "block") {
        alert("Please login first.");
        return;
    }
    var e = document.getElementById("categoriesDropdown");
    var tag = e.options[e.selectedIndex].value;
    if (tag == "")
        alert("Please select a category.");
    else {
        chrome.runtime.sendMessage({task: "checkState"}, function(response) {
            $.ajax({
                dataType: "json",
                url: server_url + 'suggest?handle=' + response.handle + '&tag=' + tag,
                data: null,
                async: false,
                success: function(data) {
                    chrome.runtime.sendMessage({task: "changeSuggestedProblem", number: data.number, letter: data.letter}, function(response) {});
                }
            });
        });
    }
}

function logout() {
    chrome.runtime.sendMessage({task: "logout"}, function(response) {
        displayLogin(true);
        displayLogout(false, null);
    });
}

function openSuggestedProblem() {
    chrome.runtime.sendMessage({task: "getSuggestedProblem"}, function(response) {
        if (response.URL == null)
            alert("Please select a category to suggest a problem in first!");
        else {
            var win = window.open(response.URL, '_blank');
            win.focus();
        }
    });
}