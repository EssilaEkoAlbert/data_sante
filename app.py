from flask import Flask, render_template, request, redirect, url_for, Response
import folium
import io
import csv

app = Flask(__name__)


donnees_sante = [
      {'zone': 'Centre', 'age': '25', 'diagnostic': 'Paludisme'}
      ]


coords = {
    "Littoral": [4.05, 9.70],
    "Centre": [3.84, 11.50],
    "Ouest": [5.47, 10.41]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    zone = request.form.get('zone')
    age = request.form.get('age')
    maladie = request.form.get('maladie')

    if zone and age and maladie:
        donnees_sante.append({
            'zone': zone,
            'age': age,
            'diagnostic': maladie
    'diagnostic'       
        })
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    
    ma_carte = folium.Map(location=[7.3697, 12.3547], zoom_start=6)

    
    for d in donnees_sante:
        zone_nom = d['zone']
        if zone_nom in coords:
            folium.CircleMarker(
                location=coords[zone_nom],
                radius=10,
                color="red",
                fill=True,
                fill_color="red",
                popup=f"{d['diagnostic']} (Âge: {d['age']})"
            ).add_to(ma_carte)

    carte_html = ma_carte._repr_html_()
    return render_template('dashboard.html', carte=carte_html, donnees=donnees_sante)

@app.route('/export')
def export():
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Zone de Sante', 'Age', 'Diagnostic'])
    for d in donnees_sante:
        cw.writerow([d['zone'], d['age'], d['diagnostic']])
    
    output = si.getvalue()
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=donnees_sanitaires.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True) 
    
