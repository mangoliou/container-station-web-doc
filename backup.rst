Draft for Backup and Restore
============================

**Requisite features**

  * Online backup
  * Offline backup (TBD)

    * live migration

  * Remote backup
  * Image and data (new folder, from host)
  * Incremental backup (TBD)
  * Backup container station (TBD)
  * Container Clone

**Backup folder layout ([F] means file, [D] means directory)**

    * [D] User-specified directory

      * [D] container-backup\@job_name

        * [F] backup-metadata
        * [F] image.tar
        * [D] <timestamp-1>

          * [F] <data.tar>

        * [D] <timestamp-2>

          * [F] <data.tar>



Targets
---------------------

.. http:post:: /api/v1/target/

    Create a backup remote target.

    :reqjson string name: name. **[required]**
    :reqjson string ipaddr: ip address. **[required]**
    :reqjson string desc: description
    :reqjson string username: username. **[required]**
    :reqjson string password: password. **[required]**
    :reqjson string base: base directory of target
    :reqjson bool encrypt: encrypt of access target

    :resjson object: :http:get:`/api/v1/target/(int:id)`

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "name": "testsite",
                "ipaddr": "127.0.0.1:5000",
                "username": "admin",
                "password": "admin",
                "base": "/"
            }' http://${QIP}:${QPORT}/api/v1/target/

    **Example response**

    .. sourcecode:: json

        {
            "base": "/",
            "desc": "",
            "encrypt": false,
            "id": 1,
            "ipaddr": "127.0.0.1:5000",
            "name": "testsite",
            "username": "admin"
        }
        
        
.. http:get:: /api/v1/target/

    List remote targets

    :resjson array object: :http:get:`/api/v1/target/(int:id)`

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/target/

    **Example response**

    .. sourcecode:: json

        [
            {
                "base": "/",
                "desc": "",
                "encrypt": false,
                "id": 1,
                "ipaddr": "127.0.0.1:5000",
                "name": "testsite",
                "username": "admin"
            }
        ]
        
        
.. http:get:: /api/v1/target/(int:id)/dirs/(string:path)

    List folder of target and backup records

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/target/(int:id)/dirs/

    **Example response**

    .. sourcecode:: json

        {
            "error": {
                "code": 503,
                "message": "Service Unabailable: 127.0.0.1"
            }
        }
        
        
.. http:get:: /api/v1/target/local/dirs/(string:path)

    List **local** folder of target and backup records

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/target/local/dirs/

    **Example response**

    .. sourcecode:: json

        [
            {
                "is_dir": true,
                "name": "test",
                "type": "d",
                "write": true
            }
        ]
        
        
.. http:get:: /api/v1/target/(int:id)

    Get a remote target

    :resjson int id: target ID
    :resjson string name: name.
    :resjson string ipaddr: ip address.
    :resjson string desc: description
    :resjson string username: username.
    :resjson string base: base directory of target
    :resjson bool encrypt: encrypt of access target

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/target/1

    **Example response**

    .. sourcecode:: json

        {
            "base": "/",
            "desc": "",
            "encrypt": false,
            "id": 1,
            "ipaddr": "127.0.0.1:5000",
            "name": "testsite",
            "username": "admin"
        }
        
        
.. http:get:: /api/v1/target/(int:id)/ping

    Test connection of remote target

    :resjson bool alive: alive of target

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/target/1/ping

    **Example response**

    .. sourcecode:: json

        {"alive": true}
        
        
.. http:put:: /api/v1/target/(int:id)

    Modify a remote target

    :resjson array object: :http:get:`/api/v1/target/(int:id)`

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt -d \
            '{
                "desc": "Hello World"
            }' http://${QIP}:${QPORT}/api/v1/target/1

    **Example response**

    .. sourcecode:: json

        {
            "base": "/",
            "desc": "Hello World",
            "encrypt": false,
            "id": 1,
            "ipaddr": "127.0.0.1:5000",
            "name": "testsite",
            "username": "admin"
        }
        
        
.. http:delete:: /api/v1/target/(int:id)

    Delete a remote target

    :resjson int array: target id

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/target/1

    **Example response**

    .. sourcecode:: json

        [1]
        
        
Backup
---------------------

