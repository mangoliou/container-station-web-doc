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
                            "Open_Sound_System_(OSS)",
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
                        "/test": {
                            "bind": "/mnt/vol1",
                            "ro": true
                        },
                        "/test/image": {
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
                        "/test": {
                            "bind": "/mnt/vol1",
                            "ro": true
                        },
                        "/test/image": {
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
            "id": "08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765",
            "name": "DockerTestAPI",
            "type": "docker"
        }
        {
            "id": "0298a0baef28c3f3c6b41205b5ec36d35f54ed47407f797204bace90c50bb4b4",
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
                "id": "ctest",
                "image": "ubuntu-trusty:latest",
                "name": "ctest",
                "state": "stopped",
                "type": "lxc"
            },
            {
                "cpu": 0.12590999338186631,
                "id": "utest",
                "image": "ubuntu-trusty:latest",
                "ipaddress": [
                    "10.0.3.154"
                ],
                "memory": 11829248,
                "name": "utest",
                "rx": 1154,
                "state": "running",
                "tx": 622,
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
                "id": "08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765",
                "image": "ubuntu:latest",
                "name": "DockerTestAPI",
                "state": "stopped",
                "type": "docker"
            },
            {
                "cpu": 0.0,
                "id": "0298a0baef28c3f3c6b41205b5ec36d35f54ed47407f797204bace90c50bb4b4",
                "image": "ubuntu:latest",
                "ipaddress": [],
                "memory": 4677632,
                "name": "DockerTestAPI2",
                "rx": 0,
                "state": "running",
                "tx": 0,
                "type": "docker"
            },
            {
                "id": "33a1f5559bd06fd0c5a13bbb4ae9dd85490a9574391661c5c6b15068c9657aa4",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "admiring_wilson",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "0ab3bfaea1729fbdc51fc078538ac78698bf362a3b112f4350915a46c9ab94e6",
                "image": "8b7588c28346",
                "name": "agitated_elion",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "59324ec24850e3d9a52cc399f16adfd6da507a873ab37ee8c99ee4934626b11d",
                "image": "045e09d166d9",
                "name": "cranky_bardeen",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "f3ba3b9a079f22268a01ab85047927fc625bdad631ef87d9cc2953fa4361813a",
                "image": "ubuntu:latest",
                "name": "dtest",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "801a6fd9ec880212694d1a48bd1706031c9f614a2a34e7eaf21284f3f938728e",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "focused_hodgkin",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "787b0517b9909862b7497941a27659d83ab5c064b719310f2333e39962eb1b55",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "high_archimedes",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "3c10e3f22a8fede63d868774e96d9899d5df393b37868377c6c48b9834f6dd44",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "hopeful_banach",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "8fc2a29223b2eac8d8f1e5083a4a7619ec595a51a3d86880ce420b0d8601a0eb",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "hungry_colden",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "f50c9cd23b3624a59e0bf64aa814c0ff4f6751015f4e3157955e3074943f6ae4",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "hungry_pare",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "4f90178c8a8b61c19db167662a27eeca49957303ca5d02f746b251637b42b8db",
                "image": "b939fa700e56",
                "name": "insane_elion",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "fd3f3f92fb01d557df08b1f6cc76276b0c64a2cb00bd36872003e4068494a47f",
                "image": "045e09d166d9",
                "name": "insane_lumiere",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "3b823e76249e9da4c072bf502965dc21c16e79fff2f14e173ed0a22283438907",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "loving_rosalind",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "565d8d6db7d15ca6b1ed755d1ef0231336e82f1de4225c69307730d6c29c2ce3",
                "image": "qnap/builder:latest",
                "name": "mad_davinci",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "97d0eaaad055fb195e9938cf084d26edad320c52c05b174513ca6ee0da7921f3",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "nostalgic_brown",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "20cadd2428e5f0a16c589214badb91fae268af096c0f07c23cecc8623898823b",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "pensive_cori",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "77baa72bafb8436aafec2fabd876e0462ddb2d63640da8bdeefeeb89ec78b528",
                "image": "qnap.dorowu.com/qnap/builder:latest",
                "name": "sick_sinoussi",
                "state": "stopped",
                "type": "docker"
            },
            {
                "id": "38f6e30d0224831431ee0513e0a17fc12f45eb48d13575ae118db68107f0fa03",
                "image": "ubuntu:latest",
                "name": "thirsty_turing",
                "state": "stopped",
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
                    "QIP=1.2.3.4",
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                ],
                "ExposedPorts": {
                    "1234/udp": {}
                },
                "Hostname": "CustomHostName",
                "Image": "ubuntu:latest",
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
            "Created": "2015-03-17T17:28:51.569306978Z",
            "Driver": "devicemapper",
            "ExecDriver": "native-0.2",
            "ExecIDs": null,
            "HostConfig": {
                "Binds": [
                    "/home/vagrant/container-station-web/test/image:/mnt/vol2:rw",
                    "/home/vagrant/container-station-web/test:/mnt/vol1:ro"
                ],
                "CapAdd": null,
                "CapDrop": null,
                "ContainerIDFile": "",
                "Devices": null,
                "Dns": null,
                "DnsSearch": null,
                "ExtraHosts": null,
                "IpcMode": "",
                "Links": null,
                "LxcConf": null,
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
                "Privileged": false,
                "PublishAllPorts": false,
                "ReadonlyRootfs": false,
                "RestartPolicy": {
                    "MaximumRetryCount": 0,
                    "Name": ""
                },
                "SecurityOpt": null,
                "VolumesFrom": null
            },
            "HostnamePath": "/var/lib/docker/containers/08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765/hostname",
            "HostsPath": "/var/lib/docker/containers/08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765/hosts",
            "Id": "08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765",
            "Image": "2d24f826cb16146e2016ff349a8a33ed5830f3b938d45c0f82943f4ab8c097e7",
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
            "ResolvConfPath": "/var/lib/docker/containers/08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765/resolv.conf",
            "RestartCount": 0,
            "State": {
                "Error": "",
                "ExitCode": 0,
                "FinishedAt": "2015-03-17T17:28:52.158493073Z",
                "OOMKilled": false,
                "Paused": false,
                "Pid": 0,
                "Restarting": false,
                "Running": false,
                "StartedAt": "2015-03-17T17:28:52.075450136Z"
            },
            "Volumes": {
                "/mnt/vol1": "/home/vagrant/container-station-web/test",
                "/mnt/vol2": "/home/vagrant/container-station-web/test/image"
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
            "logs": ":0:root:/root:/bin/bash\r\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\r\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\r\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\r\nsync:x:4:65534:sync:/bin:/bin/sync\r\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\r\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\r\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\r\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\r\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\r\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\r\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\r\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\r\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\r\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\r\nirc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin\r\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\r\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\r\nlibuuid:x:100:101::/var/lib/libuuid:\r\nsyslog:x:101:104::/home/syslog:/bin/false\r\n",
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
            "id": "08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765",
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
            "id": "08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765",
            "image": "ubuntu:latest",
            "name": "DockerTestAPI",
            "state": "stopped",
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
            "memory": 2097152,
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
            "cpu": 0.0,
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "ipaddress": [
                "10.0.3.154"
            ],
            "memory": 10637312,
            "name": "utest",
            "rx": 70,
            "state": "running",
            "tx": 90,
            "type": "lxc"
        }
        
        
    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/stop

    **Example response of Docker**

    .. sourcecode:: json

        {
            "id": "08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765",
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
        
        
