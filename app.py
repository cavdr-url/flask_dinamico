import os, json
from flask import Flask, render_template, url_for

app = Flask(__name__)

archivo_json = os.path.join(app.static_folder, 'data', 'deptos.json')
with open(archivo_json, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

@app.route('/')
def index():
    return render_template('index.html', deptos=datos)

if __name__=='__main__':
    app.run(debug=True)
    
    """
    {{ variable }} - Muestra el valor de una variable
    {% comando %} - Lógica (loops, condicionales)
    {% extends "base.html" %} - Herencia de templates
    {% block nombre %} - Define áreas de contenido variable
    
    """