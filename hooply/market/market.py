from hooply.market.models import init_db, MODELS


def main() -> None:
    # Bring up a fresh database
    db = init_db()
    db.drop_tables(MODELS)
    db.create_tables(MODELS)



if __name__ == '__main__':
    pass