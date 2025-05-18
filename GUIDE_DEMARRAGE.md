# Guide de démarrage - Prédictions F1 2025 🏎️

Wasssup guyssss un petit guide qui vous aidera à installer et utiliser le projet de prédictions F1 2025, même si vous êtes nul nul en programmation

## 1. Ouvrir le Terminal sur Mac 🖥️

1. Appuyez sur `Cmd (⌘) + Espace` pour ouvrir Spotlight
2. Tapez "Terminal"
3. Appuyez sur Entrée pour ouvrir le Terminal

## 2. Installer les outils nécessaires 🛠️

### Installation de Homebrew (gestionnaire de paquets)
1. Copiez-collez cette commande dans le Terminal :
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Appuyez sur Entrée
3. Suivez les instructions à l'écran (tapez votre mot de passe si demandé)

### Installation de Python
1. Dans le Terminal, tapez :
```bash
brew install python
```
2. Appuyez sur Entrée
3. Attendez que l'installation se termine

## 3. Télécharger le projet 📥

1. Créez un nouveau dossier pour le projet :
```bash
mkdir f1_predictions
cd f1_predictions
```

2. Téléchargez les fichiers du projet :
   - Allez sur [GitHub](https://github.com/yachour1/2025_f1_predictions)
   - Cliquez sur le bouton vert "Code"
   - Sélectionnez "Download ZIP"
   - Décompressez le fichier ZIP téléchargé
   - Copiez tous les fichiers dans le dossier `f1_predictions` que vous venez de créer

## 4. Configurer l'environnement de travail ⚙️

1. Créez un environnement virtuel (c'est comme un espace de travail isolé) :
```bash
python3 -m venv venv
```

2. Activez l'environnement virtuel :
```bash
source venv/bin/activate
```
(Vous verrez `(venv)` apparaître au début de votre ligne de commande)

3. Installez les programmes nécessaires :
```bash
pip install -r requirements.txt
```
(Attendez que l'installation se termine)

## 5. Lancer les prédictions 🏁

1. Configurez le projet :
```bash
python setup.py
```

2. Lancez les prédictions :
```bash
python prediction1.py
```

## En cas de problème ❓

### Si vous avez une erreur de cache :
```bash
python setup.py
```

### Si vous avez une erreur de permissions :
```bash
chmod +x prediction1.py
```

## Notes importantes 📝

- Ne fermez pas le Terminal pendant que vous travaillez
- Si vous voyez `(venv)` au début de la ligne, c'est que tout est bien configuré
- Si vous fermez le Terminal, vous devrez réactiver l'environnement virtuel avec :
```bash
source venv/bin/activate
```

## Pour arrêter 🛑

- Pour désactiver l'environnement virtuel : tapez `deactivate`
- Pour quitter le Terminal : tapez `exit` ou appuyez sur `Cmd (⌘) + Q`

## Comprendre les résultats 📊

Le programme va afficher :
- Les prédictions pour chaque pilote
- Le temps de course prédit
- L'erreur moyenne du modèle (MAE)

Plus l'erreur (MAE) est basse, plus les prédictions sont précises !

## Besoin d'aide ? 🤝

Si vous rencontrez des problèmes :
1. Vérifiez que vous avez bien suivi toutes les étapes
2. Assurez-vous que vous êtes dans le bon dossier
3. Vérifiez que vous voyez `(venv)` au début de votre ligne de commande

Bonne chance avec les prédictions ! 🏎️ 