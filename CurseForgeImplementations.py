import customtkinter as ctk
import webbrowser
import requests
from bs4 import BeautifulSoup

class CFimpl :
    """
    Version need to be a valid minecraft version
    Loader need to be equal to a loader in that list : "forge", "fabric", "quilt", "neoforge"
    """
    def __init__(self, Version:str, Loader:str):
        self.Version = Version
        self.Loader = Loader
        self.LoaderNmbr = None
        
        match self.Loader:
            case "fabric":
                self.LoaderNmbr = 4
            case "quilt":
                self.LoaderNmbr = 5
            case "neoforge":
                self.LoaderNmbr = 6
            case "forge":
                self.LoaderNmbr = 1
            case _:
                self.LoaderNmbr = None

        self.Controlify = f"https://www.curseforge.com/minecraft/mc-mods/controlify/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"
        self.MidnightControls = f"https://www.curseforge.com/minecraft/mc-mods/midnightcontrols/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"

        self.Controllable_Fo = f"https://www.curseforge.com/minecraft/mc-mods/controllable/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"
        self.Controllable_Fa = f"https://www.curseforge.com/minecraft/mc-mods/controllable-fabric/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"
        self.Framework = f"https://www.curseforge.com/minecraft/mc-mods/framework/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"
        
        self.Options = {"Controlify (1.19.4 -> latest)": self.Controlify,
                   "MidnightControls (1.18 -> latest)": self.MidnightControls,
                   "Controllable for Forge (1.12.2 -> 1.20.1)": self.Controllable_Fo,
                   "Controllable for Fabric (1.19.4 , 1.20.1)": self.Controllable_Fa,
                   "Framework API for Controllables": self.Framework}

    def Window(self):
        """
        open the window
        """

        root = ctk.CTk()
        root.title("Implementer une manette")
        root.geometry("400x300")

        instructionsLabel = ctk.CTkLabel(root, text="Clique sur le mod adapté, telecharge une version, puis glisse le fichier téléchargé dans le dossier 'mods' de l'instance souhaité.",
        wraplength=390)
        instructionsLabel.pack(pady=6, padx=5)

        for k, i in self.Options.items():
            ctk.CTkButton(root, text=k, command=lambda url=i: webbrowser.open(url)).pack(fill="x", pady=5, padx=5)
        
        finiButton = ctk.CTkButton(root, text="Fini !", command=lambda:root.destroy())
        finiButton.pack(pady=10, padx=5)

        root.mainloop()

if __name__ == "__main__":
    controllerImplementation = CFimpl("1.19.4", "forge")
    controllerImplementation.Window()