from hooply.market.processors.processor import BIPMProcessor, Processor


def test_bipm_processor_subclass():
    assert issubclass(BIPMProcessor, Processor) is True


def test_bipm_processor_return_type():
    b = BIPMProcessor()
    assert b.calculate_score([], []) == []
