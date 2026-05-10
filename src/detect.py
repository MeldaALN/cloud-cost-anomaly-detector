import os
import csv
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

costs = []
anomalies = []

def send_email(anomalies):
    smtp_server = "sandbox.smtp.mailtrap.io"
    port = 2525
    login = os.getenv("SMTP_LOGIN")
    password = os.getenv("SMTP_PASSWORD")

    sender = "alert@cloud.com"
    receiver = "finops-team@test.com"

    if not login or not password:
        print("❌ Variables d'environnement SMTP manquantes.")
        return

    anomaly_details = "\n".join(
        [f"- {row['date']} | {row['service']} | {row['cost']}€" for row in anomalies]
    )

    body = f"""🚨 Cloud Cost Alert

Des coûts anormaux ont été détectés :

{anomaly_details}
"""

    message = MIMEText(body)
    message["Subject"] = "Cloud Cost Alert"
    message["From"] = sender
    message["To"] = receiver

    try:
        server = smtplib.SMTP(smtp_server, port, timeout=10)
        server.starttls()
        server.login(login, password)
        server.sendmail(sender, [receiver], message.as_string())
        server.quit()
        print("📧 Email envoyé avec succès via Mailtrap !")

    except Exception as e:
        print("❌ Erreur lors de l'envoi de l'email :", repr(e))


# Lire les données
with open("data/costs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Récupérer les coûts
for row in rows:
    cost = float(row["cost"])
    costs.append(cost)

# Calculs
average = sum(costs) / len(costs)
total = sum(costs)
max_cost = max(costs)

print("=== Rapport des coûts cloud ===")
print(f"Nombre d'entrées : {len(costs)}")
print(f"Coût total : {total}€")
print(f"Moyenne des coûts : {average}€")
print(f"Coût maximum : {max_cost}€")
print("")

# Détection des anomalies
for row in rows:
    cost = float(row["cost"])

    if cost > average * 2:
        anomalies.append(row)
        print(f"🚨 Anomalie détectée le {row['date']} pour {row['service']} ({cost}€)")

print("")

if anomalies:
    send_email(anomalies)
else:
    print("✅ Aucun coût anormal détecté. Aucun email envoyé.")