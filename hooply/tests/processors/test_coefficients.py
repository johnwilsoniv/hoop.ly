from hooply.market.processors import *
from hooply.market.processors.coefficient import Coefficient


LEBRON_POS = 2.3
LEBRON_ROLE = 1.0


def test_coefficient_results():
    assert Coefficient(*BIPM_PTS).get_coefficient(LEBRON_POS) == round(Decimal(0.860), 2)
    assert Coefficient(*BIPM_3PM).get_coefficient(LEBRON_POS) == round(Decimal(0.389), 2)
    assert Coefficient(*BIPM_AST).get_coefficient(LEBRON_POS) == round(Decimal(0.728), 2)
    assert Coefficient(*BIPM_TO).get_coefficient(LEBRON_POS) == round(Decimal(-0.964), 2)
    assert Coefficient(*BIPM_ORB).get_coefficient(LEBRON_POS) == round(Decimal(0.473), 2)
    assert Coefficient(*BIPM_DRB).get_coefficient(LEBRON_POS) == round(Decimal(0.137), 2)
    assert Coefficient(*BIPM_STL).get_coefficient(LEBRON_POS) == round(Decimal(1.252), 2)
    assert Coefficient(*BIPM_BLK).get_coefficient(LEBRON_POS) == round(Decimal(1.124), 2)
    assert Coefficient(*BIPM_PF).get_coefficient(LEBRON_POS) == round(Decimal(-0.367), 2)

    assert Coefficient(*BIPM_FGA).get_coefficient(LEBRON_ROLE) == round(Decimal(-0.560), 2)
    assert Coefficient(*BIPM_FTA).get_coefficient(LEBRON_ROLE) == round(Decimal(-0.246), 2)