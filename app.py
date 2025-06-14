import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Obtener el puerto asignado por Render o usar 5000 localmente
    port = int(os.environ.get("PORT", 5000))
    # Ejecutar la aplicación vinculada a 0.0.0.0
    app.run(debug=False, host='0.0.0.0', port=port)