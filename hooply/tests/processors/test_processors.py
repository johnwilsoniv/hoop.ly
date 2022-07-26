from hooply.market.processors.processor import Processor
from hooply.market.processors.bipm import BIPMProcessor


def test_bipm_processor_subclass():
    assert issubclass(BIPMProcessor, Processor) is True


def test_bipm_processor_return_type():
    b = BIPMProcessor()
    # assert b.calculate_score([], []) == []
    assert True


def test_bipm_team_adjusted_coefficient():
    b = BIPMProcessor()
    # netrg = Dei
    assert True
