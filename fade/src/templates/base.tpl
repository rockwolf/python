<!DOCTYPE html>
<html>
<head>
    <title>FADE - Flask Application For Data Entry</title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <link rel="stylesheet" type=text/css href="{{ url_for('static', filename='css/pure-min.css') }}" />
    <link rel="stylesheet" type=text/css href="{{ url_for('static', filename='css/custom_style.css') }}" />
    <link rel="icon" type="image/png" href="{{url_for('static', filename='img/favicon.png') }}" /-->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="generator" content="">
    <meta name="author" content="Andy Nagels">
    <meta name="copyright" content="&copy; 2015&ndash;eternity Andy Nagels">
</head>
<body>
    <!--div class="header">
        <h1 class="headerTitle">
            <a href="/"><img src="/img/biohazard.png" type="image/png" alt="fade" height="50px" width="50px"/></a><span class="headerSubtitle">...</span>&nbsp;<span class="small">You're logged in as <span class="green">{{ p_user }}</span></span>
        </h1>
    </div-->
    <div class="custom-menu-wrapper">
        <div class="pure-menu custom-menu custom-menu-top">
            <a href="#" class="pure-menu-heading custom-menu-brand">FADE</a>
            <a href="#" class="custom-menu-toggle" id="toggle"><s class="bar"></s><s class="bar"></s></a>
        </div>
        <div class="pure-menu pure-menu-horizontal pure-menu-scrollable custom-menu custom-menu-bottom custom-menu-tucked" id="tuckedMenu">
            <div class="custom-menu-screen"></div>
            <ul class="pure-menu-list">
                <li class="pure-menu-item"><a href="/home" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="/tradingjournal" class="pure-menu-link">TradingJournal</a></li>
                <li class="pure-menu-item"><a href="/account" class="pure-menu-link">Account</a></li>
                <li class="pure-menu-item"><a href="/commodity" class="pure-menu-link">Commodity</a></li>
                <li class="pure-menu-item"><a href="/leverage" class="pure-menu-link">Leverage</a></li>
                <li class="pure-menu-item"><a href="/test" class="pure-menu-link">Test</a></li>
            </ul>
        </div>
    </div>
    <script>
        (function (window, document) {
            document.getElementById('toggle').addEventListener('click', function (e) {
                document.getElementById('tuckedMenu').classList.toggle('custom-menu-tucked');
                document.getElementById('toggle').classList.toggle('x');
            });
        })(this, this.document);
    </script>
    <div id="main">
    {% block body %}{% endblock %}
    </div>
</body>
</html>
