import json
import os

def save_session_profil(uname):
    folder_path = "save_user"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{uname}.json")
    
    profile_sow = {
        "username" : uname
    }
    
    with open(file_path, "w") as file:
        json.dump(profile_sow, file)
    success = print("Profil telah tersimpan !")
    
    