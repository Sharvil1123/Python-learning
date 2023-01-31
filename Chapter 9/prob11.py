import os
oldname = "copythis.txt"
newname = "renamed_by_python"
with open(oldname) as f:
    k =f.read()
with open(newname,'w') as f:
    f.write(k)
os.remove(oldname)
