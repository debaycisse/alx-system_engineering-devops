# kills a process, which is named killmenow.
exec {'pkill ./killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
}