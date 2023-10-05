#!/usr/bin/python3
from fabric.api import put, run, env

env.hosts = ["100.25.220.119", "100.25.147.34"]


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web server
    """

    try:
        # Extracting file name without extension and creating path
        filename_ext = archive_path.split("/")[-1]
        filename = filename_ext.split(".")[0]
        remote_path = "/data/web_static/releases/{}/".format(filename)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Create the folder for the new version
        run('mkdir -p {}'.format(remote_path))

        # Uncompress the archive to the folder
        run('tar -xzf /tmp/{} -C {}'.format(filename_ext, remote_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename_ext))

        # Move the files from the extracted archive
        run('mv {}/web_static/* {}'.format(remote_path, remote_path))

        # Delete the symbolic link to the previous version
        run('rm -rf {}/web_static'.format(remote_path))

        # Create a new symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(remote_path))

        print('New version deployed!')
        return True

    except Exception as e:
        return False
