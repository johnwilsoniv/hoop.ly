import datetime

from peewee import AutoField, TextField, TimestampField

from hooply.market.models.base import BaseModel


class MetaIngestion(BaseModel):
    id = AutoField()
    timestamp = TimestampField(default=datetime.datetime.now())
    type = TextField()
