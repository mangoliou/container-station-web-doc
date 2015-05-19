Container
=============

.. http:post:: /api/v1/container

    .. autosimple:: api.container_create

    :reqjson string name: container name **[required]**
    :reqjson string image: image name **[required]**
    :reqjson string tag: image tag. For LXC is ``latest``  **[required]**
    :reqjson string type: ``lxc``, ``docker`` **[required]**


    **Request in JSON format**

    =============== ========== ===== ====== ===============
    Key             Type       LXC   Docker Description
    =============== ========== ===== ====== ===============
    type            String     v     v      'lxc' or 'docker'
    name            String     v     v      Assign a name to the container
    image           String     v     v      Assign a base image to the container
    tag             String     v     v      lxc is 'latest'
    autostart       Boolean    v     v      Automatically start the container after reboot
    privileged      Boolean          v      Give extended privileges to this container
    entrypoint      String           v      Overwrite the default ENTRYPOINT of the image
    command         String           v      Run a command in container
    user            String           v      Username or UID
    working_dir     String           v      Working directory inside the container
    environment     Str Array        v      Set environment variables
    links           Object           v      Add link to another container in the form of name:alias
    **network**
    dns             Str Array        v      Set custom DNS servers
    expose_port     Int Array        v      Expose a port from the container without publishing it to your host
    hostname        String           v      Container host name
    port            Array      v     v      Publish a container's port to the host
    **resource**
    limit
    cpuweight       Int        v     v      2~1024 in relative share of CPU time
    cputime         Int        v     v      10~999 in milliseconds(ms)
    memory          String     v     v      String with 'm' in MB. Must higher than 64m
    device          Str Array  v     v      Add a host device to the container
    **volume**
    host            Object     v     v      Mount a volume from host shared folders
    container       Str Array        v      Mount volumes from the specified container
    new             Str Array        v      Mount a new volume
    =============== ========== ===== ====== ===============


.. note::
    Input check for ``name``
     - :regexp:`^([a-zA-Z0-9][a-zA-Z0-9-_.]{1,63})$`
         only [a-zA-Z0-9][a-zA-Z0-9-_.] are allowed, size between 2 and 64

    Input check for ``image``
      - Format: ``namespace/name`` or ``name``
      - namespace :regexp:`^([a-z0-9_]{4,30})$`
          only [a-z0-9\_] are allowed, size between 4 and 30
      - name :regexp:`^([a-z0-9-_.]+)$`
          only [a-z0-9-_.] are allowed


**Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "type": "lxc",
                "name": "utest",
                "image": "ubuntu-trusty",
                "tag": "latest",
                "autostart": true,
                "network": {
                    "port": [
                        [
                            12345,
                            1234,
                            "udp"
                        ]
                    ]
                },
                "resource": {
                    "device": [
                        [
                            "allow",
                            "video4linux_(81)",
                            "rw"
                        ]
                    ],
                    "limit": {
                        "cputime": 512,
                        "cpuweight": 512,
                        "memory": "768m"
                    }
                },
                "volume": {
                    "host": {
                        "/test/selenium": {
                            "bind": "/mnt/vol1",
                            "ro": true
                        },
                        "/test/spec": {
                            "bind": "/mnt/vol2",
                            "ro": false
                        }
                    }
                }
            }' http://${QIP}:${QPORT}/api/v1/container

        $ curl -sq -XPOST -b cookies.txt -d \
            '{"type": "lxc", "name": "utest", "image": "ubuntu-trusty", "tag": "latest"}' \
            http://${QIP}:${QPORT}/api/v1/container

**Example response of LXC**

    .. sourcecode:: json

        {
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "name": "utest",
            "state": "stopped",
            "type": "lxc"
        }
        {
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "name": "utest",
            "state": "stopped",
            "type": "lxc"
        }
        
        
