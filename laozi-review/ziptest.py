# import os
import zipfile
import subprocess

archpath = '\\\metrolx01\\backup\\jxk5224\\_tmp\\laozi\\test\\'
archname = 'test.zip'
fullpath = archpath + archname
testzip = zipfile.ZipFile(fullpath, 'w')
portazip = '7-Zip\\7z.exe'


def sevenzip(filename, zipname):
    """Takes path for filename, name of archive for zipname, and
    runs 7zip to compress."""
    system = subprocess.Popen([portazip, "a", zipname, filename])
    return(system.communicate())


sevenzip(archpath, archname)
