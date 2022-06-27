from hooply.market.market import main
from unittest.mock import patch, MagicMock


@patch("hooply.market.market.init_pipeline")
@patch("hooply.market.market.init_db")
def test_main(mock_init_db: MagicMock, mock_init_pipeline: MagicMock):
    main()

    assert mock_init_db.called is True
    assert mock_init_pipeline.called is True
