# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Add the custom HTTP header X-Served-By to Nginx configuration
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => "add_header X-Served-By '${::hostname}';\n",
  notify  => Service['nginx'],  # Restart Nginx when the file is updated
}

# Ensure Nginx configuration is correct
exec { 'check_nginx_configuration':
  command => '/usr/sbin/nginx -t',
  unless  => '/usr/sbin/nginx -t',
  notify  => Service['nginx'],  # Restart Nginx if configuration is valid
}
