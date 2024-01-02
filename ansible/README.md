## Ansible demo

## create two container as ansible master and slave

### for master
> docker build -t master .

> docker run -it master

### for slave
> docker build -t slave .

> docker run -it slave

## generate ssh key in master
> ssh-keygen

> sudo cat ~/.ssh/id_rsa.pub   #to check ssh key

## get Ip address of slave
> ifconfig

## provide login permissions in slave
> echo "Port 22">>/etc/ssh/sshd_config

> echo "PermitRootLogin yes">>/etc/ssh/sshd_config

> service ssh restart

> service ssh status  #check status of ssh service

> passwd  #set password

## verify connection from master
> ssh-copy-id <username>@<slave_ip_address>

## login to slave machine, from master (execute the following command in master)
> sudo ssh <slave-username>@<ip-address-of-slave>

> exit #to exit out of slave machine

## verify connection with ansible commands from master
> vi /etc/hosts #update ip_Address of slave in hosts file

> ansible -i /etc/hosts -m ping all