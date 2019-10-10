# Web stack debugging
exec { '/etc/security/limits.conf':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 50/g" \
/etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
}
exec {'soft':
  command => 'sed -i "s/holberton soft nofile 4/holberton hard nofile 40/g" \
/etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
}
exec { 'sysctl':
  command => 'sysctl -p',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
