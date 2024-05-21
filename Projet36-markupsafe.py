# Test avec le module markupsafe. Il sert de html escaping lors des input
# Il va mitiger les risques de command injection

from markupsafe import Markup

# html escaping ( retirer les balises) via un input
#ok = Markup.escape(str(input('Entrez votre nom:',)))
#print(ok)

# html escaping en assignant une variable
nom = '<<script>JAVA</script> ? @#$%^&*()_'
markupnom = Markup.escape(nom)
print(markupnom)

# Avec une fonction qui retourne l'input mais nettoyé
def escape_html_input(user_input):
    escaped_input = Markup.escape(user_input)
    return escaped_input



