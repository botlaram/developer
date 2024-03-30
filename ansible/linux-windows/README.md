# Ansible

## Linux

1. Build the Docker Image
> docker build -t myubuntu-image .

2. Run the Docker Container
> docker run -it -v <src-folder>:/tmp/ <image-nameorid>

3. Install ansible galaxy role from Azure GIt (-p: path to install roles)
> ansible-galaxy install -r requirements.yaml -p /tmp/

4. Install playbook
> ansible-playbook axivion-playbook.yaml

## Windows

1. Install or Enable Winrm in Windows 
```powershell

# check winrm status
Get-Service WinRM   

# start Winrm if status is stopped
Start-Service WinRM

# generate self signed cert using the following command (add dns example:)
New-SelfSignedCertificate -DnsName "<replace-DnsName>" -CertStoreLocation "cert:\LocalMachine\My" 

# copy the thumbprint value from above output
winrm create winrm/config/Listener?Address=*+Transport=HTTPS '@{Hostname="<replace-DnsName>"; CertificateThumbprint="<replace-thumbprint>"}'



New-NetFirewallRule -Name "WinRM HTTPS" -DisplayName "WinRM HTTPS" -Enabled True -Direction Inbound -Profile Any -Action Allow -LocalPort 5986 -Protocol TCP

# verify winrm listener
winrm enumerate winrm/config/Listener

# display service details for winrm connection
winrm get winrm/config
```

2. docker pull Container

> docker pull ubuntu

> docker run -it -v /path/to/src/ansible-role:/tmp/ <image-id>

3. create ansible dir in /etc and copy hosts.ini file

> sudo mkdir /etc/ansible

> sudo cp /tmp/hosts.ini /etc/ansible/hosts.ini

4. host.ini file (get ip address from cmd: ipconfig)

> /etc/ansible/hosts.ini

```ini
[win]
ip address

[win:vars]
ansible_python_interpreter=C:\\AppData\\Local\\Programs\\Python\\Python39\\python
ansible_user=
ansible_password=add-user-password
ansible_connection=winrm
ansible_winrm_scheme=https
ansible_winrm_transport=ntlm
ansible_port=5986
ansible_winrm_server_cert_validation=ignore
```

5. run ansible playbook command
> ansible-playbook -i /etc/ansible/hosts.ini /tmp/ping-pong.yaml -vvv
> ansible-playbook -i /etc/ansible/hosts.ini /tmp/axivion-playbook.yaml -vvv  # update host name in playbook