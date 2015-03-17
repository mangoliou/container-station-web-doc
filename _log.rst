Log and Event
=============

Log
------------------

.. http:get:: /api/v1/log

    :query time_start: (optional) Time stamp of system logs start time (epoch). **Default is 0.**
    :query time_end: (optional) Time stamp of system logs end time (epoch). **Default is 0.**
    :query limit: (optional) Number of system log records. **Default is 20.**
    :query offset: (optional) Response logs start with.
    :query user: (optional) User name who login.
    :query level: (optional) Log level like ``INFO``, ``WARN``, ``ERROR``.
    :query category: (optional) Function category like ``container``, ``image``, ``import``, ``export``, ``backup``, ``system``.
    :query text: (optional) Filter text

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/log?limit=5"

    **Example response**

    .. sourcecode:: json

        [
            {
                "category": "import",
                "id": 53,
                "level": "INFO",
                "message": "Finished import container (lxc, utest_import) from (/test/c.tgz) (return=0)",
                "ts": 1426526976,
                "user": "Anonymous"
            },
            {
                "category": "system",
                "id": 52,
                "level": "INFO",
                "message": "Create a new folder at /home/vagrant/container-station-web/test/new_folder",
                "ts": 1426526973,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 51,
                "level": "INFO",
                "message": "Import task logs are cleared",
                "ts": 1426526967,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 50,
                "level": "INFO",
                "message": "Start to import container (lxc, utest_import) from (/test/c.tgz)",
                "ts": 1426526966,
                "user": "Anonymous"
            },
            {
                "category": "container",
                "id": 49,
                "level": "INFO",
                "message": "Destroy container (lxc, utest_import)",
                "ts": 1426526963,
                "user": "Anonymous"
            }
        ]
        
        

        (echo "import log.log as ctlog\nctlog.info('Hello container station', 'TestUser1', 'container')\nctlog.warn('Hello container station', 'TestUser2', 'container')\nctlog.error('Hello container station', 'TestUser3', 'container')" | sudo VIRTUAL_ENV=$VIRTUAL_ENV PATH=$PATH python -);
        http_proxy= curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/log?limit=5" | python -mjson.tool


.. http:get:: /api/v1/log/export

    Export logs to csv format.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/log/export

    **Example response**

    .. sourcecode:: text

        [
            {
                "category": "import",
                "id": 53,
                "level": "INFO",
                "message": "Finished import container (lxc, utest_import) from (/test/c.tgz) (return=0)",
                "ts": 1426526976,
                "user": "Anonymous"
            },
            {
                "category": "system",
                "id": 52,
                "level": "INFO",
                "message": "Create a new folder at /home/vagrant/container-station-web/test/new_folder",
                "ts": 1426526973,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 51,
                "level": "INFO",
                "message": "Import task logs are cleared",
                "ts": 1426526967,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 50,
                "level": "INFO",
                "message": "Start to import container (lxc, utest_import) from (/test/c.tgz)",
                "ts": 1426526966,
                "user": "Anonymous"
            },
            {
                "category": "container",
                "id": 49,
                "level": "INFO",
                "message": "Destroy container (lxc, utest_import)",
                "ts": 1426526963,
                "user": "Anonymous"
            }
        ]
        
        

        http_proxy= curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/log/export

Event
------------------

.. http:get:: /api/v1/event

    :query index: start from. default returns the latest 20
    :query offset: the newest one

    **Response format**
    
    Category:User:JSON

    =========   =====  ==================================
    Category    User   JSON
    =========   =====  ==================================
    image       user   action: ``download``
                          - name: image name
                          - from: ``dockerhub``, ``appcenter``
                          - type: ``docker``, ``lxc``
                          - state: ``success``, ``error``
                       action: ``delete``
                          - name: image name
                          - type: ``docker``, ``lxc``
                          - state: ``success``, ``error``
                       action: ``update``
                          - from: ``local``, ``appcenter``, ``official``
                          - type: ``docker``, ``lxc``
    container   user   - container: container name
                       - id: container ID
                       - type: ``docker``, ``lxc``
                       - state: ``create``, ``start``, ``stop``, ``restart``, ``destroy``, ``pause``, ``unpause``
                       - port: ``add``, ``remove``
    export      user   - type: ``docker``, ``lxc``
                       - container: container name
                       - cid: container ID
                       - path: export to
                       - compress: ``true``, ``false``
                       - state: ``running``, ``completed``, ``aborted``
                       - result: if not ``0``, means something wrong.
    import      user   - type: ``docker``, ``lxc``
                       - cid: container name
                       - path: import from
                       - state: ``running``, ``completed``, ``aborted``
                       - result: if not ``0``, means something wrong.
    =========   =====  ==================================


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/event

    **Example response**

    .. sourcecode:: json

        {
            "index": 59,
            "messages": [
                "import:Anonymous:{\"state\": \"completed\", \"result\": 0, \"cid\": \"utest_import\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"stop\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "import:Anonymous:{\"tid\": 1, \"path\": \"/test/c.tgz\", \"state\": \"running\", \"type\": \"lxc\", \"cid\": \"utest_import\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"destroy\", \"type\": \"lxc\"}",
                "export:Anonymous:{\"container\": \"DockerTestAPI\", \"cid\": \"397568fb6bde77cd7cb98930b5400497aeca1ce3e91ef1d51f475723e8b9f65c\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "export:Anonymous:{\"container\": \"DockerTestAPI\", \"cid\": \"397568fb6bde77cd7cb98930b5400497aeca1ce3e91ef1d51f475723e8b9f65c\", \"compress\": true, \"state\": \"running\", \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "export:Anonymous:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"type\": \"lxc\", \"port\": \"add\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "export:Anonymous:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"running\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"state\": \"start\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "image:Anonymous:{\"action\": \"delete\", \"state\": \"success\", \"type\": \"docker\", \"name\": \"lgsd/diamond\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"delete\", \"from\": \"local\", \"id\": \"091f251415982b8a4f6b2ad04e1f6284362ef34792175e50b53e59c56d3ce689\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"delete\", \"from\": \"local\", \"id\": \"ffc94ca58a3b479dfb18e32b75ef605dfeb2d43aba243ff933edbc7018330865\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"delete\", \"from\": \"local\", \"id\": \"bfa7f7cadbffc9375bae0f57267f4c6939158574f791bb7e8a757e00c3ce9c32\"}"
            ],
            "offset": 79
        }
        
        

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/event | python -mjson.tool


.. http:get:: /api/v1/event/wait/(string:container_type)/(string:container_id)/(string:state)

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id
    :param state: ``running``, ``stopped``
    :query duration: timeout in seconds (default: 60)

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/stopped?duration=5"

    **Example response**

    .. sourcecode:: json

        {
            "cpu": 0.0,
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "ipaddress": [
                "10.0.3.201"
            ],
            "memory": 10846208,
            "name": "utest",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "lxc"
        }
        
        

        curl -sq -XPOST -b cookies.txt -d '{"type": "lxc", "name": "utest", "image": "ubuntu-trusty", "tag": "latest"}' http://${QIP}:${QPORT}/api/v1/container  -o /dev/null; 
        curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/stopped?duration=5" | python -mjson.tool
