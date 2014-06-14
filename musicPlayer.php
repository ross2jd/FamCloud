<!DOCTYPE html>

<html>
<head>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function () {
            var windowHeight = $(window).height();
            var windowWidth = $(window).width();
            var paddingWidth = (windowWidth - 420)/2;
            // Don't let the padding width get to small.
            if (paddingWidth < 100) {
                paddingWidth = 100;
            }
            $('.topBarPadRight').css("width", paddingWidth);
            $('.topBarPadLeft').css("width", paddingWidth);
            
            // Set the size of the height for the left and right pane
            var paneHeight = windowHeight - 114;
            $('.leftPane').css("height", paneHeight);
            $('.rightPane').css("height", paneHeight);
            
        });
        
        // Have the window height and width re-calculated every time the window is resized.
        $(window).resize(function() {
            var windowHeight = $(window).height();
            var windowWidth = $(window).width();
            var paddingWidth = (windowWidth - 420)/2;
            if (paddingWidth < 100) {
                paddingWidth = 100;
            }
            $('.topBarPadRight').css("width", paddingWidth);
            $('.topBarPadLeft').css("width", paddingWidth);
            // Set the size of the height for the left and right pane
            var paneHeight = windowHeight - 114;
            $('.leftPane').css("height", paneHeight);
            $('.rightPane').css("height", paneHeight);
        });
    </script>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            height: 100%;
        }
        .topBar {
            width: 100%;
            height: 114px;
            float: left;
        }
        .jPlayerUI {
            width: 420px;
            height: 114px;
            background-color: #FFFF00;
            float: left;
        }
        .topBarPadLeft {
            background-color: #FF0000;
            float: left;
            height: 114px;
            width: 100px;
        }
        .topBarPadRight {
            background-color: #FF0000;
            float: left;
            height: 114px;
            width: 100px;
        }
        .leftPane {
            float: left;
            clear: left;
            width: 30%;
            margin-left: 0;
            margin-right: auto;
            margin-top: 0;
            background-color: #00FF00;
        }
        .rightPane {
            float: right;
            width: 70%;
            margin-left: auto;
            margin-right: 0;
            margin-top: 0;
            background-color: #0000FF;
        }
    </style>
</head>

<body>
    <!-- The following code is for the top bar of music player -->
    <div class="topBar">
        <div class="topBarPadLeft">
            <!-- We will put our image for the drop down box here -->
        </div>
        <div class="jPlayerUI">
            <!-- The jPlayer skin that we are currently using is 420px wide and 114px tall -->
        </div>
        <div class="topBarPadRight">
        </div>
    </div>
    
    <!-- The following code is for the left pane of the music player (list the artists) -->
    <div class="leftPane">
        
    </div>
    
    <!-- The following code is for the right pane of the music player (table of songs) -->
    <div class="rightPane">
        
    </div>
    
</body>
