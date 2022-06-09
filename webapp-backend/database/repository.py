import uuid
from peewee import *
import datetime
import json
import components.product as product

db = SqliteDatabase('./database/database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Order(BaseModel):
    uid = IntegerField()
    usr_name = TextField()
    ordr = TextField()
    ordr_id = TextField(default=uuid.uuid4())
    ordr_nt = TextField(null=True)
    crt_date = DateTimeField(default=datetime.datetime.now())

def create_order(uid, usr_name, ordr, ordr_id, dt):
    return Order.create(uid=uid, usr_name=usr_name, ordr=ordr, ordr_id=ordr_id, crt_date=dt)

def get_last_order_sum(uid, nt):
    o = Order.select().where(Order.uid == uid).order_by(Order.crt_date.desc()).get()

    if o.ordr:
        o.ordr_nt = nt
        o.save()
        sum = 0
        for i in json.loads(o.ordr):
            sum = sum + ( int(product.get_product_price(i['id'])) * int(i['count']) )
        
        return sum + product.get_delivery_price()
    else:
        return False

#db.create_tables([Order])