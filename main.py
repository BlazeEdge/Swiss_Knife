import eel
import os

eel.init("web")

@eel.expose
def shutdown():
    print("shutdown...")
    try:
        os.system("shutdown /f /s /t 20")
    except:
        pass

@eel.expose
def del_tmp():
    print("Deleting temp...")
    try:
        os.system("del %TMP% /s /q")
    except:
        pass

@eel.expose
def scan_disk():
    print("Scaning disk...")
    try:
        os.system("start cmd /k chkdsk")
    except:
        pass

eel.start("index.html", size=(400, 700), block=True)