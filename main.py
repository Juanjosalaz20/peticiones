from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/buscar')
def buscar():
    producto = request.args.get('producto')
    talla = request.args.get('tamano')
    color = request.args.get('color')
    if producto is None and talla is None and color is None:
     return 'Faltan datos para la busqueda'

    return f"Buscando {producto} de talla {talla} y color {color}"

@app.route('/registro', methods=['GET'])
def ruta_formulario():
   return render_template('formulario.html')

@app.route('/registro', methods=['POST'])
def ruta_registro():
   nombre=request.form.get('estudiante')
   email=request.form.get('email')
   password=request.form.get('password')
   return f'Usuario registrado: {nombre}, {email}'













if __name__=='__main__':
    app.run(debug=True)