.. http:post:: /api/v1/backup/

    Create a backup schedule

    :reqjson string job_name: backup job name **[required]**
    :reqjson string container_id: container ID **[required]**
    :reqjson string type: container type  **[required]**
    :reqjson object dest: **[required]**
    :reqjson string target: one of ``local``, ``remote``
    :reqjson string path: destination path to put backup file.
    :reqjson int profile: remote target ID
    :reqjson object at: **[required]**
    :reqjson string repeat: one of ``daily``, ``weekly``, ``monthly``, ``oneshot``. **[required]**
    :reqjson bool disable: do not schedule this job
    :reqjson int retention: from 2 to MAX_INT. 0 means unlimited. **[required]**
    :reqjson array features: the array must be in ``compress``, ``pause``.
    :reqjson object state:
    :reqjson string code: one of ``init``, ``scheduled``, ``waiting``, ``running``, ``completed``
    :reqjson int result: 0 means success
    :reqjson int last_run: last run this job
    :reqjson int next_run: next run this job
    :reqjson int progress: running progress [-1, 99]. -1 means no available progress.


    daily parameters

    :reqjson int start: time to start a task in seconds starting from 00:00.

    weekly parameters

    :reqjson int start: refer to previous definition
    :reqjson array days: array of week day from 0 (Sunday) to 6 (Saturday).

    monthly parameters

    :reqjson int start: refer to previous definition
    :reqjson array days: array of month day from 1 to 31.

    oneshot parameters

    :reqjson int start: epoch 

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "job_name": "LocalJob",
                "container_id": "utest",
                "type": "lxc",
                "dest": {"target": "local", "path": "/test/backup"},
                "at": {"repeat": "daily", "start": 60},
                "retention": 3
            }' http://${QIP}:${QPORT}/api/v1/backup/

    **Example response**

    .. sourcecode:: json

        {
            "at": {
                "repeat": "daily",
                "start": 60
            },
            "container_id": "utest",
            "dest": {
                "path": "/test/backup",
                "target": "local"
            },
            "disable": false,
            "features": [],
            "id": 1,
            "job_name": "LocalJob",
            "retention": 3,
            "state": {
                "code": "init",
                "next_run": "2015-03-18 01:00:00"
            },
            "type": "lxc"
        }
        
        
    Network backup

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "job_name": "RemoteJob",
                "container_id": "utest",
                "type": "lxc",
                "dest": {"target": "remote", "profile": 1, "path": "/test/backup"},
                "at": {"repeat": "daily", "times": 2, "start": 60},
                "features": ["compress"]
            }' http://${QIP}:${QPORT}/api/v1/backup/

    **Example response**

    .. sourcecode:: json

        {
            "at": {
                "repeat": "daily",
                "start": 60,
                "times": 2
            },
            "container_id": "utest",
            "dest": {
                "path": "/test/backup",
                "profile": 1,
                "target": "remote"
            },
            "disable": false,
            "features": [
                "compress"
            ],
            "id": 2,
            "job_name": "RemoteJob",
            "retention": 0,
            "state": {
                "code": "init",
                "next_run": "2015-03-18 01:00:00"
            },
            "type": "lxc"
        }
        
        
.. http:get:: /api/v1/backup/

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/backup/

    **Example response**

    .. sourcecode:: json

        [
            {
                "at": {
                    "repeat": "daily",
                    "start": 60
                },
                "container_id": "utest",
                "dest": {
                    "path": "/test/backup",
                    "target": "local"
                },
                "disable": false,
                "features": [],
                "id": 1,
                "job_name": "LocalJob",
                "retention": 3,
                "state": {
                    "code": "scheduled",
                    "next_run": "2015-03-18 01:00:00"
                },
                "type": "lxc"
            },
            {
                "at": {
                    "repeat": "daily",
                    "start": 60,
                    "times": 2
                },
                "container_id": "utest",
                "dest": {
                    "path": "/test/backup",
                    "profile": 1,
                    "target": "remote"
                },
                "disable": false,
                "features": [
                    "compress"
                ],
                "id": 2,
                "job_name": "RemoteJob",
                "retention": 0,
                "state": {
                    "code": "scheduled",
                    "next_run": "2015-03-18 01:00:00"
                },
                "type": "lxc"
            }
        ]
        
        
.. http:get:: /api/v1/backup/(int:id)

    Get a backup schedule

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/backup/1

    **Example response**

    .. sourcecode:: json

        {
            "at": {
                "repeat": "daily",
                "start": 60
            },
            "container_id": "utest",
            "dest": {
                "path": "/test/backup",
                "target": "local"
            },
            "disable": false,
            "features": [],
            "id": 1,
            "job_name": "LocalJob",
            "retention": 3,
            "state": {
                "code": "scheduled",
                "next_run": "2015-03-18 01:00:00"
            },
            "type": "lxc"
        }
        
        
.. http:put:: /api/v1/backup/(int:id)/run

    Run a backup schedule immediately

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/backup/1/run

    **Example response**

    .. sourcecode:: json

        {
            "at": {
                "repeat": "daily",
                "start": 60
            },
            "container_id": "utest",
            "dest": {
                "path": "/test/backup",
                "target": "local"
            },
            "disable": false,
            "features": [],
            "id": 1,
            "job_name": "LocalJob",
            "retention": 3,
            "state": {
                "code": "scheduled",
                "next_run": "2015-03-18 01:00:00"
            },
            "type": "lxc"
        }
        
        
