from flask import Flask, render_template, request
import math

app= Flask(__name__)
@app.route('/')
def home():
    return "Hello world"

@app.route('/index')
def index():
    titulo="IEVN1001"
    listado=["Python","Flask","HTML","CSS","Javascript"]
    return render_template('index.html', titulo=titulo, listado=listado)


@app.route('/aporb')
def aporb():
    return render_template('aporb.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    n1= request.form.get("a")
    n2= request.form.get("b")
    return "La multiplicacion de {} y {} es {}".format(n1,n2,int(n1)*int(n2))

@app.route('/distancia', methods=['GET','POST'])
def distancia():
    resultado1=0.0
    resultado=0.0
    if request.method=='POST':
        x1=request.form.get("equis1")
        y1=request.form.get("igriega1")
        x2=request.form.get("equis2")
        y2=request.form.get("igriega2")
        resultado1=math.sqrt(((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2)) 
        resultado="La distacia es de {}".format(resultado1)
    return render_template('distancia.html', resultado=resultado)
    
@app.route("/figuras", methods=['GET', 'POST'])
def figuras():
    resultado = ""
    
    if request.method == 'POST':
        figura = request.form.get("figura")
        valor1 = request.form.get("valor1")
        valor2 = request.form.get("valor2")

        try:
            if figura == "cuadrado":
                lado = float(valor1)
                area = lado ** 2
                resultado = "El área del cuadrado es {:.2f}".format(area)

            elif figura == "triangulo":
                base = float(valor1)
                altura = float(valor2)
                area = (base * altura) / 2
                resultado = "El área del triángulo es {:.2f}".format(area)

            elif figura == "circulo":
                radio = float(valor1)
                area = math.pi * (radio ** 2)
                resultado = "El área del círculo es {:.2f}".format(area)

            elif figura == "pentagono":
                lado = float(valor1)
                perimetro = 5 * lado
                apotema = lado / (2 * math.tan(math.pi / 5))
                area = (perimetro * apotema) / 2
                resultado = "El área del pentágono es {:.2f}".format(area)

            else:
                resultado = "⚠️ Selecciona una figura válida."
        except:
            resultado = "⚠️ Error: verifica los datos ingresados."

    return render_template('figuras.html', resultado=resultado)

@app.route("/hola")
def func():
    return "<h1>Holaaaa</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "<h1>Hasta la proximaaaaa{}</h1>".format(user)

@app.route("/square/<int:num>")
def square(num):
    return "<h1>The square of {} is {}</h1>".format(num, num*2)

@app.route("/repeat/<string:text>/<int:times>")
def repeat(text, times):
    return "<h1>"+" ".join([text]*times)+"</h1>"

@app.route("/suma/<float:a>/<float:b>")
def suma(a,b):
    return "<h1>The sum of {} and {} is {}.</h1>".format(a,b,a+b)



if __name__=='__main__':
    app.run(debug=True)