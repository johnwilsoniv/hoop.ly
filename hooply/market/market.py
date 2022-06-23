from hooply.market.models import init_db, MODELS
from hooply.market.pipeline.pipeline import init_pipeline


def main() -> None:
    # Bring up a fresh database
    # db = init_db()
    # Load data
    init_pipeline()


if __name__ == '__main__':
    main()
