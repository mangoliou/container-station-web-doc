Import and Export
==================

Export
--------------

.. http:post:: /api/v1/container/(string:container_type)/(string:container_id)/export

    Create an export task for container id ``container_id`` of container type ``container_type``. For JSON fields, check :http:get:`/api/v1/export/`. The path must be under the folders by :http:get:`/api/v1/sharefolder/(string:path)`.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    :reqjson string path: file path **[required]**
    :reqjson boolean compress: Compress export file or not. **Default: false**
    :reqjson boolean force: Force rewrite file or not. **Default:false**

.. note::
    Input check for ``path``
     - Extract filename and filename extensions from ``path`` 
     - Filename extensions are ``tar``, ``tgz``
     - :regexp:`^([a-zA-Z0-9-_]{1,20})$`
         only [a-zA-Z0-9-_] are allowed, size between 1 and 20


**Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "path": "test/c.tgz",
                "compress": true
            }' http://${QIP}:${QPORT}/api/v1/container/lxc/utest/export

**Example response of LXC**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d
            '{"type": "lxc", "name": "utest", "image": "ubuntu-trusty", "tag": "latest"}'
            http://${QIP}:${QPORT}/api/v1/container -o /dev/null;
        curl -sq -XPOST -d '{"path": "test/c.tgz", "compress": true, "force": true}' -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/export | python -m json.tool

    
**Example request of Docker**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "path": "test/d.tgz",
                "compress": true
            }' http://${QIP}:${QPORT}/api/v1/container/docker/<container_id>/export

**Example response of Docker**

    .. runcode:: json

        id=`curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/getid/DockerTestAPI` ;
        curl -sq -XPOST -d '{"path": "test/d.tgz", "compress": true, "force": true}' -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/docker/${id}/export | python -m json.tool

.. http:get:: /api/v1/export/

    Get export tasks list.

    :resjson int id: unique task id 
    :resjson string state: one of ``waiting``, ``running``, ``completed``, ``aborted``
    :resjson int result: 0 means success
    :resjson string type: container type
    :resjson string cid: container id
    :resjson string user: request user name
    :resjson string path: file path 
    :resjson bool compress: compress or not
    :resjson int init: time of initial request
    :resjson int start: time of starting in epoch
    :resjson int end: time of completion in epoch
    :resjson int progress: running progress [-1, 99]. -1 means no available progress.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/ | python -m json.tool


.. http:get:: /api/v1/export/progress

    It's a long polling that returns when progress changed of tasks. This method only returns **progress** changing, where the task state changed, then the event will be triggered by :http:get:`/api/v1/event`.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -m 5 -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/progress

    **Example response**

    .. runcode:: json

        sleep 2;
        curl -sq -m 5 -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/progress | python -m json.tool


.. http:delete:: /api/v1/export/

    Clear completed/aborted tasks in database. It will response with task ID which have been deleted.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/

    **Example response**

    .. runcode:: json

        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/ | python -m json.tool


Import
--------------

.. http:get:: /api/v1/import/(string:dirpath)/

    Given container archive path, query the configure

    :param dirpath: archive file relative parent path in NAS

    :query name: archive file name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/test/?name=c.tgz

    **Example response**

    .. runcode:: bash

        curl -sq -XPOST -d '{"path": "test/c.tgz", "compress": true}' -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest/export -o /dev/null;
        for i in `seq 10`; do curl -sq -m 5 -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/export/progress -o /dev/null;
            if [ "$?" -eq "28" ]; then
                break;
            fi;
            sleep 5;
        done;
        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/test/?name=c.tgz | python -mjson.tool;


.. http:post:: /api/v1/import/(string:dirpath)/

    Create an import task if name is given. The JSON parameters are the same as :http:post:`/api/v1/container`.

    :param dirpath: archive file relative parent path in NAS

    :query name: archive file name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "type": "lxc",
                "name": "utest_import",
                "image": "utest",
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
                        "/var": {
                            "bind": "/mnt/vol1",
                            "ro": true
                        },
                        "/tmp": {
                            "bind": "/mnt/vol2",
                            "ro": false
                        }
                    }
                }
            }' http://${QIP}:${QPORT}/api/v1/import/test/?name=c.tgz

    **Example response**

    .. runcode:: json

        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/container/lxc/utest_import -o /dev/null;
        sleep 3;
        curl -sq -XPOST -b cookies.txt -d
            '{
                "type": "lxc",
                "name": "utest_import",
                "image": "utest",
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
                        "/var": {
                            "bind": "/mnt/vol1",
                            "ro": true
                        },
                        "/tmp": {
                            "bind": "/mnt/vol2",
                            "ro": false
                        }
                    }
                }
            }' http://${QIP}:${QPORT}/api/v1/import/test/?name=c.tgz | python -mjson.tool;


.. http:get:: /api/v1/import/

    Get import tasks list.

    :resjson int id: unique id 
    :resjson string state: one of ``waiting``, ``running``, ``completed``, ``aborted``
    :resjson int result: 0 means success
    :resjson string type: container type
    :resjson string cid: container id
    :resjson string path: file path 
    :resjson string user: request user name
    :resjson int start: time of starting in epoch
    :resjson int end: time of completion in epoch
    :resjson int progress: running progress [-1, 99]. -1 means no available progress.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/ | python -m json.tool

.. http:get:: /api/v1/import/progress

    It's a long polling that returns when progress changed of tasks. This method only returns **progress** changing, where the task state changed, then the event will be triggered by :http:get:`/api/v1/event`.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -m 5 -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/progress

    **Example response**

    .. runcode:: json

        curl -sq -m 5 -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/progress | python -m json.tool



.. http:delete:: /api/v1/import/

    Clear completed/aborted tasks in database.

    :resjson array object: task ID which have been deleted.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/

    **Example response**

    .. runcode:: json

        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/import/ | python -m json.tool



File operations
---------------

.. http:get:: /api/v1/sharefolder/(string:path)

    List shared folders. If ``path`` does not exist, it will return 400 error.

    :param path: path of a folder

    :resjson string name: directory name or file name
    :resjson string type: ``d`` is directory, ``f`` is file. **[Deprecated]**
    :resjson bool is_dir: is directory or not
    :resjson bool write: write permission

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/
        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/test
        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/Public

    **Example response**

    .. runcode:: json

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/ | python -m json.tool; 
        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/test | python -m json.tool;
        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/Public | python -m json.tool;

.. http:post:: /api/v1/sharefolder/(string:dirname)/(string:basename)/

    Create the directory or file, if they do not already exist.

    :param dirname: directory name
    :param basename: the base name of dirname path

    :reqjson string name: name of directory or file **[required]**
    :reqjson bool is_dir: is directory or not **[required]**
    :reqjson string content: context of file **[required]**

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"name":"new_folder", "is_dir":true}' \
            http://${QIP}:${QPORT}/api/v1/sharefolder/test/
        $ curl -sq -XPOST -b cookies.txt \
             -d '{"name":"new_file.json", "is_dir":false, "context": ""}' \
            http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/
        $ curl -sq -XPOST -b cookies.txt \
             -d '{"name":"new_file.txt", "is_dir":false, "context":"I am context."}' \
            http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/

    **Example response**

    .. runcode:: json
    
        curl -sq -XPOST -b cookies.txt -d '{"name":"new_folder", "is_dir":true}' \
          http://${QIP}:${QPORT}/api/v1/sharefolder/test/ | python -m json.tool;
        curl -sq -XPOST -b cookies.txt -d '{"name":"new_file.json", "is_dir":false, "context": ""}' \
          http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/ | python -m json.tool;
        curl -sq -XPOST -b cookies.txt -d '{"name":"new_file.txt", "is_dir":false, "context":"I am context."}' \
          http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/ | python -m json.tool;


.. http:delete:: /api/v1/sharefolder/(string:dirname)/(string:basename)

    Delete selected file

    :param dirname: directory name
    :param basename: the base name of dirname path

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/new_file.json

    **Example response**

    .. runcode:: json

        #curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/new_file.json | python -m json.tool;

.. http:delete:: /api/v1/sharefolder/(string:dirname)/(string:basename)/

    Delete directories and their contents

    :param dirname: directory name
    :param basename: the base name of dirname path

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/

    **Example response**

    .. runcode:: json

        curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/sharefolder/test/new_folder/ | python -m json.tool;
