# Web stack debugging
exec { '/var/www/html/wp-setting.php':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
}