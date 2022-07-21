from hooply.market.processors import *
from hooply.market.processors.coefficient import Coefficient


LEBRON_POS = 2.3
LEBRON_ROLE = 1.0


def test_coefficient_results():
    assert Coefficient(*BIPM_PTS).get_coefficient(LEBRON_POS) == 0.860
    assert Coefficient(*BIPM_3PM).get_coefficient(LEBRON_POS) == 0.389
    assert Coefficient(*BIPM_AST).get_coefficient(LEBRON_POS) == 0.728
    assert Coefficient(*BIPM_TO).get_coefficient(LEBRON_POS) == -0.964
    assert Coefficient(*BIPM_ORB).get_coefficient(LEBRON_POS) == 0.473
    assert Coefficient(*BIPM_DRB).get_coefficient(LEBRON_POS) == 0.137
    assert Coefficient(*BIPM_STL).get_coefficient(LEBRON_POS) == 1.252
    assert Coefficient(*BIPM_BLK).get_coefficient(LEBRON_POS) == 1.124
    assert Coefficient(*BIPM_PF).get_coefficient(LEBRON_POS) == -0.367

    assert Coefficient(*BIPM_FGA).get_coefficient(LEBRON_ROLE) == -0.560
    assert Coefficient(*BIPM_FTA).get_coefficient(LEBRON_ROLE) == -0.246