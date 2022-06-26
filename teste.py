from utils.dbconnect import mongoConnect

cluster = mongoConnect()
print('connected')

db = cluster["site"]
info = db["info"]


teste = info.find_one({'_id':0})
for i in range(0, 5):
    obj = {
    "img": "image link",
    "desc": "description"
    }
    info.update_one({'_id':0}, {'$push':{'sponsors':obj}})