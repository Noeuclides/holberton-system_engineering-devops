# Web stack debugging
exec { '/var/www/html/wp-setting.php':
     path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
     command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}root@2c50e8984428:~# cat 0-strace_is_your_friend.pp
# Web stack debugging
exec { '/var/www/html/wp-setting.php':
     path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
     command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}