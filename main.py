from flask import Flask, request, render_template, make_response

app=Flask(__name__)

@app.route('/buscar')
def buscar():
    producto = request.args.get('producto')
    talla = request.args.get('tamano')
    color = request.args.get('color')
    if producto is None and talla is None and color is None:
     return 'Faltan datos para la busqueda'

    return f"Buscando {producto} de talla {talla} y color {color}"

listado = []

@app.route('/registro', methods=['GET'])
def ruta_formulario():
   return render_template('formulario.html')

#Tipo de solicitud 2: se envia informacion por el body
@app.route('/registro', methods=['POST'])
def ruta_registro():
   nombre=request.form.get('estudiante')
   email=request.form.get('email')
   password=request.form.get('password')
   if nombre and email and password:
    listado.append({'nombre': nombre, 'correo': email, 'password': password})
    return render_template('formulario.html', listado=listado)
   
   return f'Datos insuficientes'

#Tipo de solicitud 3: parametros en la ruta
@app.route('/ropa/<string:producto>/<string:talla>')
def ruta_consulta(producto, talla):
   return f'El producto consultado es: {producto} de talla {talla}'

##Tipo de solicitud 4: headers http
@app.route('/ver-headers')
def ruta_headers():
   navegador=request.headers.get('User-agent')
   return f'El navegador que hace la peticion es: {navegador}'

#Tipo de solicitud 5: manejo de cookies
@app.route('/crear_cookie')
def crear_cookie():
   respuesta = make_response('Cookie creada')
   respuesta.set_cookie('usuario_logueado', 'True')
   return respuesta

@app.route('/leer_cookie')
def leer_cookie():
   valor = request.cookies.get('usuario_logueado')
   return f'El valor de la cookie es: {valor}'







if __name__=='__main__':
    app.run(debug=True)