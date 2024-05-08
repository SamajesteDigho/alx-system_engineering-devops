# Configures the /etc/ssh/ssh_config file

File { '/etc/ssh/ssh_config':
    ensure  => present,
}

FileLine { 'disable password_auth':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication',
    value  => 'no',
}

FileLine { 'rsc file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile',
    value  => '~/.ssh/school',
}