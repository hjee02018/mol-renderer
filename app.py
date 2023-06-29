
import os
from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/<pdb_id>')
def viewer1(pdb_id):
    pdb_filename = f'{pdb_id.upper()}.pdb'
    pdb_url = url_for('static', filename='pdbs/' + pdb_filename)
    return render_template('browse_complex.html', data_href=pdb_url)

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
