## Version 1 – Analyse des coûts

Cette première version du projet permet :
- d’analyser les données de coûts cloud
- de calculer des indicateurs (total, moyenne, maximum)
- de générer un rapport

---
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
```
 ---

## Version 2 – Détection et alertes

Une seconde version a été développée pour améliorer le projet :

- détection automatique des anomalies (coût > 2× la moyenne)
- envoi d’alertes par email via SMTP (Mailtrap)
- sécurisation des identifiants avec variables d’environnement (.env)

## Cloud Cost Monitoring & Alerting

## 🎯 Objectif
Ce projet permet de surveiller les coûts d’un environnement cloud et de détecter automatiquement des anomalies.  
En cas de dépassement anormal, une alerte est envoyée par email.

## ⚙️ Fonctionnalités

- 📥 Lecture des données depuis un fichier CSV  
- 📊 Calcul des indicateurs :
  - Coût total
  - Moyenne des coûts
  - Coût maximum  
- 🚨 Détection d’anomalies (coût > 2× la moyenne)  
- 📧 Envoi automatique d’un email d’alerte via SMTP (Mailtrap)  
- 🧾 Affichage d’un rapport dans le terminal  

## 🛠️ Technologies utilisées

- Python 3  
- SMTP (Mailtrap)  
- CSV (gestion de données)  
- Variables d’environnement (.env)  
- Git & GitHub  

## 🔐 Sécurité

Les bonnes pratiques de sécurité ont été appliquées :

- Les identifiants SMTP ne sont pas stockés dans le code  
- Utilisation de variables d’environnement via un fichier `.env`  
- Le fichier `.env` est exclu du versioning grâce au `.gitignore`  
- Connexion SMTP sécurisée avec STARTTLS  

👉 Cela permet d’éviter toute fuite de données sensibles.

## 📂 Structure du projet
```text
cloud-project/
├── src/
│ └── detect.py
├── data/
│ └── costs.csv
├── .env (non versionné)
├── .gitignore
└── README.md
```
