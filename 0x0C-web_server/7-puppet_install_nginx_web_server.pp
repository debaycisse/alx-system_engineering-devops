# installs and configures an nginx server
exec { 'sudo apt-get update':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
}

exec { 'sudo apt-get -y install nginx':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
  until    => 'which nginx',
}

exec { 'sudo ufw allow “Nginx HTTP”':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
}

exec { 'echo "Hello World!" | sudo tee /var/www/html/index.html':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
}

exec { 'sudo su':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
}

exec { 'sudo sed -i \'53i \\n\tlocation /redirect_me {\n\t\trewrite  ^/r(.*)e{0,1}/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n\t}\' /etc/nginx/sites-available/default':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
}

exec { 'exit':
  path     => [ '/usr/bin/', '/usr/sbin' ],
  provider => shell,
}