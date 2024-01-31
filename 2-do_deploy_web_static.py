#!/usr/bin/python3


"""
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

Prototype: def do_pack():
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
    The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
"""

from fabric.api import local
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = [""]

def do_pack():
    #create versions folder if it doesn't exist
    local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    archive_name = "versions/web_static_().tgz".format(datetime.now().strftime(time_format))
    archived = local("tar -cvzf {} web_static".format(archive_name))

    if archived.return_code != 0:
        return None
    else:
        return archive_name

def do_deploy(archive_path):
    """Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:"""

    #return false if the archive paht does not exist
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format()a_path)
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return True
    return False
