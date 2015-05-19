Application
===================


Template
------------------

.. http:get:: /api/v1/template

    List all application template information. 

    :param filter_text: (optional) filter application by name and description

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
              "http://${QIP}:${QPORT}/api/v1/template"

    **Example response**

    .. sourcecode:: json

        [
            {
                "arch": "amd64",
                "category": "application",
                "description": "Dockerized gitlab web server.",
                "from": "application",
                "icon": "http://download.qnap.com/QPKG/images/QPKG/container/gitlab_icon.png",
                "location": "https://registry.hub.docker.com/u/sameersbn/gitlab/",
                "name": "gitlab",
                "repository": "dockerhub",
                "title": "GitLab",
                "type": "app",
                "version": "7.10.4"
            },
            {
                "arch": "amd64",
                "category": "application",
                "description": "Dockerized redmine app server.",
                "from": "application",
                "icon": "http://download.qnap.com/QPKG/images/QPKG/container/redmine_icon.png",
                "location": "https://registry.hub.docker.com/u/sameersbn/redmine/",
                "name": "redmine",
                "repository": "dockerhub",
                "title": "Redmine",
                "type": "app",
                "version": "3.0.3"
            }
        ]
        
        
.. http:get:: /api/v1/template/(string:application)/description

    Get application full description with markdown format.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/template/gitlab/description"

    **Example response**

    .. sourcecode:: text

        GitLab with PostgrSQL + Redis
        =============================
        
        ## System requirements
        Recommend 2GB of RAM for your Host and 2 Cores for best performance!
        
        ## Setup
        The values of environemental variables for both PostgreSQL and GitLab need to match. The Keys cannot change. Also, the aliases used in the links to Redis and Posatgres from GHitLab cannot change.
        
        If the GitLab service does not start up, try the **Rebuild App** function on the application details page to kick start it. Watch the journal for output.
        
        To view the GUI after launching the template, browse to http://NAS_IP:10080.
        
        ## Running
        __NOTE__: Please allow a few minutes for the GitLab service to start. Watch the journal output for the message:
        
        `Checking GitLab ... Finished`
        
        Login using the default username and password:
        
        username: **root**
        
        password: **5iveL!fe**
        
        
.. http:get:: /api/v1/template/(string:application)/definition

    Get application full YAML definition.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/template/gitlab/definition"

    **Example response**

    .. sourcecode:: json

        {
            "gitlab": {
                "environment": [
                    "GITLAB_PORT=10080",
                    "GITLAB_SSH_PORT=10022"
                ],
                "image": "sameersbn/gitlab:7.10.4",
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
                    "DB_PASS=password",
                    "DB_NAME=gitlabhq_production"
                ],
                "image": "sameersbn/postgresql:9.4"
            },
            "redis": {
                "image": "sameersbn/redis:latest"
            }
        }
        
        
.. http:post:: /api/v1/template/(string:application)/pull

    Pulls images for containers.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/template/redmine/pull"

    **Example response**

    .. sourcecode:: json

        {}
        
        
