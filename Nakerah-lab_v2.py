#!/usr/bin/python3
import os
import sys
import time
import subprocess
import socket

f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
PHP_V=sys.argv[1]

os.system("sudo apt update")
print("Step 1: Install apache")
os.system("sudo apt-get install unzip") # ..
print("[+] Install the apache2 package:")
os.system("sudo apt-get install apache2 -y")
print("[+] Enable its rewrite module, and restart the service :")
os.system("sudo a2enmod rewrite && systemctl restart apache2")
print("[+] Step 2 - Adjusting the Firewall ")
os.system("sudo apt install ufw")
os.system("sudo ufw app list")
os.system("sudo ufw allow 'Apache'")
os.system("sudo ufw status")
#-----------------------------------------------------------# >>>>>>>
print("-------------------------------------------------------")
print("[+] Step 3 - Checking your Web Server")
os.system("sudo systemctl status apache2 --no-pager")
print("[+] Step 4 - Setting Up Virtual Hosts (Recommended)")
print("[+] Assign ownership of the directory:")
os.system("sudo chown -R $USER:$USER /var/www/")
print("[+] The permissions of your web")
os.system("sudo chmod -R 755 /var/www/")
print("[+] Disable the default site defined in 000-default.conf:")
os.system("sudo a2dissite 000-default.conf")
print("[+] Test for configuration errors: ")
os.system("sudo apache2ctl configtest ")
print("[+] Restart Apache to implement your changes:")
os.system("sudo systemctl reload apache2 ")
#-----------------------------------------------------------# >>>
print("-------------------------------------------------------")


print("Step 5: Install MariaDB instead of MySQL")
os.system("sudo apt-get update -y")
os.system("sudo apt-get install -y mariadb-server php-mysql")

print("-------------------------------------------------------")
print("This step is for Kali Linux")


os.system("sudo ls -lart /var/run/my")
os.system("sudo mkdir -p /var/run/mysqld")


os.system("sudo chown -R mysql:mysql /var/run/mysqld")


os.system("sudo systemctl enable --now mariadb")

print("-------------------------------------------------------")
print("Check MariaDB service status")
os.system("sudo systemctl status mariadb --no-pager -n 20")

print("-------------------------------------------------------")
print("Reminder: Run secure setup")
print("sudo mysql_secure_installation")# ---
# >>>>>>>>>>>>>>>>>>>>>>>>

print("Step 6: Install php")
# for dvwa
os.system("sudo apt-get install php 8.4-curl php 8.4-mbstring php 8.4-xml -y")
os.system("sudo apt-get install php7.3-curl php7.3-mbstring php7.3-xml -y")
os.system("sudo apt-get install php php-mysqli php-gd libapache2-mod-php -y")
# >>>>>>
print("-------------------------------------------------------")
print("Step 7: Install python")

os.system("sudo apt-get update -y")

os.system("sudo apt-get install python3 -y")
os.system("sudo apt-get install python3-pip -y")

os.system("sudo apt-get install python3-mysqldb -y")

os.system("pip3 install mysql-connector-python --break-system-packages")
os.system("pip3 install pymysql --break-system-packages")
os.system("pip3 install mariadb --break-system-packages")

os.system("sudo apt install libmariadb3 libmariadb-dev -y")


os.system("sudo apt install mariadb-server -y")
os.system("sudo systemctl enable mariadb")
os.system("sudo systemctl start mariadb")

print("[+] Installing Python3 dev tools...")
os.system("sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y")

print("[+] Upgrading pip and verifying MySQL connectors...")
venv_name = "my_project_venv"
venv_pip_path = f"./{venv_name}/bin/pip" 
subprocess.run(["python3", "-m", "venv", venv_name])
time.sleep(1)

subprocess.run([venv_pip_path, "install", "--upgrade", "pip"], check=True)

os.system("sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip2.py")
os.system("sudo apt install python3-pip")

# >>>>>>>>>>>


print("[+] Installing Python3 and essential build tools...")
os.system("sudo apt-get update -y")
os.system("sudo apt-get install python3 python3-pip python3-dev default-libmysqlclient-dev build-essential -y")

print("[+] Upgrading pip and installing Python MySQL connectors...")
venv_name = "my_project_venv"
venv_pip_path = f"./{venv_name}/bin/pip" 
subprocess.run(["python3", "-m", "venv", venv_name])
time.sleep(1)

subprocess.run([venv_pip_path, "install", "--upgrade", "pip"], check=True)

os.system("pip3 install mysql-connector-python pymysql mariadb --break-system-packages")

