# Install Nginx package
class { 'nginx': }

nginx::resource::server { 'default':
  listen_port => 80,
  server_name => '_',
  locations   => {
    '/' => {
      'root' => '/var/www/html',
      'index' => 'index.html',
    },
    '/redirect_me' => {
      'return' => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4',
    },
  },
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}
