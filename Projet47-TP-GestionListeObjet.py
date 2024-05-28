# TP Travaux sur la gestion des objets dans une liste


class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}"


class ListePersonnes:
    def __init__(self):
        self.personnes = []

    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.personnes.append(nouvelle_personne)

    def afficher_personnes(self):
        for personne in self.personnes:
            print(personne)

    def rechercher_personne(self, nom):
        for personne in self.personnes:
            if personne.nom == nom:
                print(personne)
                return
        print(f"Aucune personne avec le nom '{nom}' n'a été trouvée.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        personnes_filtrees = [personne for personne in self.personnes if min_age <= personne.age <= max_age]
        if personnes_filtrees:
            for personne in personnes_filtrees:
                print(personne)
        else:
            print(f"Aucune personne trouvée avec un âge entre {min_age} et {max_age}.")


class FileAttente:
    def __init__(self):
        self.file = []

    def ajouter_personne_en_attente(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        # le false va definir que la personne est reguliere
        self.file.append((nouvelle_personne, False))

    def ajouter_personne_importante(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        # le true va definir que la personne est importante
        self.file.insert(0,(nouvelle_personne, True))

    # def supprimer_personne_en_attente(self, nom, age):
    #     self.file.pop(nom)
    #     self.file.pop(age)




vLP = ListePersonnes()
vLP.ajouter_personne("Alice", 25)
vLP.ajouter_personne("Bob", 30)
vLP.ajouter_personne("Cimon", 20)
vLP.ajouter_personne("Donald", 22)
vLP.ajouter_personne("Erman", 9)
vLP.ajouter_personne("Poulet", 27)

print("Liste de personnes:")
vLP.afficher_personnes()

print("\nRecherche de personne:")
vLP.rechercher_personne("Bob")
print("\nFiltrage par âge entre 20 et 25 ans:")
vLP.filtrer_personnes_par_age(20, 25)
print("\nFiltrage par âge entre 10 et 33 ans:")
vLP.filtrer_personnes_par_age(10, 33)

vFA = FileAttente()
# vFA.ajouter_personne_en_attente('Tit-gris', 66)
# vFA.ajouter_personne_importante('Tit-noir', 2)
# vFA.ajouter_personne_en_attente('Tit-blanc', 33)
# vFA.supprimer_personne_en_attente('Tit-gris', 66)

print("\n\n\n\n")

class SalleCinema:
    def __init__(self, capacity):
        self.capacity = capacity
        self.reserved_places = []
        self.special_places = []

    def reserver_place(self, nom, place):
        if self.nombre_places_disponibles() > 0:
            self.reserved_places.append((nom, place))
            print(f"Une place a été réservée {nom} à la place {place} avec succès.")
        else:
            print("La place n,est pas disponible.")

    def afficher_places_reservees(self):
        print("Les places réservées sont les suivantes :")
        for nom, place in self.reserved_places:
            print(f"{nom} - Place {place}")

    def nombre_places_disponibles(self):
        return self.capacity - len(self.reserved_places)

    def filtrer_reservations_par_personne(self, nom):
        print(f"Reservations pour {nom}:")
        for n, place in self.reserved_places:
            if n == nom:
                print(f"{n} - Place {place}")

    def annuler_reservation(self, nom):
        self.reserved_places = [(n, place) for n, place in self.reserved_places if n != nom]
        print(f"Les réservations pour {nom} ont été annulées.")

    def reserver_place_speciale(self, nom):
        self.special_places.append(nom)
        print(f"une place spéciale est réservée pour {nom}.")

    def afficher_places_reservees_speciales(self):
        print("Les places réservées spéciales sont les suivantes :")
        for nom in self.special_places:
            print(f"{nom} a réservé une place spéciales")

# Example Usage
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




