# You Will Like This Launcher (YWLTL)
import os
import platform

try:
    import customtkinter, certifi, portablemc, CTkMessagebox, CTkListbox
except:
    if platform.system() == "Windows":
        os.system("python -m pip install customtkinter certifi portablemc CTkMessageBox CTkListbox")
    else:
        os.system("python3 -m pip install customtkinter certifi portablemc CTkMessageBox CTkListbox")
    import sys
    sys.exit()

import customtkinter as ctk
import tkinter as tk
import CTkListbox

def create():
    root = ctk.CTk()
    root.resizable(False, False)
    root.geometry('300x150')
    root.title("You Will Like This Launcher (YWLTL)")
    
    #versionEntry_var = ctk.StringVar(value='')
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
        if os.path.exists(os.path.join(".", "Instances", instanceName)):
            CTkMessagebox.CTkMessagebox(title='Attention !', message="Tu ne peux pas créer d'instance avec ce nom car il existe déjà une instance avec celui-ci !", option_1='AH', icon="warning")
        else:
            createInstanceBtn(version, modLoader, instanceName)
    def createInstanceBtn(version, loaders, name):
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
            main()
    createInstanceButton = ctk.CTkButton(root, text="Créer !", width=290, command=doCreateInstanceBtn)
    createInstanceButton.place(y=100, x=5)

    root.mainloop()

def main():
    if not os.path.exists(os.path.join(".", "Instances")):
        os.mkdir(os.path.join(".", "Instances"))

    root = ctk.CTk()
    root.resizable(False, False)
    root.geometry('300x270')
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
                os.system(basecmd + " --main-dir " + os.path.join("Instances", ".MC") + " --work-dir " + os.path.join("Instances", listbox.get()) + " start " + information + " -u" + usernameEntry.get())
    LaunchButton = ctk.CTkButton(root, text="Lancer l'instance selectionnée", command=launch)
    LaunchButton.pack(fill="x", padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()