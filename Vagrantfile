# -*- mode: ruby -*-
# vi: set ft=ruby :

$msg = <<MSG
======================================================


███╗   ███╗███████╗████████╗ █████╗ ██╗      █████╗ ██████╗
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║     ██╔══██╗██╔══██╗
██╔████╔██║█████╗     ██║   ███████║██║     ███████║██████╔╝
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║     ██╔══██║██╔══██╗
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗██║  ██║██████╔╝
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚════╝

Vagrant VM Development Machine

How to proceed further:

enter the VM with:
$ vagrant ssh

Execute the following commands inside the VM:

1) You have to set the 'admin' superuser password manually
$ ./manage.py changepassword admin

2) Start the server bound on all interfaces instead of 127.0.0.1 only
$ ./manage.py runserver 0.0.0.0:8000

Access the instance under http://localhost:8000 in your browser

Modifications in the folder will be immediately available in the dev environment.


=====================================================
MSG


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  config.vm.provision "shell" do |s|
    s.path = "bootstrap_ansible.sh"
  end

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "debian/contrib-buster64"
  config.vm.hostname = "mos"
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network :forwarded_port, guest: 8000, host: 8000, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.post_up_message = $msg
end
