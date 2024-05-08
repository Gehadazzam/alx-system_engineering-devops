# Puppet manifest to fix Apache 500 error

# Ensure the configuration file exists
file { '/etc/apache2/myconfig.conf':
  ensure => present,
  content => "Sample configuration content\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Restart Apache service after fixing
service { 'apache2':
  ensure => running,
  enable => true,
  require => File['/etc/apache2/myconfig.conf'],
}
