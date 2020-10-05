from flask import Flask, Response, render_template, request, jsonify
import json
import pandas as pd

app = Flask(__name__)

# data = [{
#   "producto": "bootstrap-table",
#   "marca": "10",
#   "marca": "122",
#   "stock": "An extended Bootstrap table"
# },
#  {
#   "producto": "multiple-select",
#   "marca": "288",
#   "marca": "20",
#   "stock": "A jQuery plugin"
# }, {
#   "producto": "Testing",
#   "marca": "340",
#   "marca": "20",
#   "stock": "For test"
# }]
df = pd.read_csv(r'/home/dgasch/Descargas/data-1560959662257.csv')
# df.columns=['index', 'descripcion', 'codigo', 'kg', 'tipo', 'arriba', 'abajo']
# df['proveedor']='proplan'
df=df.dropna(subset=['codigo'])
df['codigo']=df['codigo'].astype(int)
df=df.where((pd.notnull(df)), None)
# print(data)
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "state", # which is the field's name of data key
    "checkbox":"true"
  },
  {
    "field": "tipo",
    "title": "Tipo",
    "data-filter-control":"select",
    "data-sortable":"true"
  },
  {
    "field": "producto",
    "title": "Producto",
    "searchable":"input"
  },
  {
    "field": "marca",
    "title": "Marca",
    "filter-control":"input"
  },
  {
    "field": "kg",
    "title": "Kg",
    "filter-control":"input"
  },
  {
    "field": "precio",
    "title": "Precio",
    "filter-control":"input"
  },
  {
    "field": "arriba",
    "title": "Stock",
    "filter-control":"input"
  },
  {
    "field": "abajo",
    "title": "Deposito",
    "filter-control":"input"
  },
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("search.html",
      columns=columns,
      title='Flask Bootstrap Table')
@app.route('/data')
def updateInventario():
        return jsonify(df[['descripcion', 'codigo', 'tipo', 'arriba', 'abajo','proveedor','precio','kg','categoria']].to_dict('records'))


@app.route('/updateInventario',methods=['GET'])
def datos():
        codigo = request.args.get('codigo')
        print(df[df['codigo']==int(codigo)])
        df.loc[df['codigo']==int(codigo),['arriba']]=df[df['codigo']==int(codigo)]['arriba']+1
        df.loc[df['codigo']==int(codigo),['abajo']]=df[df['codigo']==int(codigo)]['abajo']-1
        print(df[df['codigo']==codigo])
        return('OK')
if __name__ == '__main__':
	#print jdata
  app.run(debug=True, host="0.0.0.0")
