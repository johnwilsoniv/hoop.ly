import datetime
from hooply.market.models.base import BaseModel
from peewee import AutoField, TextField, TimestampField


class MetaIngestion(BaseModel):
    id = AutoField()
    timestamp = TimestampField(default=datetime.datetime.now())
    type = TextField()
