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


liste_personnes = ListePersonnes()
liste_personnes.ajouter_personne("Alice", 25)
liste_personnes.ajouter_personne("Bob", 30)
liste_personnes.ajouter_personne("Cimon", 20)
liste_personnes.ajouter_personne("Donald", 22)
liste_personnes.ajouter_personne("Erman", 9)
liste_personnes.ajouter_personne("Poulet", 27)

print("Liste de personnes:")
liste_personnes.afficher_personnes()

print("\nRecherche de personne:")
liste_personnes.rechercher_personne("Bob")
print("\nFiltrage par âge entre 20 et 25 ans:")
liste_personnes.filtrer_personnes_par_age(20, 25)
print("\nFiltrage par âge entre 10 et 33 ans:")
liste_personnes.filtrer_personnes_par_age(10, 33)