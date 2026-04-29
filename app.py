from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/envoyer', methods=['POST'])
def envoyer():
    zone = request.form.get('zone')
    age = request.form.get('age')
    maladie = request.form.get('maladie')
    print(f"Collecte: {zone} | Pathologie: {maladie}")
    return f"<h2>Enregistré !</h2><p>Zone: {zone}</p><a href='/'>Retour</a>"

if __name__ == '__main__':
    app.run()
