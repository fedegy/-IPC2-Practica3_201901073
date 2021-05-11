from flask import Flask,make_response,request,jsonify

app = Flask(__name__)

@app.route('/peticion_get',methods=['GET'])
def peticion_get():
	if request.method=='GET':
		return "Es una petición GET"

@app.route('/peticion_post',methods=['POST'])
def peticion_post():
	if request.method=='POST':

		usuario=request.form.get('usuario')
		password=request.form.get('pass')

		if usuario=='admin' and password=='123':
			return "Se autentico correctamente"
		else:
			return 'Error en usuario o contraseña'
portal={
	"estudiante1":90,
	"estudiante2":58
}

@app.route('/portal/<nombre>/<nota>',methods=['PUT'])
def peticion_put(nombre,nota):
	if nota in portal:
		portal[nombre]=int(nota)
		update=make_response(jsonify(portal),200)
		return update
	#Si no hay un registro se crea el estudiante y la nota
	portal[nombre]=int(nota)
	update=make_response(jsonify(portal),2001)
	return update

@app.route('/portal/<nombre>',methods=['DELETE'])
def peticion_delete(nombre):
	if nombre in portal:
		del portal[nombre]
		el=make_response(jsonify(portal),200)
		return el
	el=make_response(jsonify({"error":"No se encuentra el estudiante"}),404)
	return el

if __name__=="__main__":
	app.run(debug=True,port=5000,threaded=True)