from flask import render_template, request, redirect, session, flash
from app.models.usuarios import Usuario
from app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 


#1_/login: Renderiza la plantilla 'auth/login.html'

@app.route('/login')
def login():
    if 'usuario' in session:
        return redirect('/')
    return render_template('login.html')

#1.2_/procesar_login: Procesa el formulario de inicio de sesión enviado por POST

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    print("POST: ", request.form)
    
    usuario_encontrado = Usuario.get_by_email(request.form['email'])

    if not usuario_encontrado:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')

    login_seguro = bcrypt.check_password_hash(usuario_encontrado.password, request.form['password'])

    data = {
        "usuario_id": usuario_encontrado.id,
        "email": usuario_encontrado.email,
        "apellido": usuario_encontrado.apellido,
        "nombre": usuario_encontrado.nombre,
        "password": usuario_encontrado.password,
    }

    if login_seguro:
        session['usuario'] = data
        flash('Genial, pudiste entrar sin problemas!!!!', 'success')
        print (data)

    else:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')
    return redirect('index')


@app.route('/detalle')
def detalle():
    if 'usuario' not in session:
        return redirect('/login')
    data = {
        'usuario_id': session["usuario"]["usuario_id"],
    }
    otros_usuario = Usuario.get_otros_usuarios(data)
    return render_template('index.html', otros_usuario=otros_usuario)



#2.1_/procesar_registro: Procesa el formulario de registro enviado por POST

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    print("POST: ", request.form)
    if request.form['password'] != request.form['confirm_password']:
        flash("La contraseña no es igual", "danger")
        return redirect('/register')
    
    if not Usuario.validar(request.form):

        return redirect('/register')

    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': password_hash,
    }
    existe_usuario = Usuario.get_by_email(request.form['email'])
    if existe_usuario:
        flash("el correo ya está registrado.", "danger")
        return redirect('/register')
    resultado = Usuario.save(data)
    if resultado:
        flash("Registrado Correctamente", "success")
    else:
        flash("Errores", "danger")
        print("resultado")
    return redirect('/login')


#2_/registro: de usuario.
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/salir')
def salir():
    session.clear()
    flash('Saliste sin problemas!!!', 'info')
    return redirect('/login')

