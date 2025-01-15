import customtkinter as ctk
import platform
import yaml
import os
import subprocess
import CTkMessagebox
import tkinter
import shutil

class CFimpl :
    """
    Version need to be a valid minecraft version
    Loader need to be equal to a loader in that list : "Forge", "Fabric", "Quilt", "NeoForge"
    """
    def __init__(self, Version:str, Loader:str, InstanceName):
        self.Version = Version
        self.Loader = Loader
        self.InstanceName = InstanceName

        self.Controlify = f"https://www.curseforge.com/minecraft/mc-mods/controlify"
        self.MidnightControls = f"https://www.curseforge.com/minecraft/mc-mods/midnightcontrols"
        self.Controllable_Fo = f"https://www.curseforge.com/minecraft/mc-mods/controllable"
        self.Controllable_Fa = f"https://www.curseforge.com/minecraft/mc-mods/controllable-fabric"

        self.Framework = f"https://www.curseforge.com/minecraft/mc-mods/framework"
        self.MidnightLib = f"https://www.curseforge.com/minecraft/mc-mods/midnightlib"
        self.FabricAPI = f"https://www.curseforge.com/minecraft/mc-mods/fabric-api"

    def DownloadUtils(self, mod, window):
        match mod:
            case "Controlify":
                self.RMMUD(self.Loader, self.Version, self.Controlify)
                with open(os.path.join(".", "RMMUD", "latest.log"), "r+") as WarningDetect:
                    detect = True if "WARNING" in WarningDetect.read() else False
                    WarningDetect.close()
                if detect:
                    CTkMessagebox.CTkMessagebox(title='Erreur !', message="Le détecteur a detecté que ce mod n'est compatible avec ta version de minecraft. \nSelectionne un autre mod.", option_1='Je change ça !', icon="warning")
                else:
                    self.RMMUD(self.Loader, self.Version, self.FabricAPI)
                    window.destroy()
                    good = True
            case "MidnightControls":
                self.RMMUD(self.Loader, self.Version, self.MidnightControls)
                with open(os.path.join(".", "RMMUD", "latest.log"), "r+") as WarningDetect:
                    detect = True if "WARNING" in WarningDetect.read() else False
                    WarningDetect.close()
                if detect:
                    CTkMessagebox.CTkMessagebox(title='Erreur !', message="Le détecteur a detecté que ce mod n'est compatible avec ta version de minecraft. \nSelectionne un autre mod.", option_1='Je change ça !', icon="warning")
                else:
                    self.RMMUD(self.Loader, self.Version, self.MidnightLib)
                    self.RMMUD(self.Loader, self.Version, self.FabricAPI)
                    window.destroy()
                    good = True
            case "Controllable_Fo":
                self.RMMUD(self.Loader, self.Version, self.Controllable_Fo)
                with open(os.path.join(".", "RMMUD", "latest.log"), "r+") as WarningDetect:
                    detect = True if "WARNING" in WarningDetect.read() else False
                    WarningDetect.close()
                if detect:
                    CTkMessagebox.CTkMessagebox(title='Erreur !', message="Le détecteur a detecté que ce mod n'est compatible avec ta version de minecraft. \nSelectionne un autre mod.", option_1='Je change ça !', icon="warning")
                else:
                    self.RMMUD(self.Loader, self.Version, self.Framework)
                    window.destroy()
                    good = True
            case "Controllable_Fa":
                self.RMMUD(self.Loader, self.Version, self.Controllable_Fa)
                with open(os.path.join(".", "RMMUD", "latest.log"), "r+") as WarningDetect:
                    detect = True if "WARNING" in WarningDetect.read() else False
                    WarningDetect.close()
                if detect:
                    CTkMessagebox.CTkMessagebox(title='Erreur !', message="Le détecteur a detecté que ce mod n'est compatible avec ta version de minecraft. \nSelectionne un autre mod.", option_1='Je change ça !', icon="warning")
                else:
                    self.RMMUD(self.Loader, self.Version, self.Framework)
                    window.destroy()
                    good = True
            case _:
                CTkMessagebox.CTkMessagebox(title='Attention !', message="Tu n'as rien selectionné !", option_1='Aïe', icon="warning")
                good = False
        if good:
            for file in os.listdir(os.path.join('.','RMMUD', 'mods')):
                shutil.move(os.path.join('.','RMMUD', 'mods', file), os.path.join(".", "Instances", self.InstanceName, "mods"))
            shutil.rmtree(os.path.join(".", "RMMUD", "RMMUDDownloads"))

    def Window(self):
        """
        open the window
        """

        root = ctk.CTk()
        root.title("Implementer une manette")
        root.geometry("400x224")
        root.resizable(False, False)

        instructionsLabel = ctk.CTkLabel(root, text="Texte a re-travailer...",
        wraplength=390)
        instructionsLabel.pack(pady=6, padx=5)

        SelectedControllerModvar = tkinter.StringVar(value=None)
        SelectedControllerMod_Controlify = ctk.CTkRadioButton(root, text="Controlify", value="Controlify", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")
        SelectedControllerMod_MidnightControls = ctk.CTkRadioButton(root, text="MidnightControls", value="MidnightControls", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")
        SelectedControllerMod_Controllable_Fo = ctk.CTkRadioButton(root, text="Controllable (Forge)", value="Controllable_Fo", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")
        SelectedControllerMod_Controllable_Fa = ctk.CTkRadioButton(root, text="Controllable (Fabric)", value="Controllable_Fa", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")

        finiButton = ctk.CTkButton(root, text="Fini !", command=lambda:self.DownloadUtils(SelectedControllerModvar.get(), root))
        finiButton.pack(pady=10, padx=5)

        root.mainloop()

    def RMMUD(self, loader, version, mod_url):
        with open(os.path.join(".", "RMMUD", "RMMUDInstances", "config.yaml"), 'r') as file:
            data = yaml.safe_load(file)
            file.close()
        data['Loader'] = loader
        data['Version'] = version
        data['Mods'] = mod_url
        with open(os.path.join(".", "RMMUD", "RMMUDInstances", "config.yaml"), 'w') as file:
            yaml.dump(data, file)
            file.close()
        
        python = "python" if platform.system() == "Windows" else "python3"
        subprocess.run([python, "RMMUD.py"], cwd=os.path.join(".", "RMMUD"))
        with open(os.path.join(".", "RMMUD", "RMMUDInstances", "config.yaml"), 'w') as file:
            data['Enabled'] = "false"
            yaml.dump(data, file)
            file.close()       
    
if __name__ == "__main__":
    controllerImplementation = CFimpl("1.19.4", "Fabric", 'cacamoulox')
    controllerImplementation.Window()