from peewee import AutoField, TextField

from hooply.market.models.base import BaseModel


class Player(BaseModel):
    id = AutoField()
    name = TextField()
    # slug = TextField()
    position = TextField()
    height = TextField()
    weight = TextField()

    def __str__(self):
        return "<{0}: {1}>".format(self.__class__, self.name)
