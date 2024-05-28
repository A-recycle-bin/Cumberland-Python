# TP Travaux sur la gestion des objets dans une liste

# Creation d'une classe dans la quelle on definit une personne par son nom et son age
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

# une facon de return la liste personne mais dans une phrase
    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}"

# Creation dune autre classe qui celle-ci contient la liste des personnes, defini au préalable
#  ajouter une personne a la liste
class ListePersonnes:
    def __init__(self):
        self.personnes = []

    #  ajouter une personne a la liste
    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.personnes.append(nouvelle_personne)

    #  ajouter la liste de personnes
    def afficher_personnes(self):
        for personne in self.personnes:
            print(personne)

    #  effectuer une recherche de personne dans la liste via son nom
    def rechercher_personne(self, nom):
        for personne in self.personnes:
            if personne.nom == nom:
                print(personne)
                return
        print(f"Aucune personne avec le nom '{nom}' n'a été trouvée.")

    #  filtrer une recherche par l'age de la personne
    def filtrer_personnes_par_age(self, min_age, max_age):
        personnes_filtrees = [personne for personne in self.personnes if min_age <= personne.age <= max_age]
        if personnes_filtrees:
            for personne in personnes_filtrees:
                print(personne)
        else:
            print(f"Aucune personne trouvée avec un âge entre {min_age} et {max_age}.")


#  Création d'une autre classe qui va gérer une files d'attentes
# Elle contient évidemment des personnes.
class FileAttente:
    def __init__(self):
        self.file = []

    #  ajouter une personne a la liste d'attente
    def ajouter_personne_en_attente(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        # le false va definir que la personne est reguliere
        self.file.append((nouvelle_personne, False))

    #  ajouter une personne importante a la liste d'attente
    def ajouter_personne_importante(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        # le true va definir que la personne est importante
        self.file.insert(0,(nouvelle_personne, True))

    #  supprimer une personne a la liste d'attente
    # def supprimer_personne_en_attente(self, nom, age):
    #     self.file.pop(nom)
    #     self.file.pop(age)


# quelques manipulations
vLP = ListePersonnes()
vLP.ajouter_personne("Alice", 25)
vLP.ajouter_personne("Bob", 30)
vLP.ajouter_personne("Cimon", 20)
vLP.ajouter_personne("Donald", 22)
vLP.ajouter_personne("Erman", 9)
vLP.ajouter_personne("Poulet", 27)


print("Liste de personnes:", vLP.afficher_personnes())
print("\nRecherche de personne:", vLP.rechercher_personne("Bob"))
print("\nFiltrage par âge entre 20 et 25 ans:", vLP.filtrer_personnes_par_age(20, 25))
print("\nFiltrage par âge entre 10 et 33 ans:", vLP.filtrer_personnes_par_age(10, 33))

vFA = FileAttente()
# vFA.ajouter_personne_en_attente('Tit-gris', 66)
# vFA.ajouter_personne_importante('Tit-noir', 2)
# vFA.ajouter_personne_en_attente('Tit-blanc', 33)
# vFA.supprimer_personne_en_attente('Tit-gris', 66)

print("\n\n\n\n")

# Ici on définit une salle de cinema, dans laquelle on definit une capacité (nbr de places)
# il y a ensuite deux listes, une pour les places reservees et lautre les places
# speciales pour handicapées.
class SalleCinema:
    def __init__(self, capacity):
        self.capacity = capacity
        self.reserved_places = []
        self.special_places = []

# Definiton d'une fonction pour reserver une place, besoin du nom et du choix de la place (par un integer)
    def reserver_place(self, nom, place):
        if self.nombre_places_disponibles() > 0:
            self.reserved_places.append((nom, place))
            print(f"Une place a été réservée {nom} à la place {place} avec succès.")
        else:
            print("La place n,est pas disponible.")

# Definiton dune fonction pour afficher les places qui ont été réservées
    def afficher_places_reservees(self):
        print("Les places réservées sont les suivantes :")
        for nom, place in self.reserved_places:
            print(f"{nom} - Place {place}")

# La difference avec la fonciton ci dessus est que celle-ci retourne seulement un integer et non pas la liste
    def nombre_places_disponibles(self):
        return self.capacity - len(self.reserved_places)

# Facon de rechercher si une personne a reserver, par son nom
    def filtrer_reservations_par_personne(self, nom):
        print(f"Reservations pour {nom}:")
        for n, place in self.reserved_places:
            if n == nom:
                print(f"{n} - Place {place}")

# Annuler une reservation
    def annuler_reservation(self, nom):
        self.reserved_places = [(n, place) for n, place in self.reserved_places if n != nom]
        print(f"Les réservations pour {nom} ont été annulées.")

# Annuleru ne reservation de place speciales
    def reserver_place_speciale(self, nom):
        self.special_places.append(nom)
        print(f"une place spéciale est réservée pour {nom}.")

#Afficher les places speciales reservees
    def afficher_places_reservees_speciales(self):
        print("Les places réservées spéciales sont les suivantes :")
        for nom in self.special_places:
            print(f"{nom} a réservé une place spéciales")

# On s'amuse un peu
cine = SalleCinema(50)
print("Places restantes :", cine.nombre_places_disponibles())
cine.reserver_place('Jacques', 2)
print("Places restantes :", cine.nombre_places_disponibles())
print('Nombre de places réservées : ', cine.afficher_places_reservees())
cine.reserver_place("Alice", 10)
cine.reserver_place("Bob", 20)
cine.reserver_place("Cimon", 30)
cine.reserver_place("Cimon", 31)

cine.afficher_places_reservees()
print("Places restantes :", cine.nombre_places_disponibles())
cine.filtrer_reservations_par_personne("Alice")
cine.annuler_reservation("Alice")
cine.reserver_place_speciale("Julie-Rose")
cine.afficher_places_reservees()
cine.afficher_places_reservees_speciales()




