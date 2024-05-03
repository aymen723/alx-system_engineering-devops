#!/usr/bin/pup
# to install a specifque flask ver
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
