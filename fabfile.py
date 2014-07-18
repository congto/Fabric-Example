__author__ = 'cherry'

from fabric.api import *
from fabric.operations import sudo

""" Provide all user and pass to automation ! """

mysql_pwd = raw_input('provide mysql database root password : ')
wp_db_name = raw_input('provide wordpress database name : ')
wp_user_name = raw_input('provide wordpress database user name : ')
wp_user_pwd = raw_input('provide wordpress database user password : ')


def deploy():
    updatesystem()
    install_server()
    config_mysql()
    install_wp()
    init_wp()
    showos()


def updatesystem():
    sudo('apt-get -y update')


def mysqlcommand():
        sudo("mysql -p%s -e 'DROP DATABASE IF EXISTS %s;'" % (mysql_pwd, wp_db_name))
        sudo("mysql -p%s -e 'CREATE DATABASE %s;'" % (mysql_pwd, wp_db_name,))
        sudo('mysql -p%s -e "CREATE USER %s@localhost IDENTIFIED BY \'%s\';"' % (mysql_pwd, wp_user_name, wp_user_pwd))
        sudo("mysql -p%s -e 'GRANT ALL PRIVILEGES ON %s .* TO %s@localhost;'" % (mysql_pwd, wp_db_name, wp_user_name))
        sudo("mysql -p%s -e 'FLUSH PRIVILEGES;'" % mysql_pwd)


def install_server():
    sudo(
        'apt-get install -y php5-gd libssh2-php php5-mysql php5-common php5-cli libapache2-mod-php5 php5-mcrypt apache2'
    )
    checkapache = run('service httpd status')
    if 'running' in checkapache:
        pass
    else:
        sudo('service apache2 start')
    run('sleep 3')


def config_mysql():
    sudo('echo mysql-server mysql-server/root_password password %s | debconf-set-selections' % mysql_pwd)
    sudo('echo mysql-server mysql-server/root_password_again password %s | debconf-set-selections' % mysql_pwd)
    sudo('apt-get -y install mysql-server python-mysqldb curl expect')
    checkmysql = run('service mysql status')
    if 'running' in checkmysql:
        mysqlcommand()
    else:
        sudo('service mysql start')
        mysqlcommand()


def install_wp():
    with cd("~/"):
        run('wget http://wordpress.org/latest.tar.gz')
        run("sleep 5")
        run('tar zxvf latest.tar.gz')
    with cd('~/wordpress'):
        run('mv wp-config-sample.php wp-config.php')
        run("sed -i 's/database_name_here/%s/g' wp-config.php" % wp_db_name)
        run("sed -i 's/username_here/%s/g' wp-config.php" % wp_user_name)
        run("sed -i 's/password_here/%s/g' wp-config.php" % wp_user_pwd)


def init_wp():
    sudo('rsync -avP ~/wordpress/ /var/www/html/')
    sudo('mkdir /var/www/html/wp-content/uploads')
    sudo("rm /var/www/html/index.html")
    sudo('service apache2 restart')


def showos():
    print "go to http://%s/ to test your wordpress website !" % env.hosts