from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    nombre_usuario = request.form["first_name"]
    total_frutas = int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"])
    print (f"Cobrando a {nombre_usuario} por {total_frutas} frutas")
    return render_template("checkout.html",  datos = request.form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)