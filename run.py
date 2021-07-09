from flask import Flask
app = Flask(__name__)

# DECORADOR
@app.route("/<int:numero>", methods=['GET','POST'])
def ola(numero):
    return 'Ola mundo! {}'.format(numero)

# CHAMADA
if __name__ == "__main__":
    app.run(debug=True)
