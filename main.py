#!/usr/bin/python3
import os
import sys
import json
while 1:
    try:
        i = os.path.normpath(os.path.expanduser(input("Input folder: ")))
        # if not os.path.exists(o) or not os.path.isdir(o):raise TypeError
        os.chdir(i)
        break
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print("Cannot change directory, try again.")
if "assets" not in os.listdir(os.getcwd()):
    print("Cannot find assets folder, not a .minecraft directory?")
    sys.exit(1)
if len(os.listdir(os.path.join(os.getcwd(), "assets", "indexes"))) == 0:
    print("Cannot find any hash description file, Minecraft never launched?")
    sys.exit(1)
elif len(os.listdir(os.getcwd()+os.sep+"assets"+os.sep+"indexes")) == 1:
    try:
        objects = json.load(open(os.listdir(os.path.join(os.getcwd(), "assets",
                                                         "indexes")[0])))
    except:
        print("Hash description file is not valid JSON, refusing to read it.")
        sys.exit(1)
elif len(os.listdir(os.getcwd()+os.sep+"assets"+os.sep+"indexes")) > 1:
    print("Multiple versions detected, select one:")
    for j, k in zip(os.listdir(os.path.join(os.getcwd(), "assets", "indexes")),
                    range(0, len(os.listdir(os.path.join(
                       os.getcwd(), "assets", "indexes"))))):
        print(str(k+1)+". "+j)
    while 1:
        try:
            l = int(input("version number (1~"+str(k+1)+"): "))
            if l not in range(0, k+2):
                raise TypeError
            break
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            print("Number invalid, try again.")
    objects = json.load(open(os.path.join(
        os.getcwd(), "assets", "indexes",
        os.listdir(os.path.join(os.getcwd(), "assets", "indexes"))[l-1])))
    # except:
    #    print("Hash description file is not valid JSON, refusing to read it.")
    #    sys.exit(1)
while 1:
    try:
        o = os.path.normpath(os.path.expanduser(input("Output folder: ")))
        if not os.path.exists(o) or not os.path.isdir(o):
            raise TypeError
        os.chdir(os.path.abspath(o))
        os.chdir(os.path.abspath(os.path.join(i, "assets", "objects")))
        break
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print("Cannot change directory, try again.")
objects = objects["objects"]
fails = []
for j in objects:
    print(objects[j]["hash"]+" >> "+os.path.join(
        os.path.abspath(o), j)+" ... ", end="")
    try:
        os.chdir(os.path.join(i, "assets", "objects"))
        try:
            os.makedirs(os.path.join(o, os.path.dirname(j)))
        except:
            pass
        os.popen("dd if="+os.path.join(objects[j]["hash"][0:2],
                                       objects[j]["hash"]) + " of=" +
                 os.path.join(o, j)+" 2>"+os.devnull).read()
        print("OK")
    except:
        print("FAIL")
        fails = fails + [j]
if len(fails) > 0:
    print("There have been "+str(len(fails))+" failed operations.")
    if input("List them? (y/N): ").lower() == "y":
        for i, j in zip(fails, range(1,len(fails))):
            print(str(j)+". "+objects[i]["hash"]+" >> "+j)
