# create a package installation manifest
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    path     => [ '/usr/bin/python3', '/bin/' ],
}
