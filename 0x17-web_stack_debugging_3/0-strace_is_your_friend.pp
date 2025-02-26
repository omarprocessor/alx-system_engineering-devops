# This Puppet manifest fixes the Apache 500 error by ensuring the necessary module is enabled

class apache_fix {
    exec { 'enable-php-module':
        command => '/usr/sbin/a2enmod php5',
        unless  => '/bin/ls /etc/apache2/mods-enabled/php5.load',
    }

    exec { 'restart-apache':
        command => '/etc/init.d/apache2 restart',
        subscribe => Exec['enable-php-module'],
        refreshonly => true,
    }
}

include apache_fix
