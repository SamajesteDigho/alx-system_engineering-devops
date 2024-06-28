# Enable helberton user to login and open files

# Increase head file limit
exec { 'increase-head-file':
    command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit
exec { 'increase-soft-file-limit':
    command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}
