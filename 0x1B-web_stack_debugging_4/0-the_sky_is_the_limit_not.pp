# Web stack debugging
exec { '/etc/default/nginx':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i s/15/4096/g /etc/default/nginx',
}->
exec { '/etc/security/limits.conf':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}