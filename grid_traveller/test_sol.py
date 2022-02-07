import grid_traveller.sol as sol

gt = sol.GridTraveller()


def test_gt():
    assert gt.gt(1, 1) == 1
    assert gt.gt(2, 3) == 3
    assert gt.gt(3, 2) == 3
    assert gt.gt(3, 3) == 6
    assert gt.gt(18, 18) == 2333606220
