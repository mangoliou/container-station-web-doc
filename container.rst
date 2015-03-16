Container
=============

.. automodule:: ctstation

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

    .. runcode:: json

        curl -sq -XPOST  -d '{"description":"Fast, free and incredibly easy to use, the Ubuntu operating system powers millions of desktop PCs, laptops and servers around the world."}' http://${QIP}:${QPORT}/api/v1/image/appcenter/lxc/ubuntu-trusty/latest/download -o /dev/null; 
        while :; do curl -sq -XGET "http://${QIP}:${QPORT}/api/v1/image/downloadstatus" | python -c "import json, sys; sys.exit(len(json.loads(sys.stdin.read())))"; 
            if [ "$?" -eq "0" ]; then 
                break; 
            fi; 
            sleep 5; 
        done; 
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/stop -o /dev/null; 
        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest -o /dev/null;
        curl -sq -XPOST -b cookies.txt -d
            '{
                "type": "lxc",
                "name": "utest",
                "image": "ubuntu-trusty",
                "tag": "latest",
                "autostart": true,
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
            | python -m json.tool;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/stop -o /dev/null;
        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest -o /dev/null;
        curl -sq -XPOST -b cookies.txt -d
            '{"type": "lxc", "name": "utest", "image": "ubuntu-trusty", "tag": "latest"}'
            http://${QIP}:${QPORT}/api/v1/container
            | python -m json.tool;

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

    .. runcode:: json

        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI`;
        echo $id | grep -q error || curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/stop -o /dev/null;
        echo $id | grep -q error || curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id} -o /dev/null;
        curl -sq -XPOST -b cookies.txt -d
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
            | python -m json.tool;
        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI2`;
        echo $id | grep -q error || curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/stop -o /dev/null;
        echo $id | grep -q error || curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id} -o /dev/null;
        curl -sq -XPOST -b cookies.txt -d 
            '{"type": "docker", "name": "DockerTestAPI2", "image": "ubuntu", "tag": "latest"}'
            http://${QIP}:${QPORT}/api/v1/container
            | python -m json.tool;
    
.. http:get:: /api/v1/container

    .. autosimple:: api.container_get_all

    :resjson array object: :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container

    **Example response**

    .. runcode:: json

        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/start -o /dev/null;
        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/running?duration=20 -o /dev/null;
        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container | python -mjson.tool


.. http:get:: /api/v1/container/(string:container_type)/(string:container_id)/inspect

    .. autosimple:: api.container_inspect
    

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/inspect

    **Example response of Docker**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/DockerTestAPI/inspect | python -mjson.tool


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

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/DockerTestAPI/logs | python -mjson.tool


.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/start

    .. autosimple:: api.container_start

    Return the last status by :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/start

    **Example response of LXC**

    .. runcode:: json

        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/stop -o /dev/null;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/start | python -mjson.tool

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/start

    **Example response of Docker**

    .. runcode:: json

        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI` ;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/stop -o /dev/null;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/start | python -mjson.tool


.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/restart

    .. autosimple:: api.container_restart

    Return the last status by :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/restart

    **Example response of LXC**

    .. runcode:: json

        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/restart | python -mjson.tool

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/restart

    **Example response of Docker**

    .. runcode:: json

        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI` ;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/restart | python -mjson.tool


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

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/running?duration=20 -o /dev/null;
        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest | python -mjson.tool


.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/stop

    .. autosimple:: api.container_stop

    Return the last status by :http:get:`/api/v1/container/(string:container_type)/(string:container_id)`

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/stop

    **Example response of LXC**

    .. runcode:: json

        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/stop | python -mjson.tool

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/stop

    **Example response of Docker**

    .. runcode:: json

        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI` ;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/stop | python -mjson.tool


.. http:delete:: /api/v1/container/(string:container_type)/(string:container_id)

    .. autosimple:: api.container_destroy

    Return {} if success

    **Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest

    **Example response of LXC**

    .. runcode:: json

        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest | python -mjson.tool

    **Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>

    **Example response of Docker**

    .. runcode:: json

        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI2` ;
        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/stop -o /dev/null;
        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id} | python -mjson.tool;