**Example request of Docker**

    .. sourcecode:: bash
        
        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "type": "docker",
                "name": "DockerTestAPI",
                "image": "ubuntu",
                "tag": "latest",
                "autostart": false,
                "privileged": true,
                "entrypoint": "cat",
                "command": "/etc/passwd",
                "environment": [
                    "QPORT=90", 
                    "QIP=1.2.3.4"
                ],
                "network": {
                    "hostname": "CustomHostName",
                    "port": [
                        [
                            12345,
                            1234,
                            "udp"
                        ]
                    ]
                },
                "resource": {
                    "limit": {
                        "cputime": 512,
                        "cpuweight": 512,
                        "memory": "768"
                    }
                },
                "volume": {
                    "host": {
                        "/test/selenium": {
                            "bind": "/mnt/vol1",
                            "ro": true
                        },
                        "/test/spec": {
                            "bind": "mnt/vol2",
                            "ro": false
                        }
                    }
                }
            }' http://${QIP}:${QPORT}/api/v1/container

        $ curl -sq -XPOST -b cookies.txt -d \
            '{"type": "docker", "name": "DockerTestAPI2", "image": "ubuntu", "tag": "latest"}' \
            http://${QIP}:${QPORT}/api/v1/container

**Example response of Docker**

    .. sourcecode:: json

        {
            "id": "1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a",
            "name": "DockerTestAPI",
            "type": "docker"
        }
        {
            "id": "11abb7a227d7c6001e8bb5f6418f284845123e6dc56ef95309e6d3881d51f3a4",
            "name": "DockerTestAPI2",
            "type": "docker"
        }
        
        
    
.. http:get:: /api/v1/container

    .. autosimple:: api.container_get_all

    :resjson array object: :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container

    **Example response**

    .. sourcecode:: json

        [
            {
                "cpu": 0.0032679738562091504,
                "id": "ctest",
                "image": "ubuntu-trusty:latest",
                "ipaddress": [
                    "10.0.3.62"
                ],
                "memory": 11546624,
                "name": "ctest",
                "rx": 180,
                "state": "running",
                "tx": 0,
                "type": "lxc"
            },
            {
                "cpu": 0.0,
                "id": "utest",
                "image": "ubuntu-trusty:latest",
                "ipaddress": [],
                "memory": 1937408,
                "name": "utest",
                "rx": 0,
                "state": "running",
                "tx": 0,
                "type": "lxc"
            },
            {
                "id": "utest_import",
                "image": "import:latest",
                "name": "utest_import",
                "state": "stopped",
                "type": "lxc"
            },
            {
                "id": "1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a",
                "image": "ubuntu:latest",
                "name": "DockerTestAPI",
                "state": "stopped",
                "type": "docker"
            },
            {
                "cpu": 0.0,
                "id": "11abb7a227d7c6001e8bb5f6418f284845123e6dc56ef95309e6d3881d51f3a4",
                "image": "ubuntu:latest",
                "ipaddress": [],
                "memory": 520192,
                "name": "DockerTestAPI2",
                "rx": 0,
                "state": "running",
                "tx": 0,
                "type": "docker"
            },
            {
                "id": "b52f11e1a8c782903ae2996331b9bd22c0f00625a893a1f4b937bf5f17584c8f",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "admiring_mclean",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "9041046d4a51be3cb18b09d3df4745f4248328be9e086cae3b99d39313555a29",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "cranky_lalande",
                "state": "stopped",
                "type": "docker"
            },
            {
                "cpu": 0.0,
                "id": "4a3633b8730da0bad1e1713894eeddf31488a06a9be83f979a1c29761a36c488",
                "image": "ubuntu:latest",
                "ipaddress": [
                    "10.0.5.6"
                ],
                "memory": 4726784,
                "name": "dtest",
                "rx": 0,
                "state": "running",
                "tx": 0,
                "type": "docker"
            },
            {
                "id": "4f0ffbd93089155bacb086fba7530800b6c8f2bfce03bd9565b1c817c740f5ec",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "gloomy_sinoussi",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "c934121a39810a52384822f982a306fe0cd8974c3a63de2fedae33e46321a24e",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "sad_bohr",
                "state": "stopped",
                "type": "docker"
            },
            {
                "cpu": 0.0,
                "id": "6103de4dc3164a7f2e3801b5e939b92a6621287282015eef6f90e770ed3ddd85",
                "image": "sameersbn/postgresql:9.4",
                "ipaddress": [
                    "10.0.5.3"
                ],
                "memory": 40468480,
                "name": "test_postgresql_1",
                "rx": 0,
                "state": "running",
                "tx": 0,
                "type": "docker"
            },
            {
                "cpu": 0.0,
                "id": "91c32e322df3121fa0566f6f98405fc1cfbfa74eec79444aa03ee178242ab2cd",
                "image": "sameersbn/redmine:3.0.2",
                "ipaddress": [
                    "10.0.5.5"
                ],
                "memory": 210853888,
                "name": "test_redmine_1",
                "rx": 0,
                "state": "running",
                "tx": 0,
                "type": "docker"
            }
        ]
        
        
