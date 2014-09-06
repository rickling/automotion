tesla-motion
============

First, install BLPAPI:

    cd blpapi && env BLPAPI_ROOT=./cpp python setup.py install --user

You'll need to load the VPN configuration for the Bloomberg API on your own. It
should expose the server on 10.8.8.1:8194.

To start the server, run:

    env DYLD_LIBRARY_PATH=blpapi/cpp/Darwin python leap-tesla/server.py
