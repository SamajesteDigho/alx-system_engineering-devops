# create a package installation manifest
package { 'flask':
    ensure   => 'installed',
    provider => 'pip3',
}
