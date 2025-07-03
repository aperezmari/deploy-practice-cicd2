from flask import Flask, jsonify

app = Flask(__name__)

# --- Funciones internas -------------------------------------------
def multiplicar(a: int, b: int) -> int:
    return a * b

def es_par(n: int) -> bool:
    return n % 2 == 0

# --- Rutas ---------------------------------------------------------
@app.route("/")
def home():
    return "¡Hola, Mundo!"

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return jsonify(resultado=a + b)

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre.capitalize()}!"

# --- Punto de entrada ---------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
