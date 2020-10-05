from flask import abort, flash, redirect, render_template, url_for,jsonify,request
from flask_login import current_user, login_required
import pandas as pd
from sqlalchemy.inspection import inspect
import flask_excel as excel

from . import home

from .forms import AlimentoForm,EanForm
from .. import db
from ..models import Alimento, Venta
import datetime

def query_to_list(rset):
    """List of result
    Return: columns name, list of result
    """
    result = []
    for obj in rset:
        instance = inspect(obj)
        items = instance.attrs.items()
        result.append([x.value for _,x in items])
    return instance.attrs.keys(), result
@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/alimentos', methods=['GET', 'POST'])
def list_alimentos():
    """
    List all alimentos
    """

    alimentos = Alimento.query.all()

    return render_template('home/alimentos/alimentos.html',
                           alimentos=alimentos, title="Alimento")


@home.route('/alimentos/add', methods=['GET', 'POST'])
def add_alimento():
    """
    Add a alimento to the database
    """
    add_alimento = True

    form = AlimentoForm()
    if form.validate_on_submit():
        alimento = Alimento(tipo = form.tipo.data,codigo = form.codigo.data
                                ,categoria = form.categoria.data,proveedor = form.proveedor.data,descripcion = form.descripcion.data
                                ,kg = form.kg.data,precio = form.precio.data,ean = form.ean.data,arriba = form.arriba.data
                                ,abajo = form.abajo.data)
        try:
            # add alimento to the database
            db.session.add(alimento)
            db.session.commit()
            flash('You have successfully added a new alimento.')
        except:
            # in case alimento name already exists
            flash('Error: alimento name already exists.')

        # redirect to alimentos page
        return redirect(url_for('home.list_alimentos'))

    # load alimento template
    return render_template('home/alimentos/alimento.html', action="Add",
                           add_alimento=add_alimento, form=form,
                           title="Add alimento")


@home.route('/alimentos/edit/<id>', methods=['GET', 'POST'])
def edit_alimento(id):
    """
    Edit a alimento
    """

    add_alimento = False

    alimento = Alimento.query.get_or_404(id)
    form = AlimentoForm(obj=alimento)
    if form.validate_on_submit():
        alimento.tipo = form.tipo.data
        alimento.categoria = form.categoria.data
        alimento.proveedor = form.proveedor.data
        alimento.descripcion = form.descripcion.data
        alimento.kg = form.kg.data
        alimento.precio = form.precio.data
        alimento.ean = form.ean.data
        alimento.arriba = form.arriba.data
        alimento.abajo = form.abajo.data
        db.session.commit()
        flash('You have successfully edited the alimento.')

        # redirect to the alimentos page
        return redirect(url_for('home.list_alimentos'))

    form.tipo.data=alimento.tipo
    form.categoria.data= alimento.categoria
    form.proveedor.data= alimento.proveedor
    form.descripcion.data= alimento.descripcion
    form.kg.data= alimento.kg
    form.precio.data= alimento.precio
    form.ean.data= alimento.ean
    form.arriba.data= alimento.arriba
    form.abajo.data= alimento.abajo
    return render_template('home/alimentos/alimento.html', action="Edit",
                           add_alimento=add_alimento, form=form,
                           alimento=alimento, title="Edit alimento")


@home.route('/alimentos/delete/<id>', methods=['GET', 'POST'])
def delete_alimento(id):
    """
    Delete a alimento from the database
    """
    check_home()

    alimento = alimento.query.get_or_404(id)
    db.session.delete(alimento)
    db.session.commit()
    flash('You have successfully deleted the alimento.')

    # redirect to the alimentos page
    return redirect(url_for('home.list_alimentos'))

    return render_template(title="Delete alimento")


@home.route('/alimentos/inventario/<id>', methods=['GET', 'POST'])
def mover_alimento(id):
    """
    Edit a alimento
    """

    add_alimento = False

    alimento = Alimento.query.get_or_404(id)
    alimento.arriba = alimento.arriba+1
    alimento.abajo = alimento.abajo-1
    db.session.commit()
    flash('You have successfully edited the alimento.')

        # redirect to the alimentos page
    return redirect(url_for('home.list_alimentos'))

