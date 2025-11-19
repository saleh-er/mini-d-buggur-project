import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_to_ai(script_path, error_message):

    # Lire le code source
    with open(script_path, "r") as f:
        code = f.read()

    # Créer le prompt pour l'IA
    prompt = f"""
Tu es un assistant Python spécialisé dans la correction de bugs.
Voici le code :
{code}

Voici l'erreur rencontrée :
{error_message}

Propose un correctif sous format JSON strict :
{{
  "status": "ok",
  "message": "Explication de la correction",
  "changes": [
    {{
      "file": "{script_path}",
      "line_to_replace": <numéro_de_ligne>,
      "new_line": "<nouvelle_ligne_de_code>"
    }}
  ]
}}
Si aucune correction nécessaire, renvoie "status": "ok" et "changes": []
"""

    # Appel à l'API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un correcteur Python expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    # Récupérer le texte de l'IA
    text_response = response['choices'][0]['message']['content']

    # Convertir le JSON en dict Python
    patch_json = json.loads(text_response)

    return patch_json
