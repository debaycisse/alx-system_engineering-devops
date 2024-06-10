# script changes the value of nginx configuration of the ULIMIT from 15 to 500 so that each nginx service worker can have more files opened. This is required to enable nginx to serve multiple simultaneous requests.
exec { "increases the value of the ULIMIT":
    command => "sed -i 's/ULIMIT=.*/ULIMIT=\"-n 500\"/g' /etc/default/nginx",
    path    => "/bin/"
}

exec { "restarts the nginx web server":
    command => "service nginx restart",
    path    => ["/usr/sbin/", "/bin/", "/usr/bin/"]
}
