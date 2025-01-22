import requests
import customtkinter
import CTkListbox
import os
import json
import shutil
import subprocess
import platform

def FetchJSON(JsonURL, JsonDownloadPath_Name):
    """Télécharge un fichier JSON à partir d'une URL et le sauvegarde localement."""
    r = requests.get(JsonURL, allow_redirects=True)
    open(JsonDownloadPath_Name, 'wb').write(r.content)

def extract_json_files(json_data):
    """
    Extrait les fichiers ZIP à partir d'un JSON.

    Args:
        json_data (dict): Le JSON à partir duquel extraire les fichiers ZIP.

    Returns:
        list: La liste des fichiers ZIP trouvés.
    """
    json_files = []
    if 'files' in json_data:
        for file in json_data['files']:
            if file.endswith('.json'):
                json_files.append(file)
    return json_files

def Window():
    # Télécharge le fichier JSON (à remplacer par votre URL et chemin de fichier)
    JsonURL = "https://gustoon.github.io/content/YWLTL/modpacks.json"
    JsonDownloadPath_Name = os.path.join(".", "downloads", "modpacks.json")
    FetchJSON(JsonURL, JsonDownloadPath_Name)

    # Crée la fenêtre principale
    root = customtkinter.CTk()
    root.title("Importer des mods dans une instance")
    root.geometry("400x500")

    # Liste des instances disponibles
    InstanceList = CTkListbox.CTkListbox(root)
    InstanceList.pack(fill="both", padx=5, pady=10)
    dirs = os.listdir(os.path.join(".", "Instances"))
    dirs = [x for x in dirs if x != ".MC"]
    for elem in dirs:
        InstanceList.insert("end", elem)

    # Instruction pour l'utilisateur
    instruction = customtkinter.CTkLabel(root, text="Selectionne une instance si-dessus dans laquelle\ntu vas importer les mod du modpack selectionné si-dessous")
    instruction.pack(fill="x", padx=5, pady=2)

    FetchJSON(JsonURL, JsonDownloadPath_Name)
    
    with open(os.path.join(".", "downloads", "modpacks.json"), 'r') as f:
        json_data = json.load(f)
    AvaibleModpacks = CTkListbox.CTkListbox(root)
    AvaibleModpacks.pack(fill="both", padx=5, pady=10)
    for yaml_file in extract_json_files(json_data):
        AvaibleModpacks.insert("end", yaml_file)

    def dwddmp():
        selected_modpack = AvaibleModpacks.get()
        selected_instance = InstanceList.get()
        instance_path = os.path.join(".", "Instances", selected_instance) # ajouter mods pour avoir les mods
        manifest_download_URL = f"https://gustoon.github.io/content/YWLTL/{selected_modpack}"
        FetchJSON(manifest_download_URL, os.path.join(".", "downloads", "manifest.json"))
        python = "python" if platform.system() == "Windows" else "python3"
        for file in os.listdir(os.path.join(instance_path, "mods")):
            if file.endswith(".jar"):
                os.remove(os.path.join(instance_path, "mods", file))
        shutil.copyfile(os.path.join(".", "download-mods.py"), os.path.join(instance_path, "mods", "download-mods.py"))
        shutil.copyfile(os.path.join(".", "downloads", "manifest.json"), os.path.join(instance_path, "mods", "manifest.json"))
        subprocess.run([python, "download-mods.py"], cwd=os.path.join(instance_path, "mods"))
        for file in os.listdir(os.path.join(instance_path, "mods")):
            if not file.endswith(".jar"):
                os.remove(os.path.join(instance_path, "mods", file))
    download_button = customtkinter.CTkButton(root, text="Fini !", command=dwddmp)
    download_button.pack(fill="x", padx=5, pady=2)

    root.mainloop()

if __name__ == "__main__":
    Window()