@home.route('/alimentos/vender/<id>', methods=['GET', 'POST'])
def vender_alimento(id):
    """
    Vender a alimento
    """

    add_alimento = False

    alimento = Alimento.query.get_or_404(id)
    if alimento.arriba >0:
        alimento.arriba = alimento.arriba-1
    else:
        alimento.abajo = alimento.abajo-1
    db.session.commit()

    venta = Venta(codigo=id,tipo =alimento.tipo,    categoria = alimento.categoria,    proveedor = alimento.proveedor,    descripcion = alimento.descripcion,    kg = alimento.kg,    precio = alimento.precio,    ean = alimento.ean)
    try:
        # add alimento to the database
        db.session.add(venta)
        db.session.commit()
        flash('You have successfully added a new venta.')
    except:
        # in case alimento name already exists
        flash('Error: no se pudo procesar la venta')

        # redirect to the alimentos page
    return redirect(url_for('home.list_alimentos'))

@home.route('/alimentos/ean/', methods=['GET', 'POST'])
def add_ean():
    """
    Add a alimento to the database
    """
    if request.method == 'POST':
        alimento = Alimento.query.get_or_404(id)
        alimento.ean = request.values.get('ean')
        db.session.commit()
        flash('You have successfully edited the alimento.')

    # load alimento template
    return render_template('home/alimentos/ean.html',
                           title="Agregar Ean")
@home.route('/alimentos/busqueda', methods=['GET', 'POST'])
def busqueda():
    if request.args.get('codigo') != None and len(request.args.get('codigo') ) >2:
        names, data = query_to_list(Alimento.query.filter(Alimento.codigo.like("%"+request.args.get('codigo')+"%")).all())
    elif request.args.get('descripcion') != None and len(request.args.get('descripcion') ) >2:
        names, data = query_to_list(Alimento.query.filter(Alimento.descripcion.like("%"+request.args.get('descripcion')+"%")).all())
    else:
        #names, data = query_to_list(Alimento.query.all())
        return  jsonify({"total": 0,'rows':[]})
    df = pd.DataFrame.from_records(data, columns=names)
    output=df[['descripcion', 'codigo', 'tipo', 'arriba', 'abajo','proveedor','precio','kg','categoria']].to_dict('records')
    return  jsonify({"total": len(output), "totalNotFiltered": 800,'rows':output})


@home.route('/alimentos/stock', methods=['GET', 'POST'])
def update_stock():
    if request.args.get('codigo') != None and len(request.args.get('codigo') ) >2:
        names, data = query_to_list(Alimento.query.filter(Alimento.codigo.like("%"+request.args.get('codigo')+"%")).all())
    elif request.args.get('descripcion') != None and len(request.args.get('descripcion') ) >2:
        names, data = query_to_list(Alimento.query.filter(Alimento.descripcion.like("%"+request.args.get('descripcion')+"%")).all())
    else:
        #names, data = query_to_list(Alimento.query.all())
        return  jsonify({"total": 0,'rows':[]})
    df = pd.DataFrame.from_records(data, columns=names)
    output=df[['descripcion', 'codigo', 'tipo', 'arriba', 'abajo','proveedor','precio','kg','categoria']].to_dict('records')
    return  jsonify({"total": len(output), "totalNotFiltered": 800,'rows':output})

@home.route('/alimentos/subir', methods=['GET','POST'])
def subir_productos():
    if request.method == 'POST':
        df=pd.DataFrame.from_dict(request.get_array(field_name='file'))
        df.columns=df.iloc[0]
        df=df.drop(0)
        df.set_index('codigo',inplace=True)
        df.to_sql('alimento', if_exists='replace',con=db.engine)
        print(df)
        print(df.columns)

        return jsonify({"result":request.get_array(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@home.route('/alimentos/descargar', methods=['GET','POST'])
def descargar_productos():
    return excel.make_response_from_tables(db.session,[Alimento,Venta],'xls',file_name='productos')

    #