.. http:get:: /api/v1/template/(string:application)/(string:lang)/wizard

    Read the wizard config file, and return html tags of each step and language tags (default: english).

    :param application: Application name
    :param lang: Wizard language

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/template/gitlab/eng/wizard"

    **Example response**

    .. sourcecode:: json

        {
            "app": {
                "entry": {
                    "port": "app.gitlab.ports.80"
                },
                "type": "web"
            },
            "env": {
                "gitlab": {
                    "environment": {
                        "GITLAB_HOST": "custom.host",
                        "GITLAB_PORT": "app.gitlab.ports.80",
                        "GITLAB_SSH_PORT": "app.gitlab.ports.22"
                    }
                }
            },
            "html": [
                "<div class=\"step1\">\n    <div class=\"step_title\">\n    {{'CONFIGURE_GITLAB' | translate}}\n    </div>\n    <form class=\"form-horizontal items\">\n        <div class=\"form-group item_desc\">\n        {{'GITLAB_PASSWORD_DESC' | translate}}\n        </div>\n        <div class=\"form-group\">\n            <label class=\"col-sm-2 control-label\">\n            {{'PASSWORD' | translate}}\n            </label>\n<input type=\"text\" class=\"col-sm-10\" name=\"app.gitlab.environment.GITLAB_ROOT_PASSWORD\" ng-model=\"app.gitlab.environment.GITLAB_ROOT_PASSWORD\" ngMinlength=\"2\" ngMaxlength=\"10\">\n        </div>\n        <div class=\"form-group item_desc\">\n        {{'GITLAB_WEB_HOST_PORT_DESC' | translate}}\n        </div>\n        <div class=\"form-group\">\n            <label class=\"col-sm-2 control-label\">\n            {{'PORT' | translate}}\n            </label>\n<input type=\"text\" class=\"col-sm-10\" name=\"app.gitlab.ports['80']\" ng-model=\"app.gitlab.ports['80']\">\n        </div>\n        <div class=\"form-group item_desc\">\n        {{'GITLAB_SSH_HOST_PORT_DESC' | translate}}\n        </div>\n        <div class=\"form-group\">\n            <label class=\"col-sm-2 control-label\">\n            {{'PORT' | translate}}\n            </label>\n<input type=\"text\" class=\"col-sm-10\" name=\"app.gitlab.ports['22']\" ng-model=\"app.gitlab.ports['22']\">\n        </div>\n    </form>\n</div>\n",
                "<div class=\"step2\">\n    <div class=\"step_title\">\n    {{'SERVICE_MANAGEMENT' | translate}}\n    </div>\n    <form class=\"form-horizontal items\">\n        <div class=\"form-group item_desc\">\n        \n        </div>\n        <div class=\"form-group\">\n            <label class=\"col-sm-2 control-label\">\n            {{'START_ONBOOT' | translate}}\n            </label>\n            <input type=\"checkbox\" ng-model=\"custom.autostart\">        </div>\n        <div class=\"form-group item_desc\">\n        \n        </div>\n        <div class=\"form-group\">\n            <label class=\"col-sm-2 control-label\">\n            {{'SERVICE_ENTRY' | translate}}\n            </label>\n<input type=\"text\" class=\"col-sm-10\" name=\"custom.entrypoint\" ng-model=\"custom.entrypoint\">\n        </div>\n    </form>\n</div>\n"
            ],
            "lang": {
                "CONFIGURE_GITLAB": "Configure Gitlab",
                "CONTEXT_PATH": "Context path",
                "GITLAB_PASSWORD_DESC": "The password for the root user. Defaults to 5iveL!fe.",
                "GITLAB_SSH_HOST_PORT_DESC": "The ssh port number. Defaults to 22.",
                "GITLAB_WEB_HOST_PORT_DESC": "The port of the GitLab server. Defaults to 80.",
                "PASSWORD": "Password",
                "PORT": "Port",
                "SERVICE_ENTRY": "Service entrypoint",
                "SERVICE_MANAGEMENT": "Service Management",
                "SERVICE_URL": "Service URL",
                "START_ONBOOT": "Start on boot"
            },
            "status": "success",
            "total_steps": 2
        }
        
        
User's application
------------------

.. http:post:: /api/v1/apps

    Create and start containers.

    :reqjson string template: Application name
    :reqjson string name: Custom application name
    :reqjson boolean autostart: Start application when container-station started
    :reqjson string virtual_path: Start application when container-station started
    :reqjson string port: 
    :reqjson object definition: Application definition

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "custom": {
                    "name": "test",
                    "autostart": true,
                    "virtual_path": "redmine",
                    "port": "5555",
                    "template": "redmine"
                },
                "definition": {
                    "postgresql": {
                        "environment": [
                            "DB_USER=redmine",
                            "DB_PASS=redminewooo",
                            "DB_NAME=myredmine"
                        ],
                        "image": "sameersbn/postgresql:9.4"
                    },
                    "redmine": {
                        "environment": [
                            "DB_USER=redmine",
                            "DB_PASS=redminewooo",
                            "DB_NAME=myredmine"
                        ],
                        "image": "sameersbn/redmine:3.0.2",
                        "links": [
                            "postgresql:postgresql"
                        ],
                        "ports": [
                            "22234:80"
                        ]
                    }
                }
            }' http://${QIP}:${QPORT}/api/v1/apps


    **Example response**

    .. sourcecode:: json

        [
            "test_postgresql_1",
            "test_redmine_1"
        ]
        
        
