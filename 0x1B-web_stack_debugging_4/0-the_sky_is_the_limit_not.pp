# Web stack debugging
exec { '/etc/default/nginx':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i s/15/4096/g /etc/default/nginx',
}

exec { '/etc/security/limits.conf':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed $ a "# Added Nginx limits\nnginx       soft    nofile  30000\nnginx       hard    nofile  50000" /etc/security/limits.conf',
}

#exec { '/etc/nginx/nginx.conf':
#  path    => '/usr/bin:/usr/sbin:/bin',
#  command => 'sed '4 a # 2019-10-09 Increase open files' /etc/nginx/nginx.conf',
#  command => 'sed '5 a worker_rlimit_nofile 30000;' /etc/nginx/nginx.conf',
#}