Guide d'installation et d'utilisation - F1 Predictions 2025
====================================================

Ce guide vous aidera à installer et exécuter le projet de prédictions F1 2025 sur votre Mac.

1. INSTALLATION DE PYTHON
------------------------
1. Ouvrez le Terminal (cherchez "Terminal" dans Spotlight avec Cmd + Espace)
2. Installez Homebrew si ce n'est pas déjà fait :
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3. Installez Python :
   brew install python

2. TÉLÉCHARGEMENT DU PROJET
--------------------------
1. Créez un nouveau dossier pour le projet :
   mkdir f1_predictions
   cd f1_predictions
2. Téléchargez les fichiers du projet dans ce dossier

3. CRÉATION DE L'ENVIRONNEMENT VIRTUEL
------------------------------------
1. Créez l'environnement virtuel :
   python3 -m venv venv
2. Activez l'environnement virtuel :
   source venv/bin/activate
   (Vous verrez (venv) apparaître au début de votre ligne de commande)

4. INSTALLATION DES DÉPENDANCES
-----------------------------
1. Installez les packages nécessaires :
   pip install -r requirements.txt

5. EXÉCUTION DU CODE
------------------
1. Exécutez le script de configuration :
   python setup.py
2. Lancez les prédictions :
   python prediction1.py

EN CAS D'ERREUR
--------------
- Si vous avez une erreur de cache, exécutez :
  python setup.py
- Si vous avez une erreur de permissions, utilisez :
  chmod +x prediction1.py

NOTES IMPORTANTES
----------------
- Assurez-vous d'être toujours dans le dossier du projet quand vous exécutez les commandes
- L'environnement virtuel doit être activé (vous voyez (venv) au début de la ligne)
- Si vous fermez le Terminal, vous devrez réactiver l'environnement virtuel avec :
  source venv/bin/activate

POUR ARRÊTER
-----------
- Pour désactiver l'environnement virtuel : deactivate
- Pour quitter le Terminal : exit ou Cmd + Q

BONNE UTILISATION !
================== 