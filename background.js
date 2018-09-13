/*
 * This file is part of Codeforces Companion (Coco),
 * Copyright (C) 2018-present Aditya Arjun, Richard Guo, An Nguyen, Elizabeth Zou
 */

var handle = null;
var number = null;
var letter = null;
var suggestedProblemURL = null;

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.task == "checkState") {
            sendResponse({handle: handle, number: number, letter: letter});
        }
        else if (request.task == "changeHandle") {
            handle = request.handle;
        }
        else if (request.task == "logout") {
            handle = null;
            number = null;
            letter = null;
            suggestedProblemURL = null;
        }
        else if (request.task == "changeSuggestedProblem") {
            number = request.number;
            letter = request.letter;
            suggestedProblemURL = "http://codeforces.com/problemset/problem/" + number + "/" + letter;
        }
        else if (request.task == "getSuggestedProblem") {
            sendResponse({number: number, letter: letter, URL: suggestedProblemURL});
        }
    }
);