Compose application
===================

 - `Docker Compose full document <https://docs.docker.com/compose/>`_ 
 - `Docker Compose Github <https://github.com/docker/compose>`_ 
 - `Docker Compose roadmap <https://github.com/docker/compose/blob/master/ROADMAP.md>`_ 

.. http:get:: /api/v1/compose/

   List all compose application information. 

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
              "http://${QIP}:${QPORT}/api/v1/compose/"

    **Example response**

    .. sourcecode:: json

        [
            {
                "description": "Dockerized gitlab web server",
                "id": 1,
                "image": "meersbn/postgresql:9.4, sameersbn/gitlab:7.8.2",
                "name": "gitlab",
                "source": "https://registry.hub.docker.com/u/sameersbn/gitlab/",
                "type": ""
            },
            {
                "description": "",
                "id": 2,
                "image": "sameersbn/postgresql:9.1-1, sameersbn/redmine:3.0.0",
                "name": "redmine",
                "source": "https://registry.hub.docker.com/u/sameersbn/redmine/",
                "type": ""
            }
        ]
        
        
.. http:get:: /api/v1/compose/(string:application)/description

    Get application full description with markdown format.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/description"

    **Example response**

    .. sourcecode:: text

        GitLab with PostgrSQL + Redis
        =======================
        
        ## System requirements
        Recommend 2GB of RAM for your Host and 2 Cores for best performance!
        
        ## Setup
        The values of environemental variables for both PostgreSQL and GitLab need to match. The Keys cannot change. Also, the aliases used in the links to Redis and Posatgres from GHitLab cannot change.
        
        If the GitLab service does not start up, try the **Rebuild App** function on the application details page to kick start it. Watch the journal for output.
        
        To view the GUI after launching the template, browse to http://panamax.local:10080.
        
        ## Running
        __NOTE__: Please allow a few minutes for the GitLab service to start. Watch the journal output for the message:
        
        `Checking GitLab ... Finished`
        
        Login using the default username and password:
        
        username: **root**
        
        password: **5iveL!fe**
        
        
.. http:get:: /api/v1/compose/(string:application)/define

    Get application full YAML definition.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/define"

    **Example response**

    .. sourcecode:: json

        {
            "gitlab": {
                "image": "sameersbn/gitlab:7.8.2",
                "links": [
                    "redis:redisio",
                    "postgresql:postgresql"
                ],
                "ports": [
                    "10080:80",
                    "10022:22"
                ]
            },
            "postgresql": {
                "environment": [
                    "DB_USER=gitlab",
                    "DB_PASS=secretpassword",
                    "DB_NAME=gitlabhq_production"
                ],
                "image": "sameersbn/postgresql:9.4"
            },
            "redis": {
                "image": "sameersbn/redis:latest"
            }
        }
        
        
.. http:post:: /api/v1/compose/(string:application)/pull

    Pulls images for containers.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/pull"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:post:: /api/v1/compose/up

    Create and start containers.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/up"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:post:: /api/v1/compose/restart

    Restart running application.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/restart"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:post:: /api/v1/compose/kill

    Force stop application containers.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/kill"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:post:: /api/v1/compose/start

    Start existing application.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/start"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:post:: /api/v1/compose/stop

    Stop running application without removing them.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/stop"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:post:: /api/v1/compose/rm

    Remove stopped application containers.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/rm"

    **Example response**

    .. sourcecode:: json

        {}
        
        
