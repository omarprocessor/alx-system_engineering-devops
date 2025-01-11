# This Puppet manifest configures SSH client to use the private key ~/.ssh/school and disables password authentication
file { '/home/vagrant/.ssh/config':
  ensure  => 'file',
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
  content => "
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no
  ",
}
