# Configures the /etc/ssh/ssh_config file

file { 'disable password_auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    replace => {
        '^#?PasswordAuthentication yes' => 'PasswordAuthentication no',
        '^#?IdentityFile .*'            => 'IdentityFile ~/.ssh/school',
    }
}
