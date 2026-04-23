# cloud-cost-anomaly-detector

## 🚀 Contexte
Les entreprises utilisant le cloud peuvent avoir des coûts anormaux sans s’en rendre compte.  
Ce projet simule un outil simple de détection d’anomalies sur des coûts cloud.*

## 🎯 Objectif
- Analyser des données de coûts cloud
- Générer un rapport
- Détecter automatiquement les dépenses anormales

## 🛠️ Technologies utilisées
- Python
- CSV
- Docker

## 📁 Structure du projet
```text
cloud-cost-anomaly-detector/
├── data/
│   └── costs.csv
├── src/
│   └── detect.py
├── Dockerfile
└── README.md

2 ème phase

# Cloud Cost Monitoring & Alerting

Objectif
Ce projet permet de surveiller les coûts d'un environnement cloud et de détecter automatiquement des anomalies.  
En cas de dépassement anormal, une alerte est envoyée par email.

## Fonctionnalités

- Lecture des données de coûts depuis un fichier CSV
- Calcul :
  - coût total
  - moyenne
  - coût maximum
- Détection d’anomalies (coût > 2x la moyenne)
- Envoi d’alertes par email via SMTP (Mailtrap)

## Technologies utilisées

- Python
- SMTP (Mailtrap)
- CSV
- Variables d’environnement (.env)

## Sécurité

Les identifiants sensibles (SMTP) ne sont pas stockés dans le code.  
Ils sont externalisés via un fichier `.env`, ignoré par Git grâce au `.gitignore`.

## Structure du projet
cloud-project/
│
├── src/
│ └── detect.py
├── data/
│ └── costs.csv
├── .env (non versionné)
├── .gitignore
└── README.md

---

## 🚀 Lancement du projet

1. Cloner le projet :
```bash
git clone <url-du-repo>
Installer les dépendances :
pip install python-dotenv
Créer un fichier .env :
SMTP_LOGIN=your_login
SMTP_PASSWORD=your_password
Lancer le script :
python src/detect.py
📧 Exemple d’alerte

Une alerte est envoyée si une anomalie est détectée :

🚨 Cloud Cost Alert
- 2024-01-10 | EC2 | 250€
