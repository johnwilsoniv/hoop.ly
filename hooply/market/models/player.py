from hooply.market.models.base import BaseModel
from peewee import AutoField, TextField


class Player(BaseModel):
    id = AutoField()
    name = TextField()
    # slug = TextField()
    position = TextField()
    height = TextField()
    weight = TextField()

    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__, self.name)
