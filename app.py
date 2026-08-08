from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="Inicio")

@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html', titulo="Pagina 1")

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html', titulo="Pagina 2")

@app.route('/pagina3', methods=['GET', 'POST'])
def pagina3():
    mensaje_enviado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje_enviado = f"Gracias {nombre}, recibimos tu mensaje en {correo}"
    return render_template('pagina3.html', titulo="Pagina 3", resultado=mensaje_enviado)

@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html', titulo="Pagina 4")

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return render_template('saludo.html', titulo="Saludo", nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
