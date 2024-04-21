# creates a configuration file for an ssh connection
file {'/root/.ssh/config':
  ensure  => file,
  content => "Host 530748-web-01 34.229.55.139\n\tHostName 34.229.55.139\n\tIdentitiesOnly = yes\n\tIdentityFile ~/.ssh/school",
  mode    => "0600",
}