# script updates the limit's value for a number of opened file for user holberton
exec { 'increases the hard limit value for user - holberton':
    command => 'sed -i \'s/holberton hard [A-Za-z0-9]*/holberton hard nofile 500/g\' /etc/security/limits.conf',
    path    => ['/bin/', '/usr/bin/']
}

exec { 'increases the soft limit value for user - holberton':
    command => 'sed -i \'s/holberton soft [A-Za-z0-9]*/holberton soft nofile 500/g\' /etc/security/limits.conf',
    path    => ['/bin/', '/usr/bin/']
}
