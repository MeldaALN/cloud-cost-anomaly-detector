import csv

costs = []

# Ouvrir le fichier et lire toutes les lignes
with open("data/costs.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Récupérer tous les coûts
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
        print(f"🚨 Anomalie détectée le {row['date']} pour {row['service']} ({cost}€)")
