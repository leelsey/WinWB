from winreg import *
from win32com.shell import shell

def appver():
    return "0.1"

def addRegistry(sdp_path):
    key = CreateKey(HKEY_LOCAL_MACHINE, sdp_path)
    try:
        SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
        print("-> Installed WinWD. (Add on Windows Registry.)")
    except EnvironmentError:
        envError()
    return key

def writeDisable(key):
    try:
        SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x1)
        print("-> Write blocking on. (Write is disabled now.)")
    except EnvironmentError:
        envError()

def writeAble(key):
    try:
        SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
        print("-> Write blocking off. (Write is able now.)")
    except EnvironmentError:
        envError()

def deleteRegistry(sdp_path):
    DeleteKey(HKEY_LOCAL_MACHINE, sdp_path)
    print("-> Removed WinWB. (Deleted on Windows Registry.)")

def envError():
    print("-> Encountered Environment Error")

def writeBlock():
    if shell.IsUserAnAdmin():
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        go = True
        key = addRegistry(sdp_path)  # key = None -> key = True<addRegistry>
        reins = "-> You need installed WinWB first. Please select \"3. Reinstall WinWB\" and retry."
        print(" _       ___     _       ______\n"
              "| |     / (_)___| |     / / __ )\n"
              "| | /| / / / __ \\ | /| / / __  |\n"
              "| |/ |/ / / / / / |/ |/ / /_/ /\n"
              "|__/|__/_/_/ /_/|__/|__/_____/\n"
              "\nWindows External Storage Write Blocker\n"
              "version: 0.1\n")
        while go:
            print("\nWhat kind of service do you want?\n"
                  "\t1. Write Blocker On\n"
                  "\t2. Write Blocker Off\n"
                  "\t3. Reinstall WinWB\n"
                  "\t4. Remove WinWB\n"
                  "\t5. Check Version\n"
                  "\t0. Quit")
            answer = input("Select command: ")
            if answer == "1":
                if key is not None:
                    writeDisable(key)
                else:
                    print(reins)
            elif answer == "2":
                if key is not None:
                    writeAble(key)
                else:
                    print(reins)
            elif answer == "3":
                key = addRegistry(sdp_path)
            elif answer == "4":
                try:
                    deleteRegistry(sdp_path)
                    key = None
                except FileNotFoundError:
                    print(reins)
            elif answer == "5":
                print("-> Version: " + appver())
            elif answer == "0" or answer == "exit" or answer == "quit":
                print("-> Bye!")
                go = False
            else:
                print("-> Please enter correct command.")
    else:
        print("Administrator permissions are required.\n"
              "Please retry after run as administration.")
        input("Press any key to continue...\n")

if __name__ == '__main__':
    writeBlock()
