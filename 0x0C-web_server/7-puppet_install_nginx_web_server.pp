#  we’d like you to install and configure an Nginx server using Puppet instead of Bash
#update before install nijinx
exec { 'install_system':
    command => '/usr/bin/apt-get update',
}
#install nignix
package { 'nginx':
    ensure  => 'installed',
    require => Exec['install_system']
}
#print hello world
file {'/var/www/html/index.html':
    content => 'Hello World!'
}
#handle redirect
exec {'redirect':
    command  => 'sed -i "24i\	rewrite ^/redirect https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

service {'nginx':
    ensure  => running,
    require => Package['nginx']
}
