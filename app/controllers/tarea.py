from flask import render_template, request, redirect, session, flash
from app.models.tareas import Job
from app.models.usuarios import Usuario
from app import app



#1_PROCESAR EL FORMULARIO DE TAREAS 

@app.route('/procesar_tarea', methods=['POST'])
def procesar_tarea():
    if "usuario" not in session:
        return redirect('/login')
    print("POST: RESULTADO", request.form)

    data = {
        'usuarios_id': session["usuario"]["usuario_id"],
        'nombre_tarea': request.form['nombre_tarea'],
        'descripcion': request.form['descripcion'],
    }
    Job.save(data)
    flash('Tarea creada, correctamente', 'success')
    return redirect('/index')

#2_PROCESAR EL FORMULARIO DE TRAE DATA DEL GET_ALL AGREGA LOS DATOS EN LA PAGINA BACKLOG

@app.route('/tabla_backlog/')
def tabla_backlog():
    if 'usuario' not in session:
        return redirect('/login')
    data = {
        **request.form,  # REVISAR
        'usuario_id': session['usuario']['usuario_id']
    }     
    jobs = Job.get_all()
    return render_template('tabla_backlog.html', data=jobs)


#3_/Tabla: De tareas que estan incluidas en el calendario.

@app.route('/tabla_calendario/')
def tabla_calendario():
    if 'usuario' not in session:
        return redirect('/login')
    data = {  # Quizás sobra
        **request.form,  # REVISAR
        'usuario_id': session["usuario"]["usuario_id"]
    }     
    jobs = Job.get_my_job()
    return render_template('tabla_calendario.html', data=jobs)


#4_FUNCION ELIMINA UN REGISTRO INGRESADO 
@app.route('/delete/<int:id>/')
def delete(id):
    if 'usuario' not in session:
        return redirect('/login')
    data = {'id': id}
    Job.delete(data)
    flash('Tarea Eliminada, correctamente', 'success')
    return redirect('/tabla_backlog')


#5_FUNCION QUE DEBE EDITAR LOS DATOS DE JOB
@app.route('/edit/<int:id>', methods=['POST'])
def procesar_edit(id):
    if 'usuario' not in session:
        return redirect('/login')
    data = {
        'id': id,
        'nombre_tarea': request.form['nombre_tarea'],
        'descripcion': request.form['descripcion'],
    }
    Job.update(data)
    print(id)
    flash('Tarea actualizada correctamente', 'success')
    return redirect('/tabla_backlog')

#6_FUNCION QUE AGREGA UNA TAREA A LA TABLA CALENDARIO.
@app.route('/join/<int:id>')
def join(id):
    data = Job.get_my_job(id)
    flash('Usuario agregado, correctamente', 'success')
    return render_template('dashboard.html', job=data) 



#7_FUNCION QUE EDITA TAREA.
@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario' not in session:
        return redirect('/login')
    return render_template('editar.html')

#8_FUNCION QUE MUESTRA EL DASHBOARD
@app.route('/dasboard/')
def dasboard():
    return render_template('/dasboard.html')

#9_FUNCION QUE MUESTRA EL CALENDARIO.
@app.route('/fullcalendar/')
def fullcalendar():
    """Renderiza el calendario."""

    return render_template('fullcalendar.html')

#8_FUNCION QUE MUESTRA EL INICIO.

@app.route('/index')
def index():
    return render_template('/index.html')

