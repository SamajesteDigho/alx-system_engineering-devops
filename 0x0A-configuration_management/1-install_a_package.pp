# create a package installation manifest
package { 'flask':
    ensure   => 'v2.1.0',
    provider => 'pip3',
}
