# script updates the limit's value for a number of opened file for user holberton
exec { 'increases the hard limit value for user - holberton':
    command => 'sed -i \'s/holberton hard nofile 4/holberton hard nofile 500/g\' /etc/security/limits.conf',
    path    => ['/bin/', '/usr/bin/']
}

exec { 'increases the soft limit value for user - holberton':
    command => 'sed -i \'s/holberton soft nofile 4/holberton soft nofile 500/g\' /etc/security/limits.conf',
    path    => ['/bin/', '/usr/bin/']
}
