import json
from modules.runner import run_script
from modules.ai_agent import send_to_ai
from modules.patcher import apply_patch

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    script_path = config["script_path"]

    print(f"--- Exécution du script : {script_path} ---")
    output, error = run_script(script_path)

    if not error:
        print("Aucune erreur trouvée !")
        return

    print("\n--- Erreur détectée ---")
    print(error)

    print("\n--- Envoi à l'IA ---")
    patch_json = send_to_ai(script_path, error)

    print("\n--- Patch proposé ---")
    print(patch_json)

    apply = input("Appliquer les corrections ? (y/n) : ")

    if apply.lower() == "y":
        apply_patch(patch_json)
        print("Corrections appliquées.")
    else:
        print("Aucune correction appliquée.")

if __name__ == "__main__":
    main()
