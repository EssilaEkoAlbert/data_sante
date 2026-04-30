from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import io

app = Flask(__name__)


donnees_sante = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    zone = request.form.get('zone')
    age = request.form.get('age')
    diagnostic = request.form.get('diagnostic')
    
    
    if zone and age and diagnostic:
        donnees_sante.append({
            'zone': zone,
            'age': age,
            'diagnostic': diagnostic
        })
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # POINT 1 & 5 : Visualisation et Carte
    return render_template('dashboard.html', donnees=donnees_sante)

@app.route('/export')
def export():
    # POINT 4 : Exportation CSV (ouvrable dans Excel)
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Zone de Sante', 'Age', 'Diagnostic'])
    for d in donnees_sante:
        cw.writerow([d['zone'], d['age'], d['diagnostic']])
    output = si.getvalue()
    return Response(output, mimetype="text/csv", headers={"Content-disposition":"attachment; filename=rapport_sante.csv"})

if __name__ == '__main__':
    app.run(debug=True)
