# Mini-Débuggeur Python avec IA

## Description

Ce projet est un **mini-débuggeur automatisé** pour scripts Python.  
Il permet de :

1. Exécuter un script Python dans un environnement virtuel isolé.
2. Récupérer les erreurs d’exécution (stderr).
3. Envoyer le code et l’erreur à un modèle d’IA (GPT-4).
4. Recevoir un JSON contenant des propositions de correction.
5. Afficher ou appliquer automatiquement les corrections.

Le projet est conçu pour être **modulaire, évolutif et facilement testable**.

---

## 🏗️ Structure du projet

mini_debuggeur_project/
│
├── main.py # Point d’entrée du projet
├── config.json # Configuration du script à analyser et du venv
├── requirements.txt # Dépendances Python
├── .env # Clé API OpenAI
│
├── modules/ # Modules principaux du débuggeur
│ ├── init.py
│ ├── runner.py # Exécution de scripts + récupération d'erreurs
│ ├── ai_agent.py # Communication avec l’IA
│ ├── patcher.py # Application des corrections
│ └── utils.py # Fonctions utilitaires
│
├── scripts_example/ # Scripts Python à tester
│ ├── bad_script.py # Script volontairement buggé
│ └── ok_script.py # Script fonctionnel
│
└── logs/ # Stockage des logs d’exécution

---

## ⚙️ Installation

1. **Cloner le projet**  
```bash
git clone <URL_DE_TON_PROJET>
cd mini_debuggeur_project

Créer l’environnement virtuel
python -m venv venv

Activer l’environnement

Windows :

.\venv\Scripts\Activate.ps1


Linux/macOS :

source venv/bin/activate


Installer les dépendances

pip install -r requirements.txt


Ajouter la clé OpenAI
Créer un fichier .env à la racine :

OPENAI_API_KEY=ta_cle_api_openai

## Utilisation

Configurer le script à analyser dans config.json :

{
    "venv_path": "venv",
    "script_path": "scripts_example/bad_script.py"
}


Lancer le débuggeur :

python main.py


Suivre les instructions dans le terminal :

Le script est exécuté

L’erreur est affichée

Les corrections proposées par l’IA sont affichées

Choisir si on applique les corrections (y/n)