os.system("sudo apt-get install python3-mysqldb ")
os.system("pip3 install mysql-connector-python --break-system-packages")
os.system("pip3 install pymysql --break-system-packages")

os.system("sudo apt install libmariadb3 libmariadb-dev -y")
os.system("sudo apt install mariadb-server -y")
os.system("sudo service mariadb start")
os.system("pip3 install mariadb --break-system-packages")
###########mutillidae  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >?>?>?>?>?>?>?>>?>?>?

os.system("sudo apt update -y")
os.system("sudo apt install php8.4-xml php8.4-fpm libapache2-mod-php php8.4-mysql php8.4-gd  php8.4-mysql php8.4-curl php8.4-mbstring -y")
os.system("sudo apt-get install php*-mbstring php*-mcrypt -y")
os.system("sudo apache2ctl graceful")
os.system("sudo apt install composer")
os.system("composer require webklex/php-imap")
os.system("sudo a2enmod proxy_fcgi setenvif")
os.system("sudo systemctl restart apache2")
os.system("sudo a2enconf php8.4-fpm")
os.system("sudo systemctl reload apache2")
os.system("sudo systemctl restart apache2.service")
os.system("sudo service php8.4-fpm restart")
os.system("sudo systemctl restart mysql")
######################
# ?>?>?>?>?>?>?>?>>?>?>
os.system("sudo apt-get install python-mysqldb --break-system-packages")
os.system("pip3 install mysql-connector-python --break-system-packages ")
os.system("pip3 install pymysql --break-system-packages")
os.system("pip3 install mysql-connector-python --break-system-packages")
os.system("sudo apt install python3-dev libpython3-dev")
os.system("sudo apt install python3-mysqldb")
os.system("sudo apt install libmariadb-dev")
os.system("sudo -H pip3 install mysqlclient --break-system-packages")
os.system("sudo apt-get install python3-dev libmariadb-dev -y")


os.system("pip3 install mysqlclient --break-system-packages")

print("-------------------------------------------------------")

# allow url include for dvwa
# Read in the file
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('allow_url_include = Off', 'allow_url_include = On')

# Write the file out again
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'w') as file:
    file.write(filedata)
time.sleep(0.5)
print("--------------------------------------------------------")
# allow url include for dvwa
# Read in the file
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('display_errors = Off', 'display_errors = On')

# Write the file out again
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'w') as file:
    file.write(filedata)
time.sleep(0.5)

print("Restart Apache2...")
os.system("sudo service apache2 restart")
print("-------------------------------------------------------")

print("[+] Now working with the files ")
# unzip files
os.system("sudo unzip file.zip")
time.sleep(0.5)
os.system("sudo unzip hackademic.zip")
time.sleep(0.5)
#os.system("sudo rm -r mutillidae2.zip")
#os.system("sudo rm -r mutillidae")

#os.system("sudo git clone https://github.com/webpwnized/mutillidae")
time.sleep(0.5)
os.system("sudo tar -xzvf xvwa.tar.gz")


os.system("sudo rm -r *.zip  *.gz")
time.sleep(0.5)
print("[+] Create a sample index.html")


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

time.sleep(0.5)
os.system("sudo mv index.html /var/www/html/index.html")
time.sleep(0.5)

os.system("sudo chmod +x ip_index.py ")
os.system("sudo cp ip_index.py /var/www/html ")
os.system('sudo ( crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /root/myscript.py" ) | crontab -')

time.sleep(3)

os.system("sudo mv 873.jpg 0386.jpg  c-logo-hd.png  /var/www/html")


os.system("sudo systemctl stop mariadb")
os.system("sudo mysqld_safe --skip-grant-tables --skip-networking &")
time.sleep(7)
with open("/tmp/reset.sql", "w") as f:
    f.write("FLUSH PRIVILEGES;\n")
    f.write("ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';\n")
    f.write("FLUSH PRIVILEGES;\n")
    f.write("EXIT;\n")

os.system("sudo mysql -u root < /tmp/reset.sql")


