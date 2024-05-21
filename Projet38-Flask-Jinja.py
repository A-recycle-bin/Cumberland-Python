# Script enumerant les differents facons d'utiliser le template Jinja
# important de creer un template de base dans le fichier base.html et de l"utiliser
# dans les autres pages afin d'avoir la meme base (header, footer, etc)

# pour inclure un autre fichier que le base html
# {% include 'fichier_a_inclure.html' %} {% endblock %}


from flask import Flask

app = Flask(__name__)


#@app.route('/home', data=data, logged=True)
#def home():
    #data = input('please enter your name : ')
    #if logged = True
        #return '<h1>you are logged in</h1>'
    #else:
        #return '<h1>Not logged in</h1>'


# To invoke the data variable, insert {{ data }} in the html code.
# To invoke something if the if statement is true {% if logged %}
# To invoke the else, {% else %} {% endif %}

# to do a for loops {% for x in list %} {{ x }} {% endfor %{
# if this is a dictionnary instead of a list {% for x in dictionnaries %} {{ x.name }} {% endfor %}

