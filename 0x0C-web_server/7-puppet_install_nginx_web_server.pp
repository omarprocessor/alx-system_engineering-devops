# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

# Allow Nginx through the firewall
firewall { '100 allow nginx':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}

# Create the root HTML file with "Hello World!"
file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
  require => Service['nginx'],
}

# Configure Nginx to listen on port 80 and set up redirect
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Redirect /redirect_me to a new URL with a 301 status
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => 'file',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Create a symbolic link for the redirect configuration
file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
}
