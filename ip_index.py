import socket
import os

hostname= socket.gethostname()
localip = socket.gethostbyname(hostname)

html ='''
<HTML>
<head>
	<meta charset="utf-8">
<style>
    #link { color:  #27ae60; } /* CSS link color */
  </style>
	<link rel="icon" type="image/png" href="c-logo-hd.png" sizes="16x16">
<TITLE> Nakerah Lab </title>
</head>
<style>


	body {
	  align-items: center;
	  background: #111;
	  background: radial-gradient(#1a1a1a, black);
	  display: flex;
	  flex-direction: column;
	  justify-content: center;

	}


	.lock {
	  background: #000;
	  border-bottom: 1px solid #262626;
	  border-left: 1px solid #262626;
	  box-shadow: -1px 1px 0 #0f0f0f, -2px 2px 0 #0d0d0d, -3px 3px 0 #0a0a0a, -4px 4px 0 #080808, -8px 8px 16px rgba(0, 0, 0, 0.5);
	  position: relative;
	  z-index: 20;

	}

	.screen {
	  background: #000;
	  height: 40px;
	  position: relative;

	}
.screen2 {
	  background: #000;
	  height: 40px;
	  width: 40px;
	  position: relative;

	}
	.code,
	.status {
	  font-family: 'Share Tech Mono', monospace;
	  font-size: 1em;
	  height: 40px;
	  line-height: 42px;
	  padding: 0 0.75em;
	  text-align: center;
	}
	.code {
	  color: #fff;
	  left: 0;
	  text-shadow: 0 0 15px #fff;
	}
	.status2 {
	  -webkit-animation: pulse 1000ms infinite alternate;
			  animation: pulse 1000ms infinite alternate;
	  color: #f00;
	  text-shadow: 0 0 15px #f00;
	}
	.status {
	  -webkit-animation: pulse 1000ms infinite alternate;
			  animation: pulse 1000ms infinite alternate;
	  color: #00FF00;
	  text-shadow: 0 0 15px #00FF00;
	}

@-webkit-keyframes pulse {
	  0%,
	  0% {
		opacity: 0.25;
	  }
	  100% {
		opacity: 1;
	  }
	}
	@keyframes pulse {
	  0%,
	  0% {
		opacity: 0.25;
	  }
	  100% {
		opacity: 1;
	  }
	}

	.scanlines {
	  background: linear-gradient(rgba(255, 255, 255, 0.04) 50%, rgba(0, 0, 0, 0.1) 50%);
	  background-size: 100% 2px;
	  bottom: 1px;
	  left: 0;
	  pointer-events: none;
	  position: absolute;
	  right: 1px;
	  top: 1px;
	  z-index: 1;
	}

  </style>

 <body style="color: white; background-color: #202020;" alink="white" link="white" vlink="white">
<div><a href="https://www.nakerah.net/index.php">
				<span></span>
				<center><img style="width: 350px; height: 200px;" alt="Nakerah-lab" src="c-logo-hd.png"></center>
			</a></div>
<h2>
<hr>
<div class="lock">
  <div class="screen">
    <div class="status">Available Now v2  </div>
    <div class="scanlines"></div>
<hr>
  </div>

<h4>
<ol>.
<a id =link HREF='http://'''+localip+''':8000/install.php'> To install bWAPP</a>
<li><a id=link HREF='http://'''+localip+''':8000'>bWAPP</a>
<li><a id=link HREF='http://'''+localip+''':1111'>Damn Vulnerable Web Application</a>
<li><a id=link HREF='/hackademic'>OWASP Hackademic</a>
<li><a id=link HREF='/xvwa'>Extreme Vulnerable Node Application</a>
<li><a id=link HREF='http://'''+localip+''':8009/mutillidae'>OWASP Mutillidae II new version  </a>
<li><a id=link HREF='http://'''+localip+''':8001/'>Sql lab  </a>
<li><a id=link HREF='http://'''+localip+''':8002/'>Rapid7 Hacksazon  </a>
<li><a id=link HREF='http://'''+localip+''':8080/WebGoat'>WebGoat  </a>
<li><a id=link HREF='http://'''+localip+''':9091/WebWolf'>WebWolf  </a>
<li><a id=link HREF='http://'''+localip+''':3000/'>OWASP Juice Shop  </a>
<li><a id=link HREF='http://'''+localip+''':8004/'>WackoPicko  </a>
<li><a id=link HREF='http://'''+localip+''':9090/'>Damn Vulnerable NodeJS Application </a>
</div>
        <hr>
<div class="lock">

<hr>
<center><font color="red">إذكر الله </font></center>
<hr>

<div>
  <a href="https://www.Twitter.com/limbo0x01"> <font color=#504060> Contact Twitter : @limbo0x01 </font></a>
</div>
<div>
  <a href="https://www.Twitter.com/3bs_303"> <font color=#504060> Contact Twitter : @3bs_303 </font></a>
</div>

 <div align="border-left">
		<a href="https://www.nakerah.net/index.php?members/limbo.873/"><img src="873.jpg" alt="Limbo" width="66" height="66"></a>
		<a href="https://nakerah.net/community/members/abbasy-beso.5684/"><img src="0386.jpg" alt="beso" width="66" height="100"></a>


</div>

</html>
'''

with open("index.html","w") as f:

    f.write(html)

os.system("sudo docker exec -d mutillidae /opt/lampp/lampp start")
