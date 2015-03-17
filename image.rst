Image
==================

Images would be from the depots, including

* local: images had been downloaded in local disk
* appcenter: images located in QNAP AppCenter, which needs to be downloaded before using
* dockerhub: images located in Docker Hub, which needs to be downloaded before using

.. http:get:: /api/v1/image/

    Get image list from specific depots.
    If depots is from dockerhub, it will take a few seconds to search.
    Filter installed image functio only effect for depots from appcenter.

    :param filter_text: (optional) filter image name and description or query string for docker search
    :param type: (optional) one of ``lxc``, ``docker``, *empty_string*
    :param from: (optional) one of ``local``, ``appcenter``, ``official``, ``dockerhub``. **Default: local**
    
    From local repository:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?from=local"

    **Example response**

    .. sourcecode:: json

        {
            "filter_text": "",
            "from": "local",
            "results": [
                {
                    "description": "Ubuntu 14.04",
                    "downloading": false,
                    "from": "local",
                    "icon": "repository/lxc/ubuntu-trusty/icon.png",
                    "installed": true,
                    "name": "ubuntu-trusty",
                    "size": 275382272,
                    "type": "lxc"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "local",
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "lgsd/diamond",
                    "size": [
                        1211189
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "local",
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "qnap.dorowu.com/busybox",
                    "size": [
                        2433303
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "local",
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "qnap.dorowu.com/qnap/builder",
                    "size": [
                        1182387082
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "local",
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "qnap/builder",
                    "size": [
                        585003814
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "local",
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "ubuntu",
                    "size": [
                        192683310,
                        192683310,
                        192672387
                    ],
                    "tags": [
                        "14.04",
                        "14.04",
                        "latest"
                    ],
                    "type": "docker"
                }
            ],
            "total_count": 6,
            "type": ""
        }
        
        
    From App Center:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?from=appcenter"

    **Example response**

    .. sourcecode:: json

        {
            "filter_text": "",
            "from": "appcenter",
            "results": [
                {
                    "arch": "amd64",
                    "description": "Deluge is a lightweight, Free Software, cross-platform BitTorrent client.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/deluge_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "aostanin/deluge",
                    "size": null,
                    "title": "Deluge",
                    "type": "docker"
                },
                {
                    "arch": "armhf",
                    "description": "ARMHF official Fedora image on Online Labs.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/fedora_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "armbuild/ocs-distrib-fedora:20",
                    "size": null,
                    "title": "Fedora 20",
                    "type": "docker"
                },
                {
                    "arch": "armhf",
                    "description": "ARMHF port of ubuntu.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/ubuntu_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "armbuild/ubuntu:14.04",
                    "size": null,
                    "title": "Ubuntu 14.04",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "A Minecraft multiplayer server with Bukkit running in a Docker container.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/minecraft_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "chrisabrams/docker-minecraft-with-bukkit",
                    "size": null,
                    "title": "Minecraft",
                    "type": "docker"
                },
                {
                    "arch": "armhf",
                    "description": "ARMHF port of ubuntu with noVNC.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/ubuntu_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "colinhuang/ubuntu-novnc-armhf",
                    "size": null,
                    "title": "Ubuntu with noVNC",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Wine enables Linux users to run Windows applications without a copy of Microsoft Windows.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/wine_linux_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "colinhuang/wine-with-novnc",
                    "size": null,
                    "title": "Ubuntu with Wine and noVNC",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "The Debian Project is an association of individuals who have made common cause to create a free operating system.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/debian_icon.png",
                    "inspect": "{}",
                    "installed": false,
                    "name": "debian-wheezy",
                    "size": "173363200",
                    "title": "Debian 7.8",
                    "type": "lxc"
                },
                {
                    "arch": "amd64",
                    "description": "Remote desktop Sharing in Ubuntu 14.04.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/ubuntu_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "dorowu/ubuntu-desktop-lxde-vnc",
                    "size": null,
                    "title": "Ubuntu desktop with noVNC",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Fedora (formerly Fedora Core) is an operating system based on the Linux kernel, developed by the community-supported Fedora Project and owned by Red Hat.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/fedora_icon.png",
                    "inspect": "{}",
                    "installed": false,
                    "name": "fedora-heisenbug",
                    "size": "297496576",
                    "title": "Fedora 20",
                    "type": "lxc"
                },
                {
                    "arch": "armhf",
                    "description": "Fedora (formerly Fedora Core) is an operating system based on the Linux kernel, developed by the community-supported Fedora Project and owned by Red Hat.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/fedora_icon.png",
                    "inspect": "{}",
                    "installed": false,
                    "name": "fedora-heisenbug-armhf",
                    "size": "286060544",
                    "title": "Fedora 20",
                    "type": "lxc"
                },
                {
                    "arch": "amd64",
                    "description": "Official Jenkins Docker image.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/jenkins_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "jenkins",
                    "size": null,
                    "title": "Jenkins",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Fast, free and incredibly easy to use, the Ubuntu operating system powers millions of desktop PCs, laptops and servers around the world.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/ubuntu_icon.png",
                    "inspect": "{}",
                    "installed": true,
                    "name": "ubuntu-trusty",
                    "size": "275382272",
                    "title": "Ubuntu 14.04",
                    "type": "lxc"
                },
                {
                    "arch": "armhf",
                    "description": "Fast, free and incredibly easy to use, the Ubuntu operating system powers millions of desktop PCs, laptops and servers around the world.",
                    "downloading": false,
                    "from": "appcenter",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/ubuntu_icon.png",
                    "inspect": "{}",
                    "installed": false,
                    "name": "ubuntu-trusty-armhf",
                    "size": "275382272",
                    "title": "Ubuntu 14.04",
                    "type": "lxc"
                }
            ],
            "total_count": 13,
            "type": ""
        }
        
        
    
    
    From Docker Official Repositories:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?from=official"

    **Example response**

    .. sourcecode:: json

        {
            "filter_text": "",
            "from": "official",
            "results": [
                {
                    "arch": "amd64",
                    "description": "The official build of CentOS.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/centos_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/_/centos/",
                    "name": "centos:7",
                    "title": "CentOS 7",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "MongoDB document databases provide high availability and easy scalability.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/mongo_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/_/mongo/",
                    "name": "mongo",
                    "title": "MongoDB",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Official build of Nginx.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/nginx_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/_/nginx/",
                    "name": "nginx",
                    "title": "Nginx",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Node.js is a JavaScript-based platform for server-side and networking applications.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/nodejs_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/_/node/",
                    "name": "node",
                    "title": "Node.js",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Redis is an open source key-value store that functions as a data structure server.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/redis_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/_/redis/",
                    "name": "redis",
                    "title": "Redis",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "MySQL Server image - listens in port 3306. For the admin account password, either set MYSQL_PASS environment variable, or check the logs for a randomly generated one.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/mysql_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/u/tutum/mysql/",
                    "name": "tutum/mysql",
                    "title": "MySQL",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Wordpress Docker image - listens in port 80. Includes bundled MySQL server.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container_icon.png",
                    "installed": false,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/u/tutum/wordpress/",
                    "name": "tutum/wordpress",
                    "title": "WordPress",
                    "type": "docker"
                },
                {
                    "arch": "amd64",
                    "description": "Official Ubuntu base image.",
                    "downloading": false,
                    "from": "official",
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/ubuntu_icon.png",
                    "installed": true,
                    "is_official": true,
                    "location": "https://registry.hub.docker.com/_/ubuntu/",
                    "name": "ubuntu:14.04",
                    "title": "Ubuntu 14.04",
                    "type": "docker"
                }
            ],
            "total_count": 8,
            "type": ""
        }
        
        
    From Docker Hub:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
              "http://${QIP}:${QPORT}/api/v1/image/?from=dockerhub&filter_text=dorowu"

    **Example response**

    .. sourcecode:: json

        {
            "filter_text": "dorowu",
            "from": "dockerhub",
            "results": [
                {
                    "description": "Ubuntu with openssh-server and NoVNC on port 6080  ",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/ubuntu-desktop-lxde-vnc",
                    "name": "dorowu/ubuntu-desktop-lxde-vnc",
                    "star_count": 8,
                    "type": "docker"
                },
                {
                    "description": "Ubuntu with openssh server and tty.js enabled on port 3000",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/ubuntu-ssh-ttyjs",
                    "name": "dorowu/ubuntu-ssh-ttyjs",
                    "star_count": 2,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/ubuntu-lxqt-vnc",
                    "name": "dorowu/ubuntu-lxqt-vnc",
                    "star_count": 2,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/lightop-ubuntu-trusty-ttyjs",
                    "name": "dorowu/lightop-ubuntu-trusty-ttyjs",
                    "star_count": 1,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/lightop",
                    "name": "dorowu/lightop",
                    "star_count": 0,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/lightop-ubuntu-trusty-lxde",
                    "name": "dorowu/lightop-ubuntu-trusty-lxde",
                    "star_count": 0,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/glusterfs-keepalived",
                    "name": "dorowu/glusterfs-keepalived",
                    "star_count": 0,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "from": "dockerhub",
                    "installed": false,
                    "is_official": false,
                    "is_trusted": false,
                    "location": "https://registry.hub.docker.com/u/dorowu/etcd",
                    "name": "dorowu/etcd",
                    "star_count": 0,
                    "type": "docker"
                }
            ],
            "total_count": 8,
            "type": ""
        }
        
        
.. http:get:: /api/v1/image/(string:image_type)/(string:image_name)/(string:image_tag)/inspect

    Inspect image information.

    :param image_type: ``docker``
    :param image_name: image name
    :param image_name: image tag, which is ``latest`` or other version number

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/image/docker/ubuntu/latest/inspect"

    **Example response**

    .. sourcecode:: json

        {
            "Architecture": "amd64",
            "Author": "",
            "Comment": "",
            "Config": {
                "AttachStderr": false,
                "AttachStdin": false,
                "AttachStdout": false,
                "Cmd": [
                    "/bin/bash"
                ],
                "CpuShares": 0,
                "Cpuset": "",
                "Domainname": "",
                "Entrypoint": null,
                "Env": [
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                ],
                "ExposedPorts": null,
                "Hostname": "43bd710ec89a",
                "Image": "117ee323aaa9d1b136ea55e4421f4ce413dfc6c0cc6b2186dea6c88d93e1ad7c",
                "MacAddress": "",
                "Memory": 0,
                "MemorySwap": 0,
                "NetworkDisabled": false,
                "OnBuild": [],
                "OpenStdin": false,
                "PortSpecs": null,
                "StdinOnce": false,
                "Tty": false,
                "User": "",
                "Volumes": null,
                "WorkingDir": ""
            },
            "Container": "c9a3eda5951d28aa8dbe5933be94c523790721e4f80886d0a8e7a710132a38ec",
            "ContainerConfig": {
                "AttachStderr": false,
                "AttachStdin": false,
                "AttachStdout": false,
                "Cmd": [
                    "/bin/sh",
                    "-c",
                    "#(nop) CMD [/bin/bash]"
                ],
                "CpuShares": 0,
                "Cpuset": "",
                "Domainname": "",
                "Entrypoint": null,
                "Env": [
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                ],
                "ExposedPorts": null,
                "Hostname": "43bd710ec89a",
                "Image": "117ee323aaa9d1b136ea55e4421f4ce413dfc6c0cc6b2186dea6c88d93e1ad7c",
                "MacAddress": "",
                "Memory": 0,
                "MemorySwap": 0,
                "NetworkDisabled": false,
                "OnBuild": [],
                "OpenStdin": false,
                "PortSpecs": null,
                "StdinOnce": false,
                "Tty": false,
                "User": "",
                "Volumes": null,
                "WorkingDir": ""
            },
            "Created": "2015-02-21T02:11:06.735146646Z",
            "DockerVersion": "1.4.1",
            "Id": "2d24f826cb16146e2016ff349a8a33ed5830f3b938d45c0f82943f4ab8c097e7",
            "Os": "linux",
            "Parent": "117ee323aaa9d1b136ea55e4421f4ce413dfc6c0cc6b2186dea6c88d93e1ad7c",
            "Size": 0,
            "VirtualSize": 192672387
        }
        
        
.. http:get:: /api/v1/image/dockerhub/docker/(string:is_official)/(string:image_name)/tags

    Get image tags from Docker Hub. It will take a few seconds to finish.
    
    :param is_official: if image is official, it should be ``1``. Otherwise it should be ``0``.
    :param image_name: image name

    :resjson array installed: tags have been installed in local
    :resjson array tags: all tags of request image

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/image/dockerhub/docker/1/redis/tags"

    **Example response**

    .. sourcecode:: json

        {
            "installed": [],
            "tags": [
                "latest",
                "2",
                "2.6",
                "2.6.17",
                "2.8",
                "2.8.10",
                "2.8.11",
                "2.8.12",
                "2.8.13",
                "2.8.14",
                "2.8.15",
                "2.8.16",
                "2.8.17",
                "2.8.18",
                "2.8.19",
                "2.8.6",
                "2.8.7",
                "2.8.8",
                "2.8.9"
            ]
        }
        
        
.. http:post:: /api/v1/image/(string:from)/(string:image_type)/(string:image_name)/(string:image_tag)/download

    Download the image from app center or docker hub

    :param from: ``dockerhub``, ``appcenter``
    :param image_type: ``lxc``, ``docker``
    :param image_name: image name
    :param image_tag: image tag, which is ``latest`` or other version number

    :reqjson string description: description of this image
    :reqjson string location: url of this image
    :reqjson string icon: icon source of this image

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "description": "I am description.", 
                "location": "https://registry.hub.docker.com/u/lgsd/diamond/",
                "icon": "http://download.qnap.com/QPKG/images/QPKG/container_icon.png"
            }' "http://${QIP}:${QPORT}/api/v1/image/dockerhub/docker/lgsd/diamond/latest/download"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:get:: /api/v1/image/downloadstatus

    Get all downloading image status.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET "http://${QIP}:${QPORT}/api/v1/image/downloadstatus"
 

    **Example response**

    .. sourcecode:: json

        []
        
        
.. http:delete:: /api/v1/image/(string:from)/(string:image_type)/(string:image_name)

    Remove image function which is only used in ``local`` image.
    This request will take few seconds to finish. 

    :param from: ``dockerhub``, ``appcenter``
    :param image_type: ``lxc``, ``docker``
    :param image_name: image name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE "http://${QIP}:${QPORT}/api/v1/image/local/docker/lgsd/diamond"

    **Example response**

    .. sourcecode:: json

        {
            "action": "delete",
            "name": "lgsd/diamond",
            "state": "success",
            "type": "docker"
        }
        
        
