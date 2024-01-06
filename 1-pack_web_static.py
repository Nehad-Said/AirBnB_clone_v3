#!/usr/bin/python3
"""
    Fabric file to archive the folder
"""


from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir


def do_pack():
    """ This generates a .tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None