try:
    print("Step 9: Create MariaDB databases ")
    import mariadb
    time.sleep(0.5)
    conn = mariadb.connect(
        user="root",
        password = "root123",
        host="localhost",
        port=3306,
        database="mysql"

    )

    print("Creating databases....")
    cursor = conn.cursor()
    print("Step 9.1: Creating dvwa database ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  dvwa;")
    cursor.execute("CREATE USER IF NOT EXISTS 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
    cursor.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("dvwa fninshed")
    
    # data xvwa;
    print("Step 9.2: Creating xvwa database ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  xvwa;")
    cursor.execute("CREATE USER IF NOT EXISTS 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("SQL fninshed")
    # data bWAPP;
    print("Step 9.3: Creating bWAPP database ")
    cursor.execute("CREATE USER IF NOT EXISTS 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    # data sql;
    print("Step 9.4: Creating secursority and challenges databases ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  secursority;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  challenges;")
    cursor.execute("CREATE USER IF NOT EXISTS 'sql'@'localhost' IDENTIFIED BY 'sql';")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'sql'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'sql'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("9.4 secursority & challenges fninshed")
    # data mutillidae;
    #print("Step 9.5: Creating mutillidae  database")
    #cursor.execute("CREATE DATABASE IF NOT EXISTS mutillidae;")
    #cursor.execute("CREATE USER IF NOT EXISTS 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
    #cursor.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
    #cursor.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
    #cursor.execute("use mysql;")
    #cursor.execute("flush privileges;")
    #print("mutillidae part 1")
    time.sleep(0.5)
    #cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY 'mutillidae';")
    #cursor.execute("SET PASSWORD FOR 'root'@'localhost' = PASSWORD('mutillidae');")
    #cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("mutillidae part 2")

    print("Every thing is going well...")
    conn.close()

except:
    import MySQLdb
    print("Step 10: Create mysql databases ")

    hostname = 'localhost',
    username = 'root',
    password = "root123", 
    database = 'mysql'


    # Simple routine to run a query on a database and print the results:
    def doQuery(conn):
        cur = conn.cursor()
        # data dvwa;
        print("Step 9.1: Creating DVWA database ")
        cur.execute("CREATE DATABASE IF NOT EXISTS dvwa;")
        cur.execute("CREATE USER IF NOT EXISTS 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
        cur.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data sql;
        print("Step 9.2: Creating XVWA database ")
        cur.execute("CREATE DATABASE IF NOT EXISTS xvwa;")
        cur.execute("CREATE USER IF NOT EXISTS 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
        cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data bWAPP;
        print("Step 9.3: Creating BWAPP database ")
        cur.execute("CREATE USER IF NOT EXISTS 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
        cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data sql;
        print("Step 9.4: Creating security and challenges databases ")
        cur.execute("CREATE DATABASE IF NOT EXISTS security;")
        cur.execute("CREATE DATABASE IF NOT EXISTS challenges;")
        cur.execute("CREATE USER IF NOT EXISTS 'sql'@'localhost' IDENTIFIED BY 'sql';")
        cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'sql'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'sql'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data mutillidae;
        #print("Step 9.5: Creating mutillidae database ")
        #cur.execute("CREATE DATABASE IF NOT EXISTS mutillidae;")
        #cur.execute("CREATE USER IF NOT EXISTS 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
        #cur.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
        #cur.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
        #cur.execute("use mysql;")
        #cur.execute("flush privileges;")
        #print("mutillidae part 1")
        time.sleep(0.5)
        
        #cur.execute("update user set authentication_string=PASSWORD('mutillidae') where user='mutillidae';")
        #cur.execute("update user set plugin='mysql_native_password' where user='mutillidae';")
        #cur.execute("flush privileges;")
        #time.sleep(0.5)

        print("mutillidae part 2")
        for firstname, lastname in cur.fetchall():
            print(firstname, lastname)
    print("Using MySQLdb ... ")
    myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
    doQuery(myConnection)
    myConnection.close()
    print("Creating databases done ...... ")


os.system("clear")
f = open('banner.txt', 'r')
file_contents = f.read()
print("file_contents")
f.close()
def op_list():
    print("Chose any number to install what you want ")
    print("\033[1;30;40m [+] Enter (1) To install { bWAPP      }")
    print("\033[1;31;40m [+] Enter (2) To install { xvwa       }")
    print("\033[1;32;40m [+] Enter (3) To install { dvwa       }")
    print("\033[1;33;40m [+] Enter (4) To install { mutillidae }")
    print("\033[1;34;40m [+] Enter (5) To install { hackademic }")
    print("\033[1;35;40m [+] Enter (6) To install { sqli-labs  }")
    print("\033[1;36;40m [+] Enter (7) To install { Rapid7 Hackazon  }")
    print("\033[1;37;40m [+] Enter (8) To install { WebGoat  }")
    print("\033[1;38;40m [+] Enter (9) To install { OWASP Juice Shopp  }")
    print("\033[1;39;40m [+] Enter (10) To install { WackoPicko  }")
    print("\033[1;40;40m [+] Enter (11) To install { Damn Vulnerable NodeJS Application }")
    print("\033[1;41;40m [+] Enter (12) To install { ALL        }")
    print("\033[0;31;40m [+] Enter (13) Or anything To  { Exit  }")

print("\033[1;36;40m Welcome :) This is Nakerah-lab v2 ")
x = 1
op_list()
while x != 0:
    if x <= 12:
        try:
            x = int(input("Enter Your Order :"))
            if x == 1:
                print("Wait for install { bWAPP      }")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull raesene/bwapp")
                os.system("sudo docker run -d -p 8000:80 --name bwapp --restart=always raesene/bwapp")
                os.system("sudo docker ps")
                time.sleep(3)
                op_list()
            elif x == 2:
                print("Wait for install { xvwa       }")
                os.system("sudo cp -r xvwa /var/www/html/")
                time.sleep(3)
                op_list()
            elif x == 3:
                print("Wait for install { dvwa       }")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull vulnerables/web-dvwa")
                os.system("docker run -d -p 1111:80 --name dvwa --restart=always vulnerables/web-dvwa")
                os.system("sudo docker ps")
                time.sleep(3)
                op_list()
            elif x == 4:
                print("Wait for install { mutillidae }")
                os.system("sudo apt install docker.io -y")
                os.system("sudodocker pull bltsec/mutillidae-docker")
                os.system("sudodocker run -d -p 8009:80 -p 443:443 --name mutillidae --restart=always bltsec/mutillidae-docker")
                os.system("sudo docker exec -d mutillidae /opt/lampp/lampp start")

                time.sleep(3)
                op_list()
            elif x == 5:
                print("Wait for install { hackademic }")
                os.system("sudo cp -r hackademic /var/www/html/")
                time.sleep(3)
                op_list()
            elif x == 6:
                print("Wait for install { sqli-labs  }")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull acgpiano/sqli-labs")
                os.system("sudo docker run -dt -p 8001:80 --name sqli-labs --restart=always acgpiano/sqli-labs:latest")
                os.system("sudo docker ps")
                time.sleep(3)
                op_list()

            elif x == 7:

                print("Wait for install { hackazon  }")
                os.system("sudo pip3 install docker --break-system-packages")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull santosomar/hackazon")
                os.system("sudo docker run --name hackazon -d -p 8002:80 --restart=always santosomar/hackazon:latest supervisord -n")
                os.system("sudo docker ps")
                import docker

                CONTAINER_NAME = "hackazon"

                WORKDIR = "/var/www/hackazon/modules/vulninjection/classes/VulnModule/Vulnerability/"

                def run_command(command):

                    try:

                        client = docker.from_env()

                        container = client.containers.get(CONTAINER_NAME)
                        
                        exit_code, output = container.exec_run(
                            cmd=command, 
                            workdir=WORKDIR,
                            user='root'  
                        )
                        
                        print(f"--- Command: {' '.join(command)} ---")
                        if exit_code == 0:
                            print(output.decode('utf-8'))
                        else:
                            print(f"Error (Exit Code: {exit_code}):")
                            print(output.decode('utf-8'))
                        print("-" * 30)

                    except docker.errors.NotFound:
                        print(f"Error: Container '{CONTAINER_NAME}' not found. Is it running?")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")


                if __name__ == "__main__":

                    run_command(['ls', '-la'])

                    run_command(['cat', 'Referer.php'])
                    

                    sed_command = [
                        'sed', 
                        '-i', 
                        's/throw new HttpException("Invalid referer", 400);/\/\/ throw new HttpException("Invalid referer", 400);/', 
                        'Referer.php'
                    ]
                    run_command(sed_command)
                    # ////////////////////////////////////////////////

            elif x == 8:

                print("Wait for install {web goat  }")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull webgoat/webgoat")
                os.system("docker run -it -d -p 127.0.0.1:8080:8080 -p 127.0.0.1:9091:9090 --name web_goat --restart=always webgoat/webgoat")
                time.sleep(4)
                os.system("sudo docker ps")
                op_list()
                

            elif x == 9:

                print("Wait for install {juice-shop  }")
            
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull bkimminich/juice-shop")
                os.system("sudo docker run  -d -p 3000:3000 --name juice_shop --restart=always bkimminich/juice-shop:latest ")
                os.system("sudo docker ps")
                time.sleep(3)
                op_list()

            elif x == 10:

                print("Wait for install {WackoPicko  }")
                os.system("sudo apt install docker.io  -y")

                os.system("sudo docker pull adamdoupe/wackopicko")
                os.system("sudo docker run -d -p 8004:80 --name wackopicko --restart=always adamdoupe/wackopicko:latest ")
                os.system("sudo docker ps")
                time.sleep(3)

            elif x == 11:

                print("Wait for install {Damn Vulnerable NodeJS Application  }")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull appsecco/dvna")
                os.system("docker run --name dvna -p 9090:9090 -d --restart=always appsecco/dvna:sqlite")

                os.system("sudo docker ps")
                time.sleep(3)
                op_list()

            elif x == 12:
                print("Wait for install { All        }")
                os.system("sudo apt install docker.io  -y")
                os.system("sudo docker pull raesene/bwapp")
                os.system("sudo docker run -d -p 8000:80 --name bwapp --restart=always raesene/bwapp")
                os.system("sudo docker ps")
                time.sleep(3)
                os.system("sudo cp -r xvwa /var/www/html/")
                os.system("sudo docker pull vulnerables/web-dvwa")
                os.system("docker run -d -p 1111:80 --name dvwa --restart=always vulnerables/web-dvwa")
                os.system("sudo docker ps")
                time.sleep(3)
                os.system("docker pull bltsec/mutillidae-docker")
                os.system("docker run -d -p 8009:80 -p 443:443 --name mutillidae --restart=always bltsec/mutillidae-docker")
                time.sleep(2)
                os.system("sudo docker exec -d mutillidae /opt/lampp/lampp start")
                time.sleep(5)
                os.system("sudo cp -r hackademic /var/www/html/")
                os.system("sudo docker pull acgpiano/sqli-labs")
                os.system("sudo docker run -dt -p 8001:80 --name sqli-labs --restart=always acgpiano/sqli-labs:latest")
                os.system("sudo docker ps")
                time.sleep(3)
                os.system("sudo pip3 install docker --break-system-packages")
                os.system("sudo docker pull santosomar/hackazon")
                os.system("sudo docker run --name hackazon -d -p 8002:80 --restart=always santosomar/hackazon:latest supervisord -n")
                os.system("sudo docker ps")
                import docker

                CONTAINER_NAME = "hackazon"

                WORKDIR = "/var/www/hackazon/modules/vulninjection/classes/VulnModule/Vulnerability/"

                def run_command(command):

                    try:

                        client = docker.from_env()

                        container = client.containers.get(CONTAINER_NAME)
                        
                        exit_code, output = container.exec_run(
                            cmd=command, 
                            workdir=WORKDIR,
                            user='root'  
                        )
                        
                        print(f"--- Command: {' '.join(command)} ---")
                        if exit_code == 0:
                            print(output.decode('utf-8'))
                        else:
                            print(f"Error (Exit Code: {exit_code}):")
                            print(output.decode('utf-8'))
                        print("-" * 30)

                    except docker.errors.NotFound:
                        print(f"Error: Container '{CONTAINER_NAME}' not found. Is it running?")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")


                if __name__ == "__main__":

                    run_command(['ls', '-la'])

                    run_command(['cat', 'Referer.php'])
                    

                    sed_command = [
                        'sed', 
                        '-i', 
                        's/throw new HttpException("Invalid referer", 400);/\/\/ throw new HttpException("Invalid referer", 400);/', 
                        'Referer.php'
                    ]
                    run_command(sed_command)
                time.sleep(3)
                os.system("sudo docker pull webgoat/webgoatf")
                os.system("sudo docker run -it -d -p 127.0.0.1:8080:8080 -p 127.0.0.1:9091:9090 --name web_goat --restart=always webgoat/webgoat")
                os.system("sudo docker ps")
                time.sleep(3)
                os.system("sudo docker pull bkimminich/juice-shop")
                os.system("sudo docker run  -d -p 3000:3000 --name juice_shop --restart=always bkimminich/juice-shop:latest ")
                os.system("sudo docker ps")
                time.sleep(3)
                os.system("sudo docker pull adamdoupe/wackopicko")
                os.system("sudo docker run -d -p 8004:80 --name wackopicko --restart=always adamdoupe/wackopicko:latest ")
                os.system("sudo docker ps")
                time.sleep(3)
                os.system("sudo docker pull appsecco/dvna")
                os.system("docker run --name dvna -p 9090:9090 -d --restart=always appsecco/dvna:sqlite")
                os.system("sudo docker ps")

                op_list()
        except:
            print(" You can't see the numbers ? enter something exist  ")
    else:
        break
print(" Goodbye Friend !!")
os.system("sudo service apache2 restart")
os.system("clear")
print("\033[0;32;40m ")
f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()

print("--------------------------------------------------------------")
print("Hello Friend ... ")
print("Now u can using yor lab ... ")
print("Just Open your Browser IP Machine = >>  : ")
os.system("IP=$(ifconfig|grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")


