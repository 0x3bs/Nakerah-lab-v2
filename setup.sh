
#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fisudo apt-get install php8.4-curl php8.4-mbstring php8.4-xml -y
sudo apt-get install php8.4-curl php8.4-mbstring php8.4-xml -y
sudo apt-get install php php-mysqli php-gd libapache2-mod-php -y
sudo apt install hhvm -y
fi
export PHP_limbo=$(php --version | grep -i 'PHP'|cut -d ')' -f 1 | head -1 | cut -c 5-10|cut -d '.' -f 1,2)


source ~/.bashrc
echo $PHP_limbo

sudo python3 Nakerah-lab_v2.py $PHP_limbo
