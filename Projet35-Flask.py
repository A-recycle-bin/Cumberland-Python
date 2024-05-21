# Apprentissage du module flask
# Flask necessite quelques fichiers et une arborescence particuliere afin de fonctionner
# Il ne fonctionnera pas seulement en executant ce script
# Ce script sert plutot de note et de reference afin de bien comprendre le module

# script de base invoquant un hello world

# Importation du module flask
from flask import Flask

# Assignation de la fonction flask a la variable app (shortcut)
app = Flask(__name__)

# Definition d'un routing pour la page '/', qui est la page d<accueil
# C'est en effectuant ce routing que l'on assigne une url a une page html et des fonctions

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# HTML escaping, pour traiter les tentatives de command injection
#
# (BESOIN DE LIRE DAVANTAGE SUR LE SUJET)
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# HTML ESCAPING AUTRE EXEMPLE un resultat de diferentes fonctions pour escape le command injection
from markupsafe import Markup

Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up » HTML'

# Pour definir une page index par defaut, et le hello world sur l'url hello
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# On peut ajouter le nom des variables a l'url
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# URL building
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# le test_resquest_context() permet de simuler une request a des fins de test.
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

## Resultat :
# /
# /login
# /login?next=/
# /user/John%20Doe

# Par defaut l application va traiter les route comme des GET request
# Pour modifier cela il faut preciser quoi faire lorsque c'est un POST
# il est possible de le faire en deux fonctions separe

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

# ou de le faire dans la meme fonction

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


# Pour invoquer un fichier qui se trouve dans l arborescence /static/style.css

url_for('static', filename='style.css')


# Pour effectuer le rendu du template html
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello/')
def hello():
    return render_template('hello.html')