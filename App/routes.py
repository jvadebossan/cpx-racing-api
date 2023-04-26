from utils.dbconnect import mongoConnect
from utils.response import res
from flask import request, Blueprint

app: Blueprint = Blueprint("routes", __name__)

cluster = mongoConnect()
db = cluster["site"]
infos = db["info"]


@app.route('/api/info', methods=['GET'])
def info():
    print('recieved')
    try:
        obj = infos.find_one({'_id':0})
        return res(data=obj, status=200)
    except:
        import traceback
        traceback.print_exc()
        return res(data="Erro", status=500)

def favicon():
    return app.send_static_file("favicon.ico")