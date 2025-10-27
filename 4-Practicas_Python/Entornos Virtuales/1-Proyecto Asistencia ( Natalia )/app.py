from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(10), nullable=False, default='DNI')
    documento = db.Column(db.String(20), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    anio_inscripcion = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Alumno {self.nombre} {self.apellido}>"

@app.route('/')
def index():
    alumnos = Alumno.query.order_by(Alumno.id.desc()).limit(5).all()
    return render_template('index.html', alumnos=alumnos)

@app.route('/alumnos')
def alumnos():
    todos = Alumno.query.order_by(Alumno.apellido.asc()).all()
    return render_template('alumnos.html', alumnos=todos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    documento = request.form['documento']
    tipo = request.form['tipo']
    anio = request.form.get('anio', type=int)

    nuevo = Alumno(nombre=nombre, apellido=apellido, documento=documento, tipo_documento=tipo, anio_inscripcion=anio)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
