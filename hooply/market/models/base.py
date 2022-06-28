from peewee import Model, MySQLDatabase

db = MySQLDatabase(
    database="hooply",
    host="localhost",
    port=3306,
    user="root",
    password="test",
    # pragmas={"journal_mode": "wal", "cache_size": 10000, "foreign_keys": 1},
)


class BaseModel(Model):
    class Meta:
        database = db
