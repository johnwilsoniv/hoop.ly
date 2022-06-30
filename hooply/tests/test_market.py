from unittest.mock import MagicMock, patch

from hooply.market.market import main


@patch("hooply.market.market.init_pipeline")
@patch("hooply.market.market.init_db")
def test_main(mock_init_db: MagicMock, mock_init_pipeline: MagicMock):
    main()

    assert mock_init_db.called is True
    assert mock_init_pipeline.called is True
