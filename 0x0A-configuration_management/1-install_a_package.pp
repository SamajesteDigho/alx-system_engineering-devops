# create a package installation manifest
package { 'werkzeug':
    ensure => 'installed',
    provider => 'pip3',
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
