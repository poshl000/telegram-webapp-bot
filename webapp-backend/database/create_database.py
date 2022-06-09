# Run it once to create db file

import uuid
from peewee import *
import datetime

db = SqliteDatabase('database.db')

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

db.create_tables([Order])