.. http:get:: /api/v1/apps

    List all custom application information.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/apps"

    **Example response**

    .. sourcecode:: json

        {
            "test": [
                "redmine",
                "postgresql"
            ]
        }
        
        
.. http:get:: /api/v1/apps/(string:name)/definition

    Get custom application definition.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test/definition"

    **Example response**

    .. sourcecode:: json

        {
            "postgresql": {
                "environment": [
                    "DB_USER=redmine",
                    "DB_PASS=redminewooo",
                    "DB_NAME=myredmine"
                ],
                "image": "sameersbn/postgresql:9.4"
            },
            "redmine": {
                "environment": [
                    "DB_USER=redmine",
                    "DB_PASS=redminewooo",
                    "DB_NAME=myredmine"
                ],
                "image": "sameersbn/redmine:3.0.2",
                "links": [
                    "postgresql:postgresql"
                ],
                "ports": [
                    "22234:80"
                ]
            }
        }
        
        
.. http:get:: /api/v1/apps/(string:name)

    Get custom application information.

    :param name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test"

    **Example response**

    .. sourcecode:: json

        {
            "custom": {
                "autostart": true,
                "name": "test",
                "port": "5555",
                "template": "redmine",
                "virtual_path": "redmine"
            },
            "definition": {
                "postgresql": {
                    "environment": [
                        "DB_USER=redmine",
                        "DB_PASS=redminewooo",
                        "DB_NAME=myredmine"
                    ],
                    "image": "sameersbn/postgresql:9.4"
                },
                "redmine": {
                    "environment": [
                        "DB_USER=redmine",
                        "DB_PASS=redminewooo",
                        "DB_NAME=myredmine"
                    ],
                    "image": "sameersbn/redmine:3.0.2",
                    "links": [
                        "postgresql:postgresql"
                    ],
                    "ports": [
                        "22234:80"
                    ]
                }
            }
        }
        
        
.. http:put:: /api/v1/apps/(string:name)/restart

    Restart running application.

    :param name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test/restart"

    **Example response**

    .. sourcecode:: json

        Failed to run command
        curl -sq -XPUT -b cookies.txt     "http://${QIP}:${QPORT}/api/v1/apps/test/restart" | python -m json.tool
        
        
.. http:put:: /api/v1/apps/(string:name)/kill

    Force stop application containers.

    :param name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test/kill"

    **Example response**

    .. sourcecode:: json

        Failed to run command
        curl -sq -XPUT -b cookies.txt     "http://${QIP}:${QPORT}/api/v1/apps/test/kill" | python -m json.tool
        
        
.. http:put:: /api/v1/apps/(string:name)/start

    Start existing application.

    :param name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test/start"

    **Example response**

    .. sourcecode:: json

        Failed to run command
        curl -sq -XPUT -b cookies.txt     "http://${QIP}:${QPORT}/api/v1/apps/test/start" | python -m json.tool
        
        
.. http:put:: /api/v1/apps/(string:name)/stop

    Stop running application without removing them.

    :param name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test/stop"

    **Example response**

    .. sourcecode:: json

        Failed to run command
        curl -sq -XPUT -b cookies.txt     "http://${QIP}:${QPORT}/api/v1/apps/test/stop" | python -m json.tool
        
        
.. http:delete:: /api/v1/apps/(string:name)

    Remove stopped application containers.

    :param name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/apps/test"

    **Example response**

    .. sourcecode:: json

        Failed to run command
        curl -sq -XDELETE -b cookies.txt     "http://${QIP}:${QPORT}/api/v1/apps/test" | python -m json.tool
        
        
