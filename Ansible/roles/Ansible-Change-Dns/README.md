# Change_Dns ( Ansible )




Then, Include role in Playbook:

```yml
- hosts: all
  roles:
    - Change_Dns
```




only runnig this playbook
```
ansible-playbook -i inventory set_dns.yml
```