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
        self.MidnightLib = f"https://www.curseforge.com/minecraft/mc-mods/midnightlib/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"

        self.Controllable_Fo = f"https://www.curseforge.com/minecraft/mc-mods/controllable/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"
        self.Controllable_Fa = f"https://www.curseforge.com/minecraft/mc-mods/controllable-fabric/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"
        self.Framework = f"https://www.curseforge.com/minecraft/mc-mods/framework/files/all?version={self.Version}&gameVersionTypeId={str(self.LoaderNmbr)}"

        self.Options = {"Controlify (1.19.4 -> latest)": self.Controlify,
                   "MidnightControls (1.18 -> latest)": self.MidnightControls,
                   "Controllable for Forge (1.12.2 -> 1.20.1)": self.Controllable_Fo,
                   "Controllable for Fabric (1.19.4 , 1.20.1)": self.Controllable_Fa,
                   "Framework API for Controllables": self.Framework,
                   "MidnightLib API for MidnightControls": self.MidnightLib}

    def Window(self):
        """
        open the window
        """

        root = ctk.CTk()
        root.title("Implementer une manette")
        root.geometry("600x380")

        instructionsLabel = ctk.CTkLabel(root, text="Clique sur le(s) mod(s) adapté(s), telecharge une version, puis glisse le fichier téléchargé dans le dossier 'mods' de l'instance souhaité.",
        wraplength=390)
        instructionsLabel.pack(pady=6, padx=5)

        for k, i in self.Options.items():
            if k == "Framework API for Controllables" or k == "MidnightLib API for MidnightControls":
                if k == "Framework API for Controllables":
                    APIlabel = ctk.CTkLabel(root, text="API", font=(ctk.CTkFont(), 15)).pack(fill="x", pady=2, padx=5)
                    ctk.CTkButton(root, text=k, command=lambda url=i: webbrowser.open(url), fg_color="#4DA1A9", hover_color="#2E5077").pack(fill="x", pady=5, padx=5)
                else:
                    ctk.CTkButton(root, text=k, command=lambda url=i: webbrowser.open(url), fg_color="#4DA1A9", hover_color="#2E5077").pack(fill="x", pady=5, padx=5)
            else:
                ctk.CTkButton(root, text=k, command=lambda url=i: webbrowser.open(url)).pack(fill="x", pady=5, padx=5)
        
        finiButton = ctk.CTkButton(root, text="Fini !", command=lambda:root.destroy())
        finiButton.pack(pady=10, padx=5)

        root.mainloop()

if __name__ == "__main__":
    controllerImplementation = CFimpl("1.19.4", "forge")
    controllerImplementation.Window()