# Configures the /etc/ssh/ssh_config file
ini_setting { 'disable password_auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    section => 'Host',
    setting => 'PasswordAuthentication',
    value   => 'no',
},

ini_setting { 'disable password_auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    section => 'Host',
    setting => 'IdentityFile',
    value   => '~/.ssh/school',
},
