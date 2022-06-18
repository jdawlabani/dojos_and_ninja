from operator import methodcaller
from flask import Flask, render_template, redirect, request
from dojo import Dojo
from ninja import Ninja

app = Flask(__name__)
app.secret_key = 'Hush child'

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    return render_template('all_dojos.html', dojos = Dojo.get_all())

@app.route('/dojos/create', methods=['post'])
def create_dojo():
    Dojo.create({'name': request.form['name']})
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {'id': id}
    dojo = Dojo.get_by_id_with_ninjas(data)
    print(dojo)
    return render_template('show_dojo.html', dojo = dojo)

@app.route('/ninjas')
def new_ninja():
    return render_template("ninja.html", dojos = Dojo.get_all())

@app.route('/ninjas/create', methods=['post'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id'],
    }
    Ninja.create(data)
    link = '/dojos/' + str(data['dojo_id'])
    return redirect(link)

if __name__ == '__main__':
    app.run(debug=True)