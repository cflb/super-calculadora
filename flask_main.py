"""Webservice para calculos matematicos"""
from flask import Flask
from aritmetica import soma, divisao

"""
  Criar um webservice para fazer calculos InMathematical_Operators
  da seguinte forma: 
   - http://localhost:5000/soma/2/3
     Resultado esperado: 5
"""

# localhost - host local - ip (internet protocol) - ip local = 127.0.0.1

app = Flask(__name__)


@app.route('/soma/<int:v1>/<int:v2>/')
def opracao_somar(v1, v2):
    return str(soma(v1, v2))

@app.route('/divisao/<int:v1>/<int:v2>/')
def opracao_divisao(v1, v2):
    return str(divisao(v1, v2))


if __name__ == "__main__":
    app.run(debug=True)
