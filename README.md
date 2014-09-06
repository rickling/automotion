tesla-motion
============

First, install BLPAPI:

    env BLPAPI_ROOT=blpapi/cpp/Darwin python setup.py install --user

To start the server, run:

    env DYLD_LIBRARY_PATH=blpapi/cpp/Darwin python leap-tesla/server.py
