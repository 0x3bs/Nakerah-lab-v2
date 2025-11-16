# Nakerah-lab-v2

Nakerah-lab-v2 Will make You able to install all this labs by one click , without any problems in inshallah.
This project is trying to help the community to install their own lab .

This is how it looks:

![alt text](https://github.com/0x3bs/Nakerah-lab-v2/blob/main/imgs/image-10.png "Pic 1")

Now this is what is Nakerah-lab V2 include .

1. bWAPP
2. xvwa
3. dvwa
4. mutillidae
5. hackademic
6. sqli-labs
7. rapid7 hackazon
8. WebGoat
9. owasp juice shop
10. WackoPicko
11. Damn Vulnerable NodeJS Application



or: 
And this After install :

![alt text](https://github.com/0x3bs/Nakerah-lab-v2/blob/main/imgs/image-12.png "Pic 1")

## Installation

the ip u can get it from : ifconfig
or:
You can download Ubuntu server 2018 64 and it's the best one :

[Download Ubuntu Server 64](https://old-releases.ubuntu.com/releases/18.04.5/ubuntu-18.04.5-live-server-amd64.iso)

Please note that PHP version 8.4 is require .

### the mysql credentials must be :
```
user:root
pass:root123
------------------------------------
```

if you don't remember mysql credentials run :
step by step

```
sudo systemctl stop mariadb

sudo mysqld_safe --skip-grant-tables --skip-networking &

mysql -u root

FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
FLUSH PRIVILEGES;
EXIT;

```


------------------------------
Run :

```
sudo apt-get install git

sudo git clone https://github.com/0x3bs/Nakerah-lab-v2.git

cd Nakerah-lab-v2

sudo chmod +x setup.sh

sudo ./setup.sh


```
to check you dockers after run :

```
sudo dockers ps
```

------------------------------

to open any labs from another device : 

you must know the IP for the device which has the labs and then :

to open index.html :
```
http://{ip}
```

to open bWAPP :
```
to install : http://{ip}:8000/install.php
http://{ip}:8000
```
to open dvwa :
```
http://{ip}:1111
```

to open sqli_labs
```
http://{ip}:8001
```

to open hackazon :
```
http://{ip}:8002
```

to open webgoat :
```
http://{ip}:8080/WebGoat
```

to open webwolf :
```
http://{ip}:9091/WebWolf
```
to open juicw_shop :
```
http://{ip}:3000
```

to open wackopicko :
```
http://{ip}:8004
```
to open dvna :
```
http://{ip}:9090
```
-------------------------------
The login details

for xvwa :
```php
admin:admin
xvwa:xvwa
user:vulnerable
```
for Mutillidae :
```php
admin:admin
pass:adminpass
```
for bWAPP :
```php
admin:bee
pass:bug
```
for dvwa :
```php
admin:admin
pass:password
```




############################
## Contact    Twitter     ##
limbo0x01 > [limbo0x01](https://twitter.com/limbo0x01)

0x3bs > [0X3bs](https://twitter.com/3bs_303)
