/*
 * This file is part of name <link>,
 * Copyright (C) 2018-present A. Arjun, R. Guo, A. Nguyen, E. Zou
 */

var handle = null;

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.task == "checkState") {
            sendResponse({handle: handle});
        }
        else if (request.task == "changeHandle") {
            handle = request.handle;
        }
        else if (request.task == "logout") {
            handle = null;
        }
    }
);