from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

def load_species():
    with open(os.path.join('data', 'species.json')) as f:
        return json.load(f)

species_list = load_species()

def get_species(species_id):
    for sp in species_list:
        if sp['id'] == species_id:
            return sp
    return None

@app.route('/')
def index():
    return render_template('index.html', species=species_list)

@app.route('/species/<int:species_id>')
def species_detail(species_id):
    sp = get_species(species_id)
    if not sp:
        abort(404)
    return render_template('species.html', species=sp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
