import customtkinter as ctk
import platform
import yaml
import os
import subprocess
import CTkMessagebox
import tkinter

class CFimpl :
    """
    Version need to be a valid minecraft version
    Loader need to be equal to a loader in that list : "Forge", "Fabric", "Quilt", "NeoForge"
    """
    def __init__(self, Version:str, Loader:str):
        self.Version = Version
        self.Loader = Loader

        self.Controlify = f"https://www.curseforge.com/minecraft/mc-mods/controlify"
        self.MidnightControls = f"https://www.curseforge.com/minecraft/mc-mods/midnightcontrols"
        self.Controllable_Fo = f"https://www.curseforge.com/minecraft/mc-mods/controllable"
        self.Controllable_Fa = f"https://www.curseforge.com/minecraft/mc-mods/controllable-fabric"

        self.Framework = f"https://www.curseforge.com/minecraft/mc-mods/framework"
        self.MidnightLib = f"https://www.curseforge.com/minecraft/mc-mods/midnightlib"
        
    def Window(self):
        """
        open the window
        """

        root = ctk.CTk()
        root.title("Implementer une manette")
        root.geometry("600x380")

        instructionsLabel = ctk.CTkLabel(root, text="Texte a re-travailer...",
        wraplength=390)
        instructionsLabel.pack(pady=6, padx=5)

        SelectedControllerModvar = tkinter.StringVar(value=None)
        SelectedControllerMod_Controlify = ctk.CTkRadioButton(root, text="Controlify", value="Controlify", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")
        SelectedControllerMod_MidnightControls = ctk.CTkRadioButton(root, text="MidnightControls", value="MidnightControls", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")
        SelectedControllerMod_Controllable_Fo = ctk.CTkRadioButton(root, text="Controllable (Forge)", value="Controllable_Fo", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")
        SelectedControllerMod_Controllable_Fa = ctk.CTkRadioButton(root, text="Controllable (Fabric)", value="Controllable_Fa", variable=SelectedControllerModvar).pack(pady=5, padx=5, fill="x")

        finiButton = ctk.CTkButton(root, text="Fini !", command=lambda:root.destroy())
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
    
if __name__ == "__main__":
    controllerImplementation = CFimpl("1.19.4", "Fabric")
    controllerImplementation.Window()