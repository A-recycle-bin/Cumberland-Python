# Projet qui prend genere un mot de passe en renvoyant des caracteres aleatoires
# 64 Caracteres en majuscule, chiffre et carac speciaux


import random


# Fonction pour effectuer l.operation "shuffle"
def melange(mdp):
  liste = list(mdp)
  random.shuffle(liste)
  return ''.join(liste)


# Creation des caracteres aleatoires
carac1=chr(random.randint(40,90))
carac2=chr(random.randint(40,90))
carac3=chr(random.randint(40,90))
carac4=chr(random.randint(40,90))
carac5=chr(random.randint(40,90))
carac6=chr(random.randint(40,90))
carac7=chr(random.randint(40,90))
carac8=chr(random.randint(40,90))
carac9=chr(random.randint(40,90))
carac10=chr(random.randint(40,90))
carac11=chr(random.randint(40,90))
carac12=chr(random.randint(40,90))
carac13=chr(random.randint(40,90))
carac14=chr(random.randint(40,90))
carac15=chr(random.randint(40,90))
carac16=chr(random.randint(40,90))
carac17=chr(random.randint(40,90))
carac18=chr(random.randint(40,90))
carac19=chr(random.randint(40,90))
carac20=chr(random.randint(40,90))
carac21=chr(random.randint(40,90))
carac22=chr(random.randint(40,90))
carac23=chr(random.randint(40,90))
carac24=chr(random.randint(40,90))
carac25=chr(random.randint(40,90))
carac26=chr(random.randint(40,90))
carac27=chr(random.randint(40,90))
carac28=chr(random.randint(40,90))
carac29=chr(random.randint(40,90))
carac30=chr(random.randint(40,90))
carac31=chr(random.randint(40,90))
carac32=chr(random.randint(40,90))
carac33=chr(random.randint(40,90))
carac34=chr(random.randint(40,90))
carac35=chr(random.randint(40,90))
carac36=chr(random.randint(40,90))
carac37=chr(random.randint(40,90))
carac38=chr(random.randint(40,90))
carac39=chr(random.randint(40,90))
carac40=chr(random.randint(40,90))
carac41=chr(random.randint(40,90))
carac42=chr(random.randint(40,90))
carac43=chr(random.randint(40,90))
carac44=chr(random.randint(40,90))
carac45=chr(random.randint(40,90))
carac46=chr(random.randint(40,90))
carac47=chr(random.randint(40,90))
carac48=chr(random.randint(40,90))
carac49=chr(random.randint(40,90))
carac50=chr(random.randint(40,90))
carac51=chr(random.randint(40,90))
carac52=chr(random.randint(40,90))
carac53=chr(random.randint(40,90))
carac54=chr(random.randint(40,90))
carac55=chr(random.randint(40,90))
carac56=chr(random.randint(40,90))
carac57=chr(random.randint(40,90))
carac58=chr(random.randint(40,90))
carac59=chr(random.randint(40,90))
carac60=chr(random.randint(40,90))
carac61=chr(random.randint(40,90))
carac62=chr(random.randint(40,90))
carac63=chr(random.randint(40,90))
carac64=chr(random.randint(40,90))


password = carac1+carac64+carac63+carac6+carac2+carac3+carac4+carac5+carac58+carac59+carac60+carac61+carac62+carac10+carac11+carac12+carac13+carac14+carac15+carac16+carac17+carac18+carac19+carac20+carac21+carac22+carac23+carac24+carac25+carac26+carac27+carac28+carac29+carac30+carac31+carac32+carac33+carac34+carac35+carac36+carac37+carac38+carac39+carac40+carac41+carac42+carac43+carac44+carac45+carac46+carac47+carac48+carac49+carac50+carac51+carac52+carac53+carac54+carac55+carac56+carac57+carac7+carac8+carac9
password = melange(password)
print('Les mots de passe suggérés sont :\n    ', password)
print('Ou :', melange(password))
print('Ou :', melange(password))
print('Ou :', melange(password))
print('Ou :', melange(password))
print('Également possible de relancer le script pour obtenir de nouveaux résultats.')