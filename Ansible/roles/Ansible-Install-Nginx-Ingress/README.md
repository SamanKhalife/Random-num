# Install Nginx Ingress Controller ( Ansible )

You can use this role to install [Nginx Ingress](https://github.com/kubernetes/ingress-nginx) for Kubernetes.

For the sake of clarity, there are two versions of Nginx Ingress controller:

-   **Community version** – Found in the **[kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx)** repo on GitHub, the community Ingress controller is based on Nginx Open Source with docs on Kubernetes.io. It is maintained by the Kubernetes community with a [commitment from F5 Nginx](https://www.nginx.com/blog/nginx-sprint-2-0-clear-vision-fresh-code-new-commitments-to-open-source/#resources-for-kubernetes) to help manage the project
-   **Nginx version** – Found in the **[nginxinc/kubernetes-ingress](https://github.com/nginxinc/kubernetes-ingress)** repo on GitHub, Nginx Ingress Controller is developed and maintained by F5 Nginx with docs on [docs.nginx.com](https://docs.nginx.com/nginx-ingress-controller/). It is available in two editions:
    -   Nginx Open Source‑based (free and open source option)
    -   Nginx Plus-based (commercial option)

> A ❤ for community

## How-to

First you need instal the role:

-   Clone this role:

    ```bash
    git clone git@github.com:hatamiarash7/Ansible-Install-Nginx-Ingress.git install_nginx_ingress
    ```

-   Or you can install using galaxy:

    ```bash
    ansible-galaxy install hatamiarash7.install_nginx_ingress
    ```

Then, Include role in Playbook:

```yml
- hosts: all
    roles:
        - hatamiarash7.install_nginx_ingress
```

## Dependencies

This role will use [Helm](https://helm.sh/) to install Nginx ingress. Also you need **Docker** & **Kubernetes**. Take a look at these roles too:

-   [install_docker](https://github.com/hatamiarash7/Ansible-Install-Docker)
-   [install_kubernetes](https://github.com/hatamiarash7/Ansible-Install-Kubernetes)
-   [install_helm](https://github.com/hatamiarash7/Ansible-Install-Helm)

## Usage

```yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
    name: documentation
    annotations:
        kubernetes.io/ingress.class: nginx
spec:
    rules:
        - host: docs.domain.ir
          http:
              paths:
                  - path: /
                    pathType: Prefix
                    backend:
                        service:
                            name: documentation
                            port:
                                number: 3000
```

**Note :** The default [configuration](files/ingress-nginx.yml) was changed to work with `kubeadm` managed clusters.

---

## Support 💛

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/bc1qmmh6vt366yzjt3grjxjjqynrrxs3frun8gnxrz)](https://en.cryptobadges.io/donate/bc1qmmh6vt366yzjt3grjxjjqynrrxs3frun8gnxrz) [![Donate with Ethereum](https://en.cryptobadges.io/badge/micro/0x0831bD72Ea8904B38Be9D6185Da2f930d6078094)](https://en.cryptobadges.io/donate/0x0831bD72Ea8904B38Be9D6185Da2f930d6078094)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D1WGU9)

<div><a href="https://payping.ir/@hatamiarash7"><img src="https://cdn.payping.ir/statics/Payping-logo/Trust/blue.svg" height="128" width="128"></a></div>

## Contributing 🤝

Don't be shy and reach out to us if you want to contribute 😉

1. Fork it !
2. Create your feature branch : `git checkout -b my-new-feature`
3. Commit your changes : `git commit -am 'Add some feature'`
4. Push to the branch : `git push origin my-new-feature`
5. Submit a pull request

## Issues

Each project may have many problems. Contributing to the better development of this project by reporting them. 👍
