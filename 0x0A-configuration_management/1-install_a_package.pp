# manifest that installs flask via pip3
package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => pip3,
}