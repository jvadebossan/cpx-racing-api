# from flask import Flask
# from App.routes import app as routes
# #import cors
# from flask_cors import CORS

# app: Flask = Flask(__name__)
# CORS(app)

# app.config.update(
#     JSON_SORT_KEYS=False,
#     JSON_AS_ASCII=False
# )

# app.logger.disabled = True
# app.register_blueprint(routes)

# if __name__ == "__main__":
#     app.run(debug=True)


from utils.dbconnect import mongoConnect
from utils.response import res
from flask import request, Flask

app = Flask(__name__)

cluster = mongoConnect()
db = cluster["site"]
infos = db["info"]


@app.route('/api/info', methods=['GET'])
def info():
    try:
        obj = infos.find_one({'_id':0})
        return res(data=obj, status=200)
    except:
        import traceback
        traceback.print_exc()
        return res(data="Erro", status=500)

def favicon():
    return app.send_static_file("favicon.ico")