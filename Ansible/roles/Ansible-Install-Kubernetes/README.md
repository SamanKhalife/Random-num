# Install kubernetes ( Ansible )

```
- hosts: master
  become: yes
  roles:
    - install_dependencies
    - install_kubernetes
    - configure_containerd
    - master_setup
    - configure_calico

- hosts: worker
  become: yes
  roles:
    - install_dependencies
    - install_kubernetes
    - configure_containerd
    - worker_setup
```


```
[master]
master-1 ansible_host=master_node_ip

[worker]
worker-1 ansible_host=node1_ip
worker-2 ansible_host=node2_ip
```