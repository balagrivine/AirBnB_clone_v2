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

def do_pack():
    #create versions folder if it doesn't exist
    local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    archive_name = "web_static_().tgz".format(datetime.utcnow().strftime(time_format))
    local("tar -cvzf versions/{} web_static".format(archive_name))

    return os.path.join("versions", archive_name)
