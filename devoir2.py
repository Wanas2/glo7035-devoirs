### Devoir 2: La route des bières ###
# 
# Encore une fois, vos réponses doivent s'imprimer sur une seule ligne
# ET sous l'indication #Q...

from py2neo import Graph

url = "bolt://localhost:7687"
user = "neo4j"
password = "supersecret"

base_de_donnee = Graph(url, auth=(user,password))

#Question de pratique: Quelles sont les microbrasseries dans la ville de Québec? (0 points)
print("#Q0")
requete_0 = base_de_donnee.run("MATCH (micro:Microbrasserie)-[:est_à]->(depart:Ville) WHERE depart.nom = \"Québec\" RETURN micro")
print([x['micro']['nom'] for x in requete_0])

#Quelles sont les bières brassées à Québec?
# (2 points)
print("#Q1")
requete_1 = base_de_donnee.run("MATCH (b:`Bière`)--(m:Microbrasserie),(v:Ville)--(m:Microbrasserie) WHERE v.nom = \"Québec\" RETURN b")
print([x['b']['nom'] for x in requete_1])

# Avant de quitter pour la grande aventure, vous désirez connaître quelles sont les villes adjacentes à québec ayant une micro brasserie?
# (2 points)
print("#Q2")
requete_2 = base_de_donnee.run("MATCH (d:Ville)--(a:Ville), (a:Ville)--(m:Microbrasserie) WHERE d.nom = \"Québec\" Return a")
print([x['a']['nom'] for x in requete_2])

#Vous ne connaissez pas beaucoup les bières de type "Rousse", mais vous aimeriez trouver la meilleure au québec. Quel est le nom de la meilleure bière rousse et quelle est sa cote?
# (2 points)
print("#Q3")
requete_3 = base_de_donnee.run("MATCH (t:`Type_Bière`)--(b:`Bière`)--(:Microbrasserie)--(v:Ville) WHERE t.nom = \"Rousse\" AND v.nom = \"Québec\" RETURN b.nom, b.cote ORDER BY b.cote DESC LIMIT 1")
print([(n,c) for n,c in requete_3])

# Vous êtes un grand amateur de bières de types "Saison". Dans quelles villes trouverez vous ce type de bière?
# (2 points)
print("#Q4")
requete_4 = base_de_donnee.run("MATCH (t:`Type_Bière`)--(b:`Bière`), (b:`Bière`)--(m:Microbrasserie), (m:Microbrasserie)--(v:Ville) WHERE t.nom = \"Saison\" RETURN v")
print([x['v']['nom'] for x in requete_4])

# Vous désirez trouver une place tranquille pour prendre une bière, Quelles sont les villes ayant une microbrasserie et ayant moins de 20 000 habitants
# (2 points)
print("#Q5")
requete_5 = base_de_donnee.run("MATCH (v:Ville)--(m:Microbrasserie) WHERE v.population < 20000 RETURN v")
print([x['v']['nom'] for x in requete_5])

# Combien de bière de type "India Pale Ale" sont faites au québec
# (2 points)
print("#Q6")
requete_6 = base_de_donnee.run("MATCH (t:`Type_Bière`)--(b:`Bière`), (b:`Bière`)--(m:Microbrasserie), (m:Microbrasserie)--(v:Ville) WHERE t.nom = \"India Pale Ale\" AND v.nom = \"Québec\" RETURN count(b)")
print([x["count(b)"] for x in requete_6][0])

# Quels sont les types de bières en commun entre "Dieu du ciel" et "Le trou du diable"
# (3 points)
print("#Q7")
requete_7 = base_de_donnee.run("MATCH (t:`Type_Bière`)--(:`Bière`)--(:Microbrasserie{nom:\"Dieu du ciel\"}) WHERE (t:`Type_Bière`)--(:`Bière`)--(:Microbrasserie{nom:\"Le trou du diable\"}) RETURN t")
print([x['t']['nom'] for x in requete_7])