Vagrant.configure("2") do |config|
  config.vm.box = 'bgch_secure_1404'
  config.vm.box_url = 'http://dist.bgchtest.info:/vagrant/bgch_secure_1404.box'
  config.vm.synced_folder '.', '/usr/lib/dockerdemo'
  config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get purge -y docker
     apt-get install -y docker.io
     apt-get install -y python-pip
     pip install bottle
  SHELL
end
