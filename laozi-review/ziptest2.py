import os
import zipfile

archpath = '\\\metrolx01\\backup\\jxk5224\\_tmp\\laozi\\test\\'
archname = 'test.zip'
fullpath = archpath + archname
testzip = zipfile.ZipFile(fullpath, 'w')

for folder, subfolders, files in os.walk(archpath):

    for file in files:
        testzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), archpath), compress_type=zipfile.ZIP_DEFLATED)

testzip.close()
