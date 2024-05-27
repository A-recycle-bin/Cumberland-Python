import Etudiant, Personne, Point

# tout le monde devient vieux
print(Personne.p1.infos())
Personne.p1.set_age(99)
Personne.p2.set_age(99)
Personne.p3.set_age(99)
print(Personne.p1.infos())

#modification de l"etudiant 1
print(Etudiant.e1.__init__(nom='George', prenom='George', age=99, niveau='Aucun'))
print(Etudiant.e1.infos())

