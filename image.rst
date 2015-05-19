Image
==================

.. contents::

Images would be from the depots, including

* local: images had been downloaded in local disk
* qnap: images selected by QNAP, which needs to be download before using
* dockerhub: images located in Docker Hub, which needs to be downloaded before using

Search
-----------------

.. http:get:: /api/v1/image/

    Get image list from specific depots.
    If depots is from dockerhub, it will take a few seconds to search.
    Filter installed image function only effect for depots from qnap.

    :param filter_text: (optional) filter image name and description or query string for docker search
    :param type: (optional) one of ``lxc``, ``docker``, *empty_string*
    :param category: (optional) one of ``local``, ``qnap``, ``official``, ``dockerhub``. **Default: local**
    
    From local repository:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?category=local"

    **Example response**

    .. sourcecode:: json

        {
            "category": "local",
            "filter_text": "",
            "results": [
                {
                    "description": "Ubuntu 14.04",
                    "downloading": false,
                    "icon": "repository/lxc/ubuntu-trusty/icon.png",
                    "installed": true,
                    "name": "ubuntu-trusty",
                    "repository": "local",
                    "size": [
                        "275382272"
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "lxc"
                },
                {
                    "description": "",
                    "downloading": false,
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "qnap.dorowu.com/qnap/builder",
                    "repository": "local",
                    "size": [
                        1183207922
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "icon": "",
                    "installed": true,
                    "is_latest": [],
                    "name": "sameersbn/postgresql",
                    "repository": "local",
                    "size": [
                        228211218
                    ],
                    "tags": [
                        "9.4"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "icon": "",
                    "installed": true,
                    "is_latest": [],
                    "name": "sameersbn/redmine",
                    "repository": "local",
                    "size": [
                        618160542,
                        617775210
                    ],
                    "tags": [
                        "3.0.2",
                        "3.0.3"
                    ],
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "icon": "",
                    "installed": true,
                    "is_latest": [
                        "latest"
                    ],
                    "name": "ubuntu",
                    "repository": "local",
                    "size": [
                        188304295
                    ],
                    "tags": [
                        "latest"
                    ],
                    "type": "docker"
                }
            ],
            "total_count": 5,
            "type": ""
        }
        
        
    From QNAP selected:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?category=qnap"

    **Example response**

    .. sourcecode:: json

        {
            "category": "qnap",
            "filter_text": "",
            "results": [
                {
                    "arch": "amd64",
                    "description": "The Debian Project is an association of individuals who have made common cause to create a free operating system.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/debian_icon.png",
                    "inspect": "{}",
                    "installed": false,
                    "name": "debian-wheezy",
                    "repository": "qnap",
                    "size": "173363200",
                    "title": "Debian",
                    "type": "lxc",
                    "version": "7.8"
                },
                {
                    "arch": "amd64",
                    "description": "Fedora (formerly Fedora Core) is an operating system based on the Linux kernel, developed by the community-supported Fedora Project and owned by Red Hat.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/fedora_icon.png",
                    "inspect": "{}",
                    "installed": false,
                    "name": "fedora-heisenbug",
                    "repository": "qnap",
                    "size": "297496576",
                    "title": "Fedora",
                    "type": "lxc",
                    "version": "20"
                },
                {
                    "arch": "amd64",
                    "description": "Fast, free and incredibly easy to use, the Ubuntu operating system powers millions of desktop PCs, laptops and servers around the world.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/ubuntu_icon.png",
                    "inspect": "{}",
                    "installed": true,
                    "name": "ubuntu-trusty",
                    "repository": "qnap",
                    "size": "275382272",
                    "title": "Ubuntu",
                    "type": "lxc",
                    "version": "14.04"
                },
                {
                    "arch": "amd64",
                    "description": "Deluge is a lightweight, Free Software, cross-platform BitTorrent client.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/deluge_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "aostanin/deluge",
                    "repository": "dockerhub",
                    "size": null,
                    "title": "Deluge",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "A Minecraft multiplayer server with Bukkit running in a Docker container.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/minecraft_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "chrisabrams/docker-minecraft-with-bukkit",
                    "repository": "dockerhub",
                    "size": null,
                    "title": "Minecraft",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Wine enables Linux users to run Windows applications without a copy of Microsoft Windows.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/wine_linux_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "colinhuang/wine-with-novnc",
                    "repository": "dockerhub",
                    "size": null,
                    "title": "Ubuntu with Wine and noVNC",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Remote desktop Sharing in Ubuntu 14.04.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/ubuntu_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "dorowu/ubuntu-desktop-lxde-vnc",
                    "repository": "dockerhub",
                    "size": null,
                    "title": "Ubuntu desktop with noVNC",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Official Jenkins Docker image.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/jenkins_icon.png",
                    "inspect": "",
                    "installed": false,
                    "name": "jenkins",
                    "repository": "dockerhub",
                    "size": null,
                    "title": "Jenkins",
                    "type": "docker",
                    "version": "latest"
                }
            ],
            "total_count": 8,
            "type": ""
        }
        
        
    
    
    From Docker Hub repository:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?category=official"

    **Example response**

    .. sourcecode:: json

        {
            "category": "official",
            "filter_text": "",
            "results": [
                {
                    "arch": "amd64",
                    "description": "The official build of CentOS.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/centos_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/_/centos/",
                    "name": "centos",
                    "repository": "dockerhub",
                    "title": "CentOS",
                    "type": "docker",
                    "version": "7"
                },
                {
                    "arch": "amd64",
                    "description": "MongoDB document databases provide high availability and easy scalability.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/mongo_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/_/mongo/",
                    "name": "mongo",
                    "repository": "dockerhub",
                    "title": "MongoDB",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Official build of Nginx.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/nginx_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/_/nginx/",
                    "name": "nginx",
                    "repository": "dockerhub",
                    "title": "Nginx",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Node.js is a JavaScript-based platform for server-side and networking applications.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/nodejs_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/_/node/",
                    "name": "node",
                    "repository": "dockerhub",
                    "title": "Node.js",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Redis is an open source key-value store that functions as a data structure server.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/redis_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/_/redis/",
                    "name": "redis",
                    "repository": "dockerhub",
                    "title": "Redis",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "MySQL Server image - listens in port 3306. For the admin account password, either set MYSQL_PASS environment variable, or check the logs for a randomly generated one.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/mysql_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/u/tutum/mysql/",
                    "name": "tutum/mysql",
                    "repository": "dockerhub",
                    "title": "MySQL",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Wordpress Docker image - listens in port 80. Includes bundled MySQL server.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/container_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/u/tutum/wordpress/",
                    "name": "tutum/wordpress",
                    "repository": "dockerhub",
                    "title": "WordPress",
                    "type": "docker",
                    "version": "latest"
                },
                {
                    "arch": "amd64",
                    "description": "Official Ubuntu base image.",
                    "downloading": false,
                    "icon": "http://download.qnap.com/QPKG/images/QPKG/container/ubuntu_icon.png",
                    "installed": false,
                    "location": "https://registry.hub.docker.com/_/ubuntu/",
                    "name": "ubuntu",
                    "repository": "dockerhub",
                    "title": "Ubuntu",
                    "type": "docker",
                    "version": "14.04"
                }
            ],
            "total_count": 8,
            "type": ""
        }
        
        
    From Docker Hub search:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
              "http://${QIP}:${QPORT}/api/v1/image/?category=dockerhub&filter_text=dorowu"

    **Example response**

    .. sourcecode:: json

        {
            "category": "dockerhub",
            "filter_text": "dorowu",
            "results": [
                {
                    "description": "Ubuntu with openssh-server and NoVNC on port 6080  ",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/ubuntu-desktop-lxde-vnc",
                    "name": "dorowu/ubuntu-desktop-lxde-vnc",
                    "repository": "dockerhub",
                    "star_count": 12,
                    "type": "docker"
                },
                {
                    "description": "Ubuntu with openssh server and tty.js enabled on port 3000",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/ubuntu-ssh-ttyjs",
                    "name": "dorowu/ubuntu-ssh-ttyjs",
                    "repository": "dockerhub",
                    "star_count": 3,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/ubuntu-lxqt-vnc",
                    "name": "dorowu/ubuntu-lxqt-vnc",
                    "repository": "dockerhub",
                    "star_count": 2,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/lightop-ubuntu-trusty-ttyjs",
                    "name": "dorowu/lightop-ubuntu-trusty-ttyjs",
                    "repository": "dockerhub",
                    "star_count": 1,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/lightop",
                    "name": "dorowu/lightop",
                    "repository": "dockerhub",
                    "star_count": 0,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/lightop-ubuntu-trusty-lxde",
                    "name": "dorowu/lightop-ubuntu-trusty-lxde",
                    "repository": "dockerhub",
                    "star_count": 0,
                    "type": "docker"
                },
                {
                    "description": "",
                    "downloading": false,
                    "installed": false,
                    "is_official": false,
                    "is_trusted": true,
                    "location": "https://registry.hub.docker.com/u/dorowu/glusterfs-keepalived",
                    "name": "dorowu/glusterfs-keepalived",
                    "repository": "dockerhub",
                    "star_count": 0,
                    "type": "docker"
                }
            ],
            "total_count": 7,
            "type": ""
        }
        
        
Inspect & tags
-----------------


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
                "Env": null,
                "ExposedPorts": null,
                "Hostname": "9ec8c01a6a48",
                "Image": "37bea4ee0c816e3a3fa025f36127ef8ef0817b3f8fcd7b49eb7b26064f647bb0",
                "Labels": {},
                "MacAddress": "",
                "Memory": 0,
                "MemorySwap": 0,
                "NetworkDisabled": false,
                "OnBuild": null,
                "OpenStdin": false,
                "PortSpecs": null,
                "StdinOnce": false,
                "Tty": false,
                "User": "",
                "Volumes": null,
                "WorkingDir": ""
            },
            "Container": "a07d9edec0b3a777941a33087d8351d31f9aadce9418ad628de5e05dcebe8a3f",
            "ContainerConfig": {
                "AttachStderr": false,
                "AttachStdin": false,
                "AttachStdout": false,
                "Cmd": [
                    "/bin/sh",
                    "-c",
                    "#(nop) CMD [\"/bin/bash\"]"
                ],
                "CpuShares": 0,
                "Cpuset": "",
                "Domainname": "",
                "Entrypoint": null,
                "Env": null,
                "ExposedPorts": null,
                "Hostname": "9ec8c01a6a48",
                "Image": "37bea4ee0c816e3a3fa025f36127ef8ef0817b3f8fcd7b49eb7b26064f647bb0",
                "Labels": {},
                "MacAddress": "",
                "Memory": 0,
                "MemorySwap": 0,
                "NetworkDisabled": false,
                "OnBuild": null,
                "OpenStdin": false,
                "PortSpecs": null,
                "StdinOnce": false,
                "Tty": false,
                "User": "",
                "Volumes": null,
                "WorkingDir": ""
            },
            "Created": "2015-04-30T21:50:13.355542328Z",
            "DockerVersion": "1.6.0",
            "Id": "07f8e8c5e66084bef8f848877857537ffe1c47edd01a93af27e7161672ad0e95",
            "Os": "linux",
            "Parent": "37bea4ee0c816e3a3fa025f36127ef8ef0817b3f8fcd7b49eb7b26064f647bb0",
            "Size": 0,
            "VirtualSize": 188304295
        }
        
        
.. http:get:: /api/v1/image/(string:image_type)/(string:image_name)/(string:image_tag)/remote_inspect

    Inspect image information.

    :param image_type: ``docker``
    :param image_name: image name
    :param image_name: image tag, which is ``latest`` or other version number

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/image/docker/redis/latest/remote_inspect"

    **Example response**

    .. sourcecode:: json

        Failed to run command
        curl -sq -XGET -b cookies.txt     "http://${QIP}:${QPORT}/api/v1/image/docker/redis/latest/remote_inspect" | python -m json.tool
        
        
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
                "2.8.20",
                "2.8.6",
                "2.8.7",
                "2.8.8",
                "2.8.9",
                "3",
                "3.0",
                "3.0.0",
                "3.0.1"
            ]
        }
        
        
Download
-----------------


.. http:post:: /api/v1/image/(string:repository)/(string:image_type)/(string:image_name)/(string:image_tag)/download

    Download the image from QNAP or Docker Hub

    :param repository: ``dockerhub``, ``qnap``
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

        [
            {
                "name": "lgsd/diamond",
                "percent": null,
                "status": "downloading"
            }
        ]
        
        
.. http:delete:: /api/v1/image/(string:repository)/(string:image_type)/(string:image_name)

    Remove image function which is only used in ``local`` image.
    This request will take few seconds to finish. 

    :param repository: ``local`` 
    :param image_type: ``lxc``, ``docker``
    :param image_name: image name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE "http://${QIP}:${QPORT}/api/v1/image/local/docker/lgsd/diamond"

    **Example response**

    .. sourcecode:: json

        {
            "error": {
                "code": 404,
                "message": "Image not found: lgsd/diamond"
            }
        }
        
        
