# You Will Like This Launcher (YWLTL)
# TODO mettre a jour automatiquement le launcher en prenant la derniere version sur github (pour eviter qu'on prenne 1 heure a mettre a jour pour jouer avec le houmous)

import os
import platform
from time import sleep
try:
    import customtkinter, certifi, portablemc, CTkMessagebox, CTkListbox, bs4, requests
except:
    print("Some modules are missing. Please install them using pip install -r requirements.txt")
    sleep(3)
"""
except:
    if platform.system() == "Windows":
        os.system("python -m pip install customtkinter certifi portablemc CTkMessageBox CTkListbox beautifulsoup4 requests")
    else:
        os.system("python3 -m pip install customtkinter certifi portablemc CTkMessageBox CTkListbox beautifulsoup4 requests")
    sys.exit()
"""
import customtkinter as ctk
import tkinter as tk
import CTkListbox
import SpinBox
import CurseForgeImplementations

def create():
    root = ctk.CTk()
    root.resizable(False, False)
    root.geometry('300x170')
    root.title("You Will Like This Launcher (YWLTL)")
    
    versionEntry = ctk.CTkEntry(root, placeholder_text="Version (par ex. 1.19.2)", width=140)
    versionEntry.place(y=50, x=5)

    ModLoader_var = customtkinter.StringVar(value='vanilla')
    ModLoader = customtkinter.CTkOptionMenu(root,values=['vanilla', 'forge', 'fabric', 'neoforge', 'legacyfabric', 'quilt'],
                                            width=140, height=28,
                                            variable=ModLoader_var)
    ModLoader.place(y=50, x=155)

    InstanceNameEntry = ctk.CTkEntry(root, placeholder_text='Le nom de ton instance de Minecraft')
    InstanceNameEntry.pack(fill="x", pady=10, padx=5)

    def doCreateInstanceBtn():
        instanceName = InstanceNameEntry.get()
        version = versionEntry.get()
        modLoader = ModLoader_var.get()
        controller = controllerSwitch_var.get()

        if os.path.exists(os.path.join(".", "Instances", instanceName)):
            CTkMessagebox.CTkMessagebox(title='Attention !', message="Tu ne peux pas créer d'instance avec ce nom car il existe déjà une instance avec celui-ci !", option_1='AH', icon="warning")
        else:
            createInstanceBtn(version, modLoader, instanceName, controller)
    def createInstanceBtn(version, loaders, name, controller):
        if name == '' or version == '':
            CTkMessagebox.CTkMessagebox(title='Attention !', message='Remplis toutes les informations avant de cliquer ici !', option_1='OK', icon="warning")
        else:
            root.destroy()
            if loaders == 'vanilla':
                loader = ''
            else:
                loader = loaders + ":"
            if platform.system() == "Windows":
                basecmd = "python -m portablemc"
            else:
                basecmd = "python3 -m portablemc"
            os.system(basecmd + " --main-dir " + os.path.join("Instances", ".MC") + " --work-dir " + os.path.join("Instances", name) + " start " + loader + version + " --dry")
            with open(os.path.join("Instances", name, "infos.txt"), "w+") as f:
                f.write(loader + version)
                f.close()
            if not loaders == 'vanilla':
                os.mkdir(os.path.join(".", "Instances", name, "mods"))
                if controller == 'on':
                    controllerImplementation = CurseForgeImplementations.CFimpl(version, loaders, name)
                    controllerImplementation.Window()
            main()
    createInstanceButton = ctk.CTkButton(root, text="Créer !", width=290, command=doCreateInstanceBtn)
    createInstanceButton.place(y=100, x=5)

    controllerSwitch_var = customtkinter.StringVar(value="off")
    controllerSwitch = ctk.CTkSwitch(root, text="Support de la manette", variable=controllerSwitch_var, onvalue="on", offvalue="off")
    controllerSwitch.place(y=135, x=70)

    root.mainloop()

def main():
    if not os.path.exists(os.path.join(".", "Instances")):
        os.mkdir(os.path.join(".", "Instances"))

    root = ctk.CTk()
    root.resizable(False, False)
    root.geometry('300x350')
    root.title("You Will Like This Launcher (YWLTL)")

    usernameEntry = ctk.CTkEntry(root, placeholder_text="Pseudonyme")
    usernameEntry.pack(fill="x", pady=10, padx=5)

    def createInstance():
        root.destroy()
        create()
    createInstanceButton = ctk.CTkButton(root, text="Créer Une instance", command=createInstance)
    createInstanceButton.pack(fill="x", padx=5, pady=5)

    listbox = CTkListbox.CTkListbox(root)
    listbox.pack(fill="both", padx=5, pady=10)
    dirs = os.listdir(os.path.join(".", "Instances"))
    dirs = [x for x in dirs if x != ".MC"]
    for elem in dirs:
        listbox.insert("end", elem)

    def launch():
        if not listbox.get():
            CTkMessagebox.CTkMessagebox(title='Attention !', message='Selectionne une instance !', option_1="Ah oui, c'est vrai...", icon="warning")
        else:
            with open(os.path.join(".", "UsernameSaver.txt"), "w") as f:
                f.write(usernameEntry.get())
                f.close()
            if platform.system() == "Windows":
                basecmd = "python -m portablemc"
            else:
                basecmd = "python3 -m portablemc"
            if usernameEntry.get() == '':
                CTkMessagebox.CTkMessagebox(title='Heuuuh...', message="Tu n'as pas de pseudonyme ?", option_1="Mais si !", icon="question")
            else:
                with open(os.path.join("Instances", listbox.get(), "infos.txt"), "r+") as f:
                    information = f.read()
                    f.close()
                ram = float(ramSpinbox.entry.get()) * 1024
                ram = str(ram).replace(".0", "")
                os.system(basecmd + " --main-dir " + os.path.join("Instances", ".MC") + " --work-dir " + os.path.join("Instances", listbox.get()) + " start " + information + " -u" + usernameEntry.get() + ' --jvm-args="-Xmx' + ram + 'M"')
    LaunchButton = ctk.CTkButton(root, text="Lancer l'instance selectionnée", command=launch)
    LaunchButton.pack(fill="x", padx=5, pady=5)

    ramLabel = ctk.CTkLabel(root, text="Mémoire vive allouée au jeu (En Giga-Octets)")
    ramLabel.pack(fill="x", padx=5, pady=2)

    ramSpinbox = SpinBox.FloatSpinbox(master=root, step_size=0.5)
    ramSpinbox.pack(fill="x", padx=5, pady=5)

    if not os.path.exists(os.path.join(".", "UsernameSaver.txt")):
        with open((os.path.join(".", "UsernameSaver.txt")), "x") as f:
            f.close()
    else:
        with open(os.path.join(".", "UsernameSaver.txt"), "r") as f:
            usernameEntry.insert(0, f.readlines(1))
            usernameEntry.configure(state="disabled")
            f.close()
    root.mainloop()

if __name__ == "__main__":
    main()