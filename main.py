#!/usr/bin/python3
import os,sys,json
while 1:
    try:
        i=os.path.normpath(os.path.expanduser(input("Input folder: ")))
        if not os.path.exists(o) or not os.path.isdir(o):raise TypeError
        os.chdir(i)
        break
    except:print("Cannot change directory, try again.")
if not "assets" in os.listdir(os.getcwd()):
    print("Cannot find assets folder, not a .minecraft directory?")
    sys.exit(1)
if len(os.listdir(os.path.join(os.getcwd(),"assets","indexes")))==0:
    print("Cannot find any hash description file, Minecraft never launched?")
    sys.exit(1)
elif len(os.listdir(os.getcwd()+os.sep+"assets"+os.sep+"indexes"))==1:
    try:objects=json.load(open(os.listdir(os.path.join(os.getcwd(),"assets",
                                                       "indexes")[0])))
    except:
        print("Hash description file is not valid JSON, refusing to read it.")
        sys.exit(1)
elif len(os.listdir(os.getcwd()+os.sep+"assets"+os.sep+"indexes"))>1:
    print("Multiple versions detected, select one:")
    for j,k in zip(os.listdir(os.getcwd()+os.sep+"assets"+os.sep+"indexes"),
                   range(0,len(os.listdir(os.path.join(os.getcwd(),"assets","indexes")))):
        print(str(k+1)+". "+j)
        while 1:
            try:
                l=int(input("version number: "))
                if l not in range(1,k):raise TypeError
                break
            except:print("Number invalid, try again.")
    try:objects=json.load(open(j[l-1]))
    except:
        print("Hash description file is not valid JSON, refusing to read it.")
        sys.exit(1)
while 1:
    try:
        o=os.path.normpath(os.path.expanduser(input("Output folder: ")))
        if not os.path.exists(o) or not os.path.isdir(o):raise TypeError
        os.chdir(os.path.abspath(o))
        os.chdir(os.path.abspath(os.join(i,"assets","objects")))
        break
    except:print("Cannot change directory, try again.")
objects=objects.objects
fails=[]
for j in objects:
    print(objects[j].hash+" >> "+os.path.join(os.path.abspath(o),j)+" ...",end="")
    try:
        os.chdir(os.path.join(i,"assets","objects"))
        os.makedirs(os.path.join(o,os.path.dirname(j)))
        in=open(os.path.join(objects[j].hash[:2],objects[j].hash))
        out=open(os.path.join(o,j),"w")
        out.write(in.read())
        in.close()
        out.close()
        print("OK")
    except:
        print("FAIL")
        fails=fails+j
if len(fails)>0:
    print("There have been "+int(len(fails))+" failed operations.")
    if input("List them? (y/N): ").lower()=="y":
        for i,j in zip(fails,range(1,len(fails)):
            print(str(j)+". "+objects[i].hash+" >> "+j)
