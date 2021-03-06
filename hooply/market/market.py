from hooply.logger import setup_logger
from hooply.market.models import MODELS, init_db
from hooply.market.pipeline.pipeline import init_pipeline

logger = setup_logger(__name__)


def main() -> None:
    # Bring up a fresh database
    db = init_db()
    # Load data
    init_pipeline(db)


if __name__ == "__main__":
    main()
