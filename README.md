# Laozi.py

---

#### _According to traditional accounts, Laozi was a scholar who worked as the Keeper of the Archives for the royal court of Zhou._ - [Wikipedia](https://en.wikipedia.org/wiki/Laozi)

---

Laozi.py is a personal project of mine, meant to help me learn more about Python while also accomplishing an organizational function. This started out as an internal script I use for work, organizing folders on a server of ours, but I figured it might be useful for organization on people's computers/servers.

The script looks for 3 folders within a user-specified path. They can be named whatever you want, but the ideas behind the 3 folders are an "Archive" folder, a "Holding" folder, and a "Delete" folder. The script runs through these 3 folders each time it runs, and performs a function on whatever files are in those folders. The breakdown of the folders is as follows:

* Archive - Holds the .ZIP (for now, the only available archive format I have implemented) file(s).

* Holding - This is kind of the "working" folder. Items in the holding folder have not been touched by the script yet. When the script runs, it will check the files to see if they are older than the user-specified time (default 30 days *(currently 30 seconds, will fix in a later release)*). If the files are older than the specified time, they will be archived into a .ZIP file and moved to , and the original file/folder will be moved to the "Delete" folder, to be deleted on the next run.

* Delete - One of the most aptly named things I have ever created, the Delete folder holds files moved from Holding, and each pass of the script will delete anything older than a specified period of time.

The script can be scheduled to run, and takes arguments for simplicity...so you change the servPath variable in the script to the path of the folder that contains the sub-folders, and then simply pass the sub folder names as arguments in the script.

###### _I will eventually go more in depth here, but I think the script is fairly simple and self-explanatory. There are still some things that need to be worked out, such as making sure the arguments the script takes are valid, moving .ZIP files to the Archive folder (I had quite a bit of trouble with this, and need to revisit it), and seeing how it works as a scheduled job. I may also eventually write in Python 2.x compatibility._
