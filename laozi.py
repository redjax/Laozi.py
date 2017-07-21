"""

This script will keep the archive folder cleaned up.

The general flow for backups should be this:

1. Batch script copies user folder to repository.
2. Laozi begins archiving
3. Once a week, run the flow:
    Create archives for un-archived folders
    Move unzipped folders that have an archived copy to "Holding"
    Move folders in "Holding" that are over 30 days old to "Delete"
    Delete folders in "Delete" that are older than 30 days

Script is a work in progress.
"""
import datetime
import os
import shutil
import zipfile
from distutils.dir_util import copy_tree
import sys

"""
For use without argv

servPath = "[ENTER SERVER PATH HERE]"
holdingPath = servPath + "[ENTER HOLDING FOLDER PATH HERE]"
deletePath = servPath + "[ENTER DELETE FOLDER PATH HERE]"
archivePath = servPath + "[ENTER ARCHIVE FOLDER PATH HERE]"
"""

"""
The terminology here may be a bit confusing. The servPath is essentially the
path to the folder on your system (server or local), which contains the
holding, delete, and archive paths. Even if you are not using this on a server,
you still need to give the script a location to clean.

I am thinking of changing this functionality to be more flexible, but for now,
the script looks for a folder that contains the "holding," "delete," and
"archive" paths.

TL;DR: put your path (local or remote) that has the 3 folders in it in
"servPath," and then pass the other folders as arguments to the script.
"""
servPath = ""  # Put the path with holding, delete, & archive here.
holdingPath = servPath + sys.argv[1]
deletePath = servPath + sys.argv[2]
archivePath = servPath + sys.argv[3]

print("Holding: " + holdingPath)
print("Delete: " + deletePath)
print("Archive: " + archivePath)


def main():
    """The main function that will run other functions with the input path."""
    input("Pause before archive_file runs...")
    archive_file(holdingPath)
    # makeZip(holdingPath)

    input("Pause before delete_file runs..." + deletePath)
    # Check the Delete folder first
    delete_file(deletePath)

    input("Pause before move_file runs..." + holdingPath)
    # Check the Holding folder next
    move_file(holdingPath)


def delete_file(delpath):
    """delete_file deletes ever file/directory of a certain age (cutoff)."""
    # Change this variable to delete files older than set:
    # days, minutes, seconds, hours, etc)
    # cutoff = datetime.timedelta(days=30)
    cutoff = datetime.timedelta(seconds=30)

    for dirpath, dirnames, filenames in os.walk(delpath):

        for file in filenames:
            print("Del Path: " + delpath)
            curpath = os.path.join(dirpath, file)
            file_modified = datetime.datetime.fromtimestamp(
                os.path.getmtime(curpath))

            if datetime.datetime.now() - file_modified > cutoff:
                os.remove(curpath)

        for dir in dirnames:
            print("Del Path: " + delpath)
            curpath = os.path.join(dirpath, dir)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(
                curpath))

            if datetime.datetime.now() - file_modified > cutoff:
                shutil.rmtree(curpath)


def move_file(path):
    """Move files to the deletePath for the delete_file function."""
    # >>>[[[MAKE THE FUNCTION CHECK FOR ZIP EXTENSION!!]]]<<<
    # cutoff = datetime.timedelta(days=30)
    cutoff = datetime.timedelta(seconds=30)
    archivefile = "archive" or "Archive"
    movefile = "Move" or "move"
    deletefile = "Delete" or "delete"

    for dirpath, dirnames, filenames in os.walk(path):
        print("Folder Path: " + path)

        for file in filenames:
            if (archivefile or movefile or deletefile) not in filenames:
                curpath = os.path.join(dirpath, file)
                file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(
                    curpath))

                if datetime.datetime.now() - file_modified > cutoff:
                    copy_tree(path, deletePath)
                    delete_file(path)

        for dir in dirnames:
            print("Dir Path: " + path)
            if (archivefile or movefile or deletefile) not in dirnames:
                curpath = os.path.join(dirpath, dir)
                file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(
                    curpath))

                if datetime.datetime.now() - file_modified > cutoff:
                    full_path = os.path.join(path, dir)
                    print(full_path)
                    shutil.move(full_path, deletePath)


def archive_file(path):
    """Create the zip archive for the path it is given."""
    # cutoff = datetime.timedelta(seconds=30)

    for name in os.listdir(path):

        if not os.path.isdir(os.path.join(path, name)):
            continue

        archive = os.path.join(path, name) + ".zip"
        print("Archive path:" + archive)  # This path is correct
        cwd = os.getcwd()
        print("Current working directory:" + cwd)  # This path is the problem.

        with zipfile.ZipFile(archive, 'w') as zip:
            full_path = os.path.join(path, name)
            zip.write(full_path, name)


main()
