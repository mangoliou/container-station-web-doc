Preference
============================


.. http:post:: /api/v1/preference/(string:key)

    :reqjson string value: set the value of key

    :resjson int id: primary key ID

    **Example request**

    .. sourcecode:: bash

        $ curl -XPOST -sq -b cookies.txt -d '{"value":"I am sphinx"}' \
            http://${QIP}:${QPORT}/api/v1/preference/doc_test

    **Example response**

    .. runcode:: json

        curl -XPOST -sq -b cookies.txt -d '{"value":"I am sphinx"}' http://${QIP}:${QPORT}/api/v1/preference/doc_test | python -mjson.tool;

.. http:get:: /api/v1/preference/

    :resjson string key-name: value

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/

    **Example response**

    .. runcode:: json

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/ | python -mjson.tool;

.. http:get:: /api/v1/preference/(string:key)

    :resjson string key-name: value

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/doc_test

    **Example response**

    .. runcode:: json

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/doc_test | python -mjson.tool;

.. http:put:: /api/v1/preference/(string:key)

    :reqjson string value: set the value of key

    :resjson bool result: true when success

    **Example request**

    .. sourcecode:: bash

        $ curl -XPUT -sq -b cookies.txt -d '{"value":"I am container station"}' \
            http://${QIP}:${QPORT}/api/v1/preference/doc_test
        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/doc_test

    **Example response**

    .. runcode:: json

        curl -XPUT -sq -b cookies.txt -d '{"value":"I am container station"}' http://${QIP}:${QPORT}/api/v1/preference/doc_test | python -mjson.tool;
        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/doc_test | python -mjson.tool;

.. http:delete:: /api/v1/preference/(string:key)

    **Example request**

    .. sourcecode:: bash

        $ curl -XDELETE -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/doc_test

    **Example response**

    .. runcode:: json

        curl -XDELETE -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/doc_test | python -mjson.tool;


Special preference settings
---------------------------

Default image folder
^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v1/preference/folder

    :resjson string folder: Get current image directory path

    **Example request**

    .. sourcecode:: bash

        $ curl -XGET -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/folder


.. http:put:: /api/v1/preference/folder

    :reqjson string path: New image directory

    **Example request**

    .. sourcecode:: bash

        $ curl -XPUT -sq -b cookies.txt -d '{"path":"/Public"}' \
            http://${QIP}:${QPORT}/api/v1/preference/folder

Network settings
^^^^^^^^^^^^^^^^

.. http:get:: /api/v1/preference/network

    :resjson string LXC_DHCP_MAX: DHCP Max
    :resjson string LXC_NETMASK: Netmask
    :resjson string LXC_ADDR: IP address
    :resjson string LXC_DHCP_RANGE: DHCP range
    :resjson string LXC_NETWORK: Network
    :resjson string LXC_BRIDGE: Bridge name

    **Example request**

    .. sourcecode:: bash

        $ curl -XGET -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/preference/network


.. http:put:: /api/v1/preference/network


    **Example request**

    .. sourcecode:: bash

        $ curl -XPUT -sq -b cookies.txt -d '{"LXC_NETWORK":"88.8.89.0/24"}' \
            http://${QIP}:${QPORT}/api/v1/preference/network

