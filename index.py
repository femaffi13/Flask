from flask import Flask, render_template 
app = Flask(__name__)

#-----------------------------------#
# @app.route('/') #Decorador. Defino la ruta raíz
# def principal(): #Método
#     return "Sitio web en Flask"
#-----------------------------------#
@app.route('/')
def principal():
    return render_template('index.html') #Busca por defecto en la carpeta de templates

#-----------------------------------#
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
#-----------------------------------#

if __name__ == '__main__':
    app.run(
        debug=True, #Para ver los cambios realizados sin detener y levantar el servidor
        port=5017 #Para cambiar el puerto que está por defecto
        ) 