.. http:get:: /api/v1/container/(string:container_type)/(string:container_id)/inspect

    .. autosimple:: api.container_inspect
    

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/inspect

    **Example response of Docker**

    .. sourcecode:: json

        {
            "AppArmorProfile": "",
            "Args": [
                "/etc/passwd"
            ],
            "Config": {
                "AttachStderr": false,
                "AttachStdin": false,
                "AttachStdout": false,
                "Cmd": [
                    "/etc/passwd"
                ],
                "CpuShares": 512,
                "Cpuset": "",
                "Domainname": "",
                "Entrypoint": [
                    "cat"
                ],
                "Env": [
                    "QPORT=90",
                    "QIP=1.2.3.4"
                ],
                "ExposedPorts": {
                    "1234/udp": {}
                },
                "Hostname": "CustomHostName",
                "Image": "ubuntu:latest",
                "Labels": {},
                "MacAddress": "",
                "Memory": 805306368,
                "MemorySwap": -1,
                "NetworkDisabled": false,
                "OnBuild": null,
                "OpenStdin": true,
                "PortSpecs": null,
                "StdinOnce": false,
                "Tty": true,
                "User": "",
                "Volumes": null,
                "WorkingDir": ""
            },
            "Created": "2015-05-19T08:05:06.940651806Z",
            "Driver": "aufs",
            "ExecDriver": "native-0.2",
            "ExecIDs": null,
            "HostConfig": {
                "Binds": [
                    "/home/vagrant/container-station-web/test/spec:/mnt/vol2:rw",
                    "/home/vagrant/container-station-web/test/selenium:/mnt/vol1:ro"
                ],
                "CapAdd": null,
                "CapDrop": null,
                "CgroupParent": "",
                "ContainerIDFile": "",
                "CpuShares": 0,
                "CpusetCpus": "",
                "Devices": null,
                "Dns": null,
                "DnsSearch": null,
                "ExtraHosts": null,
                "IpcMode": "",
                "Links": null,
                "LogConfig": {
                    "Config": null,
                    "Type": "json-file"
                },
                "LxcConf": null,
                "Memory": 0,
                "MemorySwap": 0,
                "NetworkMode": "",
                "PidMode": "",
                "PortBindings": {
                    "1234/udp": [
                        {
                            "HostIp": "0.0.0.0",
                            "HostPort": "12345"
                        }
                    ]
                },
                "Privileged": true,
                "PublishAllPorts": false,
                "ReadonlyRootfs": false,
                "RestartPolicy": {
                    "MaximumRetryCount": 0,
                    "Name": ""
                },
                "SecurityOpt": null,
                "Ulimits": null,
                "VolumesFrom": null
            },
            "HostnamePath": "/var/lib/docker/containers/1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a/hostname",
            "HostsPath": "/var/lib/docker/containers/1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a/hosts",
            "Id": "1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a",
            "Image": "07f8e8c5e66084bef8f848877857537ffe1c47edd01a93af27e7161672ad0e95",
            "LogPath": "/var/lib/docker/containers/1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a/1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a-json.log",
            "MountLabel": "",
            "Name": "/DockerTestAPI",
            "NetworkSettings": {
                "Bridge": "",
                "Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "IPAddress": "",
                "IPPrefixLen": 0,
                "IPv6Gateway": "",
                "LinkLocalIPv6Address": "",
                "LinkLocalIPv6PrefixLen": 0,
                "MacAddress": "",
                "PortMapping": null,
                "Ports": null
            },
            "Path": "cat",
            "ProcessLabel": "",
            "ResolvConfPath": "/var/lib/docker/containers/1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a/resolv.conf",
            "RestartCount": 0,
            "State": {
                "Dead": false,
                "Error": "",
                "ExitCode": 0,
                "FinishedAt": "2015-05-19T08:05:07.230472971Z",
                "OOMKilled": false,
                "Paused": false,
                "Pid": 0,
                "Restarting": false,
                "Running": false,
                "StartedAt": "2015-05-19T08:05:07.172782762Z"
            },
            "Volumes": {
                "/mnt/vol1": "/home/vagrant/container-station-web/test/selenium",
                "/mnt/vol2": "/home/vagrant/container-station-web/test/spec"
            },
            "VolumesRW": {
                "/mnt/vol1": false,
                "/mnt/vol2": true
            }
        }
        
        
.. http:get:: /api/v1/container/(string:container_type)/(string:container_id)/logs

    .. autosimple:: api.container_logs
    
    Support Docker container only.
    
    :query tail: (optional) Output the specified number of lines at the end of logs. **Default is 100.**

    :resjson string logs: logs string
    :resjson int tail: the last N line of output

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/logs

    **Example response of Docker**

    .. sourcecode:: json

        {
            "logs": ":0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\nlibuuid:x:100:101::/var/lib/libuuid:\nsyslog:x:101:104::/home/syslog:/bin/false\n",
            "tail": 100
        }
        
        
.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/start

    .. autosimple:: api.container_start

    Return the last status by :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/start

    **Example response of LXC**

    .. sourcecode:: json

        {
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "name": "utest",
            "state": "stopped",
            "type": "lxc"
        }
        
        
    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/start

    **Example response of Docker**

    .. sourcecode:: json

        {
            "cpu": 0.0,
            "id": "1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a",
            "image": "ubuntu:latest",
            "ipaddress": [],
            "memory": 0,
            "name": "DockerTestAPI",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "docker"
        }
        
        
.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/restart

    .. autosimple:: api.container_restart

    Return the last status by :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/restart

    **Example response of LXC**

    .. sourcecode:: json

        {
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "name": "utest",
            "state": "stopped",
            "type": "lxc"
        }
        
        
    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/restart

    **Example response of Docker**

    .. sourcecode:: json

        {
            "cpu": 0.0,
            "id": "1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a",
            "image": "ubuntu:latest",
            "ipaddress": [],
            "memory": 0,
            "name": "DockerTestAPI",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "docker"
        }
        
        
.. http:get:: /api/v1/container/(string:container_type)/(string:container_id)

    .. autosimple:: api.container_get

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    :resjson string id: container ID
    :resjson string name: container name
    :resjson string image: derived from
    :resjson string state: one of ``running``, ``stopped``
    :resjson string type: one of ``lxc``, ``docker``
    :resjson float cpu: cpu usage
    :resjson int memory: memory usage
    :resjson int rx: network receive rate
    :resjson int tx: network transmit rate
    :resjson array ipaddress: container IP address

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest

    **Example response**

    .. sourcecode:: json

        {
            "cpu": 0.0,
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "ipaddress": [],
            "memory": 1941504,
            "name": "utest",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "lxc"
        }
        
        
.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/stop

    .. autosimple:: api.container_stop

    Return the last status by :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/stop

    **Example response of LXC**

    .. sourcecode:: json

        {
            "cpu": 0.07484022872519341,
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "ipaddress": [
                "10.0.3.21"
            ],
            "memory": 10723328,
            "name": "utest",
            "rx": 1145,
            "state": "running",
            "tx": 1310,
            "type": "lxc"
        }
        
        
    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/stop

    **Example response of Docker**

    .. sourcecode:: json

        {
            "id": "1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a",
            "image": "ubuntu:latest",
            "name": "DockerTestAPI",
            "state": "stopped",
            "type": "docker"
        }
        
        
.. http:delete:: /api/v1/container/(string:container_type)/(string:container_id)

    .. autosimple:: api.container_destroy

    Return {} if success

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest

    **Example response of LXC**

    .. sourcecode:: json

        {}
        
        
    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>

    **Example response of Docker**

    .. sourcecode:: json

        {}
        
        
