import os
import zipfile
import jsonops


def createZip():
    jsonops.readjson('args.json')

    archpath = (jsonops.getarg('args.json', 'metrolx')
                + jsonops.getarg('args.json', 'backupfolder'))
    archname = 'test.zip'
    fullpath = archpath + archname
    testzip = zipfile.ZipFile(fullpath, 'w')

    for folder, subfolders, files in os.walk(archpath):

        for file in files:
            testzip.write(os.path.join(folder, file), os.path.relpath(
                            os.path.join(folder, file),
                            archpath), compress_type=zipfile.ZIP_DEFLATED)

    testzip.close
