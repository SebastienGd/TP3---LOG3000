"""
Point d'entrée principal de l'application Flask Calculator.
Interprète les expressions, relie l'interface au traitement arithmétique et gère le serveur web.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse l'expression arithmétique de l'utilisateur et l'évalue afin de renvoyer le résultat.
    Gère au plus une opération binaire à la fois avec une séparation stricte des opérandes gauche/droite.
    
    Args:
        expr (str): L'expression arithmétique entière capturée par le front-end.
        
    Returns:
        float/int: Le numérique final modélisant la réponse au calcul.
        
    Raises:
        ValueError: Si le format d'expression est vide, invalide (sans opérateur, opérateurs multiples) 
                    ou en présence d'opérandes illisibles (non-nombres).
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Détermine la réponse à adresser à l'utilisateur ciblant la racine du site web.
    En POST (calcul soumis par le clique sur le bouton "egal"), évalue l'expression affichée.
    
    Returns:
        str: Modèle index.html restitué par Jinja, injectant la variable 'result'.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)