.. http:put:: /api/v1/backup/(int:id)/stop

    Stop a backup schedule immediately

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/backup/1/stop

    **Example response**

    .. sourcecode:: json

        {
            "at": {
                "repeat": "daily",
                "start": 60
            },
            "container_id": "utest",
            "dest": {
                "path": "/test/backup",
                "target": "local"
            },
            "disable": false,
            "features": [],
            "id": 1,
            "job_name": "LocalJob",
            "retention": 3,
            "state": {
                "code": "scheduled",
                "last_run": "2015-03-17 17:27:06",
                "next_run": "2015-03-18 01:00:00"
            },
            "type": "lxc"
        }
        
        
.. http:put:: /api/v1/backup/(int:id)

    Modify a backup schedule

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt -d \
            '{
                "disable": true
            }' http://${QIP}:${QPORT}/api/v1/backup/1

    **Example response**

    .. sourcecode:: json

        {
            "at": {
                "repeat": "daily",
                "start": 60
            },
            "container_id": "utest",
            "dest": {
                "path": "/test/backup",
                "target": "local"
            },
            "disable": true,
            "features": [],
            "id": 1,
            "job_name": "LocalJob",
            "retention": 3,
            "state": {
                "code": "scheduled",
                "last_run": "2015-03-17 17:27:06",
                "next_run": "2015-03-18 01:00:00",
                "result": -2
            },
            "type": "lxc"
        }
        
        
.. http:delete:: /api/v1/backup/(int:id)

    Delete a backup task, which the task state must be ``init``, ``scheduled``, ``completed``

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/backup/1

    **Example response**

    .. sourcecode:: json

        [
            1
        ]
        
        
Restore
---------------------


.. http:post:: /api/v1/restore/

    Create a restore job

    :reqjson string job_name: restore job name **[required]**
    :reqjson string container_id: container ID **[required]**
    :reqjson string type: container type  **[required]**
    :reqjson object src: **[required]**
    :reqjson string target: one of ``local``, ``remote``
    :reqjson string path: destination path to put backup file.
    :reqjson string portfolio: 
    :reqjson bool disable: do not schedule this job
    :reqjson object state:
    :reqjson string code: one of ``init``, ``scheduled``, ``waiting``, ``running``, ``completed``
    :reqjson int result: 0 means success
    :reqjson int start: time of starting in epoch
    :reqjson int end: time of completion in epoch
    :reqjson int progress: running progress [-1, 99]. -1 means no available progress.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "job_name": "RestoreLocalJob",
                "container_id": "utest",
                "type": "lxc",
                "src": {"target": "local", "path": "/test/backup", "portfolio": "1"}
            }' http://${QIP}:${QPORT}/api/v1/restore/

    **Example response**

    .. sourcecode:: json

        {
            "container_id": "utest",
            "disable": false,
            "id": 1,
            "src": {
                "path": "/test/backup",
                "portfolio": "1",
                "target": "local"
            },
            "state": {
                "code": "init"
            },
            "type": "lxc"
        }
        
        
.. http:get:: /api/v1/restore/

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/restore/

    **Example response**

    .. sourcecode:: json

        [
            {
                "container_id": "utest",
                "disable": false,
                "id": 1,
                "src": {
                    "path": "/test/backup",
                    "portfolio": "1",
                    "target": "local"
                },
                "state": {
                    "code": "completed",
                    "last_run": "2015-03-17 17:27:07",
                    "result": 0
                },
                "type": "lxc"
            }
        ]
        
        
.. http:get:: /api/v1/restore/(int:id)

    Get a restore schedule

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/restore/1

    **Example response**

    .. sourcecode:: json

        {
            "container_id": "utest",
            "disable": false,
            "id": 1,
            "src": {
                "path": "/test/backup",
                "portfolio": "1",
                "target": "local"
            },
            "state": {
                "code": "completed",
                "last_run": "2015-03-17 17:27:07",
                "result": 0
            },
            "type": "lxc"
        }
        
        
.. http:put:: /api/v1/restore/(int:id)/stop

    Stop a restore task immediately

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/restore/1/stop

    **Example response**

    .. sourcecode:: json

        {
            "container_id": "utest",
            "disable": false,
            "id": 1,
            "src": {
                "path": "/test/backup",
                "portfolio": "1",
                "target": "local"
            },
            "state": {
                "code": "completed",
                "last_run": "2015-03-17 17:27:07",
                "result": 0
            },
            "type": "lxc"
        }
        
        
.. http:delete:: /api/v1/restore/(int:id)

    Delete a restore task, which the task state must be ``init``, ``scheduled``, ``completed``

    :resjson int id: task ID

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/restore/1

    **Example response**

    .. sourcecode:: json

        [
            1
        ]
        
        
Progress Changed
----------------------

.. http:get:: /api/v1/backup/progress

    It's a long polling that returns when progress changed of tasks. This method only returns **progress** changing.

    :resjson int id: task ID
    :resjson int progress: running progress [-1, 99]. -1 means no available progress.
    :resjson string type: ``backup``, ``restore``
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/backup/progress

    **Example response**

    .. sourcecode:: json

        []
        
        
