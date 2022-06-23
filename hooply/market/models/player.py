from hooply.market.models.base import BaseModel
from peewee import TextField


class Player(BaseModel):
    name = TextField()
    slug = TextField()
    position = TextField()
    height = TextField()
    weight = TextField()
