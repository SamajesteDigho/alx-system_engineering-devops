# Configure the trafic amount on Nginx

# Increase the ULIMIT
exec { 'fix--for-nginx',
    command => '/bin/sed -i "s/15/2048/" /etc/default/nginx',
    path    => 'usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart',
    command => '/etc/init.d/nginx restart',
    path    => '/etc/init.d/',
}
