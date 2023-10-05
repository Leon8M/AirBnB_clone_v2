#!/usr/bin/python3
from fabric.api import local
from time import strftime


def do_pack():
    """A script that generates an archive of the contents of the web_static folder."""
    try:
        current_time = strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(current_time))

        return "versions/web_static_{}.tgz".format(current_time)

    except Exception as e:
        return None
