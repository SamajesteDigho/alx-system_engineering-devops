# Configures the /etc/ssh/ssh_config file

File { '/etc/ssh/ssh_config':
    ensure => present,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
}

FileLine { 'disable password_auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    replace => {
        '^#?PasswordAuthentication yes' => 'PasswordAuthentication no',
        '^#?IdentityFile .*'            => 'IdentityFile ~/.ssh/school',
    }
}
