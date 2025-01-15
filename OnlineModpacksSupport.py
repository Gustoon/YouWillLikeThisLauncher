import requests
import customtkinter
import CTkListbox
import os
import json
import shutil
import subprocess
import platform
import yaml

def FetchJSON(JsonURL, JsonDownloadPath_Name):
    """Télécharge un fichier JSON à partir d'une URL et le sauvegarde localement."""
    r = requests.get(JsonURL, allow_redirects=True)
    open(JsonDownloadPath_Name, 'wb').write(r.content)

def LoadYAMLFiles(JsonFilePath):
    """Charge les fichiers YAML à partir d'un fichier JSON."""
    with open(JsonFilePath, 'r') as file:
        data = json.load(file)
    return data.get('files', [])

def download_yaml_file(yaml_file_url, yaml_file_path):
    """Télécharge un fichier YAML à partir d'une URL et le sauvegarde localement."""
    r = requests.get(yaml_file_url, allow_redirects=True)
    open(yaml_file_path, 'wb').write(r.content)

def Window():
    # Télécharge le fichier JSON (à remplacer par votre URL et chemin de fichier)
    JsonURL = "https://gustoon.github.io/content/YWLTL/modpacks.json"
    JsonDownloadPath_Name = "./downloads/modpacks.json"
    FetchJSON(JsonURL, JsonDownloadPath_Name)

    # Charge les fichiers YAML à partir du fichier JSON
    yaml_files = LoadYAMLFiles(JsonDownloadPath_Name)

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

    # Liste des fichiers YAML disponibles
    AvaibleModpacks = CTkListbox.CTkListbox(root)
    AvaibleModpacks.pack(fill="both", padx=5, pady=10)
    for yaml_file in yaml_files:
        AvaibleModpacks.insert("end", yaml_file)

    # Bouton pour télécharger le fichier YAML sélectionné
    def download_selected_yaml_file():
        selected_yaml_file = AvaibleModpacks.get(AvaibleModpacks.curselection())
        yaml_file_url = f"https://gustoon.github.io/content/YWLTL/{selected_yaml_file}"
        yaml_file_path = os.path.join(".", "downloads", selected_yaml_file)
        download_yaml_file(yaml_file_url, yaml_file_path)

        shutil.move(os.path.join(".", "downloads", selected_yaml_file), os.path.join(".", "RMMUD", "RMMUDInstances", selected_yaml_file))

        python = "python" if platform.system() == "Windows" else "python3"
        subprocess.run([python, "RMMUD.py"], cwd=os.path.join(".", "RMMUD"))

        for mod in os.listdir(os.path.join(".", "RMMUD", "mods")):
            shutil.move(os.path.join(".", "RMMUD", "mods", mod), os.path.join(".", "Instances", InstanceList.get(), "mods"))

        with open(os.path.join(".", "RMMUD", "RMMUDInstances", selected_yaml_file), 'r') as file:
            data = yaml.safe_load(file)
            file.close()
        with open(os.path.join(".", "RMMUD", "RMMUDInstances", selected_yaml_file), 'w') as file:
            data['Enabled'] = "false"
            yaml.dump(data, file)
            file.close()

    download_button = customtkinter.CTkButton(root, text="Fini !", command=download_selected_yaml_file)
    download_button.pack(fill="x", padx=5, pady=2)

    root.mainloop()

if __name__ == "__main__":
    Window()