# Install python3-pip if not already installed
package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}

# Install werkzeug version 2.1.1 (compatible with Flask 2.1.0)
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show werkzeug | grep -q "Version: 2.1.1"',
  require => Exec['install_flask'],
}
