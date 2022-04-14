from flask import Flask, render_template, request, Response
app = Flask(__name__)

import geopandas as gpd

gdfRip = gpd.read_file('/workspace/flask/Limiti/ripartizioni/RipGeo01012021_WGS84.shp')
gdfReg = gpd.read_file('/workspace/flask/Limiti/regioni/Reg01012021_WGS84.shp')
gdfProv = gpd.read_file('/workspace/flask/Limiti/province/ProvCM01012021_WGS84.shp')
gdfCom = gpd.read_file('/workspace/flask/Limiti/comuni/Com01012021_WGS84.shp')

@app.route('/', methods=['GET'])
def elenco_ripartizioni():
    return render_template('url_elencoRip.html', nomi=gdfRip['DEN_RIP'].to_list(), codici=gdfRip['COD_RIP'].to_list())

@app.route('/regioni', methods=['GET'])
def regioni():
    gdfRegioni = gdfReg[gdfReg['COD_RIP']==int(request.args['id'])]
    return render_template('url_elencoReg.html', nomi=gdfRegioni['DEN_REG'].to_list(), codici=gdfRegioni['COD_REG'].to_list())


@app.route('/province', methods=['GET'])
def province():
    gdfProvince = gdfProv[gdfProv['COD_REG']==int(request.args['id'])].sort_values(by='DEN_UTS')
    return render_template('url_elencoProv.html', nomi=gdfProvince['DEN_UTS'].to_list(), codici=gdfProvince['COD_PROV'].to_list())


@app.route('/comuni/<id>', methods=['GET'])
def comuni(id):
    gdfComuni = gdfCom[gdfCom['COD_PROV']==int(id)].sort_values(by='COMUNE')
    return render_template('url_elencoCom.html', nomi=gdfComuni['COMUNE'].to_list(), codici=gdfComuni['PRO_COM'].to_list())


import folium
@app.route('/comune/<int:id>', methods=['GET'])
def comune(id):
    comuneScelto = gdfCom[gdfCom['PRO_COM']==id]
    start_coords = (comuneScelto.to_crs(epsg=4326).representative_point().geometry.y, comuneScelto.to_crs(epsg=4326).representative_point().geometry.x)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map.save('templates/map.html')
    return render_template('url_infocomune.html', nome=comuneScelto['COMUNE'].values[0], codice=comuneScelto['PRO_COM'].values[0])

import io
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

@app.route('/mappa/<int:id>', methods=['GET'])
def mappa(id):

    comuneScelto = gdfCom[gdfCom['PRO_COM']==id]
    fig, ax = plt.subplots(figsize = (12,8))
    comuneScelto.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)