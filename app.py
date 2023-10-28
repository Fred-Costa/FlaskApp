from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    total = 0

    if request.method == "POST":
        num1 = float(request.form['primeiroNumero'])
        num2 = float(request.form['segundoNumero'])
        operacao = request.form['operacao']

        if operacao == 'soma':
            total = num1 + num2
        elif operacao == 'subtracao':
            total = num1 - num2
        elif operacao == 'divisao':
            total = num1 / num2
        elif operacao == 'multiplicacao':
            total = num1 * num2
        return f"Resultado:  {total}"

    return render_template('resultado.html', total=total)


if __name__ == "__main__":
    app.run(debug=True)
