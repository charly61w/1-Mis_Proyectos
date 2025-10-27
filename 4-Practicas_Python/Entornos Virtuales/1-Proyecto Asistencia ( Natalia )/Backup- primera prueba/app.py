# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Modelo de prueba para alumnos
class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(10), nullable=False, default='DNI')
    documento = db.Column(db.String(20), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Alumno {self.nombre} {self.apellido}>"

@app.route('/')
def index():
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    documento = request.form['documento']
    tipo = request.form['tipo']

    nuevo = Alumno(nombre=nombre, apellido=apellido, documento=documento, tipo_documento=tipo)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
