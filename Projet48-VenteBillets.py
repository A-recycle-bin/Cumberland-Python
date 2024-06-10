
class Evenement:

    def __init__(self, name, date, location, price, place):
        self.name = name
        self.date = date
        self.location = location
        self.price = price
        self.place = place
        self.billets_vendus = 0

    def vendre_billet(self, quantite):
        """
        Fonction qui permet de vendre un ou des billets a l'utilisateur

        Input:
            quantite (int): Le nombre de billets à vendre.

        Output:
            Le montant total de la vente (valeur float).
        """
        if self.place >= quantite:
            self.place -= quantite
            self.billets_vendus += quantite
            return quantite * self.price
        else:
            return 0.0

class GestionnaireEvenements:
    """
    Classe qui va gérer les événements et les ventes de billets.

    """
    def __init__(self):
        """
        Initialise la liste des événements.
        """
        self.evenements = []

    def ajouter_evenement(self, evenement):
        """
         Fonction ADMIN pour ajouter un nouvel événement à la liste.
        Input:
             L'événement à ajouter.
        """
        self.evenements.append(evenement)

    def vendre_billet(self, nom_evenement, quantite):
        """
        Vend une certaine quantité de billets pour un événement.
        Input:
            Le nom de l'événement (str)
            Le nombre de billets à vendre (int)
        Output:
            Le montant total de la vente (float).
        """
        for evenement in self.evenements:
            if evenement.name == nom_evenement:
                return evenement.vendre_billet(quantite)
        return 0.0

    def afficher_evenements(self):
        """
        Affiche la liste des événements.
        """
        for evenement in self.evenements:
            print(f"Événement: {evenement.name}")
            print(f"Date: {evenement.date}")
            print(f"Lieu: {evenement.location}")
            print(f"Prix du billet: {evenement.price} $$")
            print(f"Billets disponibles: {evenement.place}")
            print(f"Billets vendus: {evenement.billets_vendus}")
            print()


# Exemple d'utilisation
gestionnaire = GestionnaireEvenements()

concert = Evenement("Concert de rock", "2023-06-15", "Salle des fêtes", 500, 25)
gestionnaire.ajouter_evenement(concert)

salon = Evenement("Salon de l'automobile", "2023-09-20", "Parc des expositions", 1000, 10)
gestionnaire.ajouter_evenement(salon)

print("Vente de billets pour le concert:")
montant_vente = gestionnaire.vendre_billet("Concert de rock", 50)
print(f"Montant total de la vente: {montant_vente} $$")

print("\nVente de billets pour le salon:")
montant_vente = gestionnaire.vendre_billet("Salon de l'automobile", 100)
print(f"Montant total de la vente: {montant_vente} $$")

print("\nListe des événements:")
gestionnaire.afficher_evenements()