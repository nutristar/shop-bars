import sys, os
import shutil
# print((sys.argv))

X = "D:\P"
a=0
for path, dirs, files in os.walk(X):
    if a!=0:
        shutil.make_archive(f"output_filename{a}", 'zip', path)


    if a==10:
        break
    a+=1