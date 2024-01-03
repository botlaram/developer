## Ansible demo

## create two container as ansible master and slave

### for master
> docker build -t master .

> docker run -it master

### for slave
> docker build -t slave .

> docker run -it slave

### generate ssh key in master
> ssh-keygen

> sudo cat ~/.ssh/id_rsa.pub   #to check ssh key

### get Ip address of slave
> ifconfig

### provide login permissions in slave
> echo "Port 22">>/etc/ssh/sshd_config

> echo "PermitRootLogin yes">>/etc/ssh/sshd_config

> service ssh restart

> service ssh status  #check status of ssh service

> passwd  #set password

### verify connection from master
> ssh-copy-id <username>@<slave_ip_address> #this will ask to enter slave password

### login to slave machine, from master (execute the following command in master)
> sudo ssh <slave-username>@<ip-address-of-slave>

> exit #to exit out of slave machine

### verify connection with ansible commands from master
> vi /etc/hosts #update ip_Address of slave in hosts file

> ansible -i /etc/hosts -m ping all

### execute ansible adhoc copy command (in master)
> cd /opt && touch file.txt

> ansible all -i /etc/hosts --module-name copy --args "src=/opt/file.txt dest=/tmp/file.txt"

## demo1: install git using ansible in slave
> apt remove git #if git in already in slave, uninstall

### template for ansible tasks
> ansible-galaxy init demo

### task/main.yml update the script to install git

> vi tasks/main.yml

```yaml
- name: Update package lists
  ansible.builtin.apt:
    update_cache: yes
  become: true

- name: Install Git
  ansible.builtin.apt:
    name: git
    state: present
  become: true

- name: Check Git version
  ansible.builtin.shell: git --version
  register: git_version_output

- name: Display Git version
  ansible.builtin.debug:
    var: git_version_output.stdout
```

### to perform this action in slave we need to add ip address to inventory file

> vi tests/inventory #add slave ipaddress

### update tests/test.yml name with slave-ipaddress

> vi tests/test.yml

```yaml
- hosts: 172.17.0.3
  remote_user: root
  roles:
    - demo
```

### validate ansible playbook

> ansible-playbook --syntax-check /opt/demo/tests/test.yml

### execute the script by providing path till tests/test.yml and inventory file(where you have updated the ip address)

> ansible-playbook -i /etc/hosts /opt/demo/tests/test.yml

### to run with debug mode

> ansible-playbook -i /etc/hosts /opt/demo/tests/test.yml -vvv