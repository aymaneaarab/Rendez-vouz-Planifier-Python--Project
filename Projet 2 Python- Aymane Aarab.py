from datetime import datetime

#1
def remplir(taches):
    nb=int(input("entrez les nombres des taches "))
    for i in range (nb):
        tache={}
        nom=input("entrez le nom de la tache ")
        date=input("entrez la date de la tache en ce format JJ/MM/AAAA (exemple: 01/11/2010) ")
        complete=input(" tache complete? oui / non ")
        tache["nom"]=nom
        tache["date"]=date
        tache["complete"]=complete
        taches.append(tache)

#6
def affichagetout(taches):
    for i in taches:
        print("Nom de la tâche : ", i["nom"])
        print("Date : ", i["date"])
        print("Statut (complete ou non) : ", i["complete"])
        print("-----------------")



#4
def suppression(taches):
    nom=input("entrez le nom de tache qui tu veux supprimer ")
    for i in taches:
        if i["nom"]==nom:
            taches.remove(i)
            print("la tache ",nom ,"a ete supprimme")
            break
    else:
        print("le nom de tache qui vous entrez non disponible""")

#3
def modifi(taches):
    nom=input("entrez le nom de tache que tu veux modifier")
    for i in taches:
        if i['nom'] == nom:
            date = input("entrez la nouvelle date ou tappez entrer pour conserver l ancienne date")
            if date:
                i['date'] = date
            complete = input(" entrez le nouveau statut de la tache (oui/ non) ou tappez entrer pour conserver l ancien status si il est complete ou non")
            if complete:
                i['complete'] = complete
            print(f"tache '{nom}' a ete modifie.")
            return
    print(f"tache  '{nom}' non disponible.")




#2
def ajout(taches):
    nom=input("entrez le nom de la tache ")
    date=input("entrez la date de la tache en ce format JJ/MM/AAAA (exemple: 01/11/2010) ")
    complete=input(" tache complete? oui / non ")
    tache = {'nom': nom, 'date': date, 'complete': complete}
    taches.append(tache)
    print("la tache ajoutee en succes")



#5
def recherche(taches):
    nom=input("entrez le nom de la tache")
    for i in taches:
        if i["nom"]==nom:
            print("Nom de la tâche : ", i["nom"])
            print("Date : ", i["date"])
            print("Statut (complete ou non) : ", i["complete"])
            print("-----------------")
            break
    else:
            print("ce nom n ' es pas disponible")



#7
def affichperiode(taches):
    date_debut = input("Entrez la date de début en format JJ/MM/AAAA(exemple: 11/10/2020) : ")
    date_fin = input("Entrez la date de fin en format JJ/MM/AAAA(exemple: 11/10/2020) : ")

    date_debut = datetime.strptime(date_debut, "%d/%m/%Y")
    date_fin = datetime.strptime(date_fin, "%d/%m/%Y")

    print("Tâches pour la période sélectionnée :")
    for tache in taches:
        tache_date = datetime.strptime(tache['date'], "%d/%m/%Y")
        if date_debut <= tache_date <= date_fin:
            print(f"Nom de la tache: {tache['nom']} || date de la tache : {tache['date']}||  status de la tache(complete ou non):{tache['complete']}")

#8
def filtre(taches):
    date_debut = input("Entrez la date de début (JJ/MM/AAAA) : ")
    date_fin = input("Entrez la date de fin (JJ/MM/AAAA) : ")

    date_debut = datetime.strptime(date_debut, "%d/%m/%Y")
    date_fin = datetime.strptime(date_fin, "%d/%m/%Y")

    filtre = input("Afficher les tâches terminées ou non terminées / oui pour les taches termines, non pour les taches non termines ")
   
    print("Tâches filtrées :")
    for tache in taches:
        tache_date = datetime.strptime(tache['date'], "%d/%m/%Y")
        if date_debut <= tache_date <= date_fin and tache['complete'] == filtre:
            print(f"Nom de la tache: {tache['nom']} || date de la tache : {tache['date']}||  status de la tache(complete ou non):{tache['complete']}")





choix=0
while choix!=9:
    print("""---------MENU-------
1- remplire la base de donne avec votre taches
2- ajouter une tache (vous devez remplir la base de donne premierement pour ajouter)
3- modifier une tache (vous devez remplir la base de donne premierement pour modifier)
4- supprimer une tache (vous devez remplir la base de donne premierement pour supprimer)
5- recherche une tache et affiche les infos
6- afficher tous les taches et ses informations
7- afficher les taches pour une periode
8- filtrer les taches (termines ou non)
9- Quitter
entrez votre choix: """)
    choix=int(input())
    if choix==1:
        taches=[]
        remplir(taches)
    elif choix==2:
        ajout(taches)
    elif choix==3:
        modifi(taches)
    elif choix==4:
        suppression(taches)
    elif choix==5:
        recherche(taches)
    elif choix==6:
        affichagetout(taches)
    elif choix==7:
        affichperiode(taches)
    elif choix==8:
        filtre(taches)
    elif choix==9:
        print("fin programme")
        break
    else:
        print("choix invalide")
        


