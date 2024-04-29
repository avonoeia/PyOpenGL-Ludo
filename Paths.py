from Board import *

paths = {
    "yellowPlayerPath": {
        0: board["pierHorizontalRight"][(4, -1)][0],
        1: board["pierHorizontalRight"][(3, -1)][0],
        2: board["pierHorizontalRight"][(2, -1)][0],
        3: board["pierHorizontalRight"][(1, -1)][0],
        4: board["pierHorizontalRight"][(0, -1)][0],
        5: board["pierVerticalBottom"][(1, 0)][0],
        6: board["pierVerticalBottom"][(1, -1)][0],
        7: board["pierVerticalBottom"][(1, -2)][0],
        8: board["pierVerticalBottom"][(1, -3)][0],
        9: board["pierVerticalBottom"][(1, -4)][0],
        10: board["pierVerticalBottom"][(1, -5)][0],
        11: board["pierVerticalBottom"][(0, -5)][0],
        12: board["pierVerticalBottom"][(-1, -5)][0],
        13: board["pierVerticalBottom"][(-1, -4)][0],
        14: board["pierVerticalBottom"][(-1, -3)][0],
        15: board["pierVerticalBottom"][(-1, -2)][0],
        16: board["pierVerticalBottom"][(-1, -1)][0],
        17: board["pierVerticalBottom"][(-1, 0)][0],
        18: board["pierHorizontalLeft"][(0, -1)][0],
        19: board["pierHorizontalLeft"][(-1, -1)][0],
        20: board["pierHorizontalLeft"][(-2, -1)][0],
        21: board["pierHorizontalLeft"][(-3, -1)][0],
        22: board["pierHorizontalLeft"][(-4, -1)][0],
        23: board["pierHorizontalLeft"][(-5, -1)][0],
        24: board["pierHorizontalLeft"][(-5, 0)][0],
        25: board["pierHorizontalLeft"][(-5, 1)][0],
        26: board["pierHorizontalLeft"][(-4, 1)][0],
        27: board["pierHorizontalLeft"][(-3, 1)][0],
        28: board["pierHorizontalLeft"][(-2, 1)][0],
        29: board["pierHorizontalLeft"][(-1, 1)][0],
        30: board["pierHorizontalLeft"][(0, 1)][0],
        31: board["pierVerticalTop"][(-1, 0)][0],
        32: board["pierVerticalTop"][(-1, 1)][0],
        33: board["pierVerticalTop"][(-1, 2)][0],
        34: board["pierVerticalTop"][(-1, 3)][0],
        35: board["pierVerticalTop"][(-1, 4)][0],
        36: board["pierVerticalTop"][(-1, 5)][0],
        37: board["pierVerticalTop"][(0, 5)][0],
        38: board["pierVerticalTop"][(1, 5)][0],
        39: board["pierVerticalTop"][(1, 4)][0],
        40: board["pierVerticalTop"][(1, 3)][0],
        41: board["pierVerticalTop"][(1, 2)][0],
        42: board["pierVerticalTop"][(1, 1)][0],
        43: board["pierVerticalTop"][(1, 0)][0],
        44: board["pierHorizontalRight"][(0, 1)][0],
        45: board["pierHorizontalRight"][(1, 1)][0],
        46: board["pierHorizontalRight"][(2, 1)][0],
        47: board["pierHorizontalRight"][(3, 1)][0],
        48: board["pierHorizontalRight"][(4, 1)][0],
        49: board["pierHorizontalRight"][(5, 1)][0],
        50: board["pierHorizontalRight"][(5, 0)][0],
        51: board["pierHorizontalRight"][(4, 0)][0],
        52: board["pierHorizontalRight"][(3, 0)][0],
        53: board["pierHorizontalRight"][(2, 0)][0],
        54: board["pierHorizontalRight"][(1, 0)][0],
        55: board["pierHorizontalRight"][(0, 0)][0],
        56: (30, 0),
    },
    "greenPlayerPath": {
        0: board["pierVerticalBottom"][(-1, -4)][0],
        1: board["pierVerticalBottom"][(-1, -3)][0],
        2: board["pierVerticalBottom"][(-1, -2)][0],
        3: board["pierVerticalBottom"][(-1, -1)][0],
        4: board["pierVerticalBottom"][(-1, 0)][0],
        5: board["pierHorizontalLeft"][(0, -1)][0],
        6: board["pierHorizontalLeft"][(-1, -1)][0],
        7: board["pierHorizontalLeft"][(-2, -1)][0],
        8: board["pierHorizontalLeft"][(-3, -1)][0],
        9: board["pierHorizontalLeft"][(-4, -1)][0],
        10: board["pierHorizontalLeft"][(-5, -1)][0],
        11: board["pierHorizontalLeft"][(-5, 0)][0],
        12: board["pierHorizontalLeft"][(-5, 1)][0],
        13: board["pierHorizontalLeft"][(-4, 1)][0],
        14: board["pierHorizontalLeft"][(-3, 1)][0],
        15: board["pierHorizontalLeft"][(-2, 1)][0],
        16: board["pierHorizontalLeft"][(-1, 1)][0],
        17: board["pierHorizontalLeft"][(0, 1)][0],
        18: board["pierVerticalTop"][(-1, 0)][0],
        19: board["pierVerticalTop"][(-1, 1)][0],
        20: board["pierVerticalTop"][(-1, 2)][0],
        21: board["pierVerticalTop"][(-1, 3)][0],
        22: board["pierVerticalTop"][(-1, 4)][0],
        23: board["pierVerticalTop"][(-1, 5)][0],
        24: board["pierVerticalTop"][(0, 5)][0],
        25: board["pierVerticalTop"][(1, 5)][0],
        26: board["pierVerticalTop"][(1, 4)][0],
        27: board["pierVerticalTop"][(1, 3)][0],
        28: board["pierVerticalTop"][(1, 2)][0],
        29: board["pierVerticalTop"][(1, 1)][0],
        30: board["pierVerticalTop"][(1, 0)][0],
        31: board["pierHorizontalRight"][(0, 1)][0],
        32: board["pierHorizontalRight"][(1, 1)][0],
        33: board["pierHorizontalRight"][(2, 1)][0],
        34: board["pierHorizontalRight"][(3, 1)][0],
        35: board["pierHorizontalRight"][(4, 1)][0],
        36: board["pierHorizontalRight"][(5, 1)][0],
        37: board["pierHorizontalRight"][(5, 0)][0],
        38: board["pierHorizontalRight"][(5, -1)][0],
        39: board["pierHorizontalRight"][(4, -1)][0],
        40: board["pierHorizontalRight"][(3, -1)][0],
        41: board["pierHorizontalRight"][(2, -1)][0],
        42: board["pierHorizontalRight"][(1, -1)][0],
        43: board["pierHorizontalRight"][(0, -1)][0],
        44: board["pierVerticalBottom"][(1, 0)][0],
        45: board["pierVerticalBottom"][(1, -1)][0],
        46: board["pierVerticalBottom"][(1, -2)][0],
        47: board["pierVerticalBottom"][(1, -3)][0],
        48: board["pierVerticalBottom"][(1, -4)][0],
        49: board["pierVerticalBottom"][(1, -5)][0],
        50: board["pierVerticalBottom"][(0, -5)][0],
        51: board["pierVerticalBottom"][(0, -4)][0],
        52: board["pierVerticalBottom"][(0, -3)][0],
        53: board["pierVerticalBottom"][(0, -2)][0],
        54: board["pierVerticalBottom"][(0, -1)][0],
        55: board["pierVerticalBottom"][(0, 0)][0],
        56: (0, -30),
    },
    "bluePlayerPath": {
        0: board["pierHorizontalLeft"][(-4, 1)][0],
        1: board["pierHorizontalLeft"][(-3, 1)][0],
        2: board["pierHorizontalLeft"][(-2, 1)][0],
        3: board["pierHorizontalLeft"][(-1, 1)][0],
        4: board["pierHorizontalLeft"][(0, 1)][0],
        5: board["pierVerticalTop"][(-1, 0)][0],
        6: board["pierVerticalTop"][(-1, 1)][0],
        7: board["pierVerticalTop"][(-1, 2)][0],
        8: board["pierVerticalTop"][(-1, 3)][0],
        9: board["pierVerticalTop"][(-1, 4)][0],
        10: board["pierVerticalTop"][(-1, 5)][0],
        11: board["pierVerticalTop"][(0, 5)][0],
        12: board["pierVerticalTop"][(1, 5)][0],
        13: board["pierVerticalTop"][(1, 4)][0],
        14: board["pierVerticalTop"][(1, 3)][0],
        15: board["pierVerticalTop"][(1, 2)][0],
        16: board["pierVerticalTop"][(1, 1)][0],
        17: board["pierVerticalTop"][(1, 0)][0],
        18: board["pierHorizontalRight"][(0, 1)][0],
        19: board["pierHorizontalRight"][(1, 1)][0],
        20: board["pierHorizontalRight"][(2, 1)][0],
        21: board["pierHorizontalRight"][(3, 1)][0],
        22: board["pierHorizontalRight"][(4, 1)][0],
        23: board["pierHorizontalRight"][(5, 1)][0],
        24: board["pierHorizontalRight"][(5, 0)][0],
        25: board["pierHorizontalRight"][(5, -1)][0],
        26: board["pierHorizontalRight"][(4, -1)][0],
        27: board["pierHorizontalRight"][(3, -1)][0],
        28: board["pierHorizontalRight"][(2, -1)][0],
        29: board["pierHorizontalRight"][(1, -1)][0],
        30: board["pierHorizontalRight"][(0, -1)][0],
        31: board["pierVerticalBottom"][(1, 0)][0],
        32: board["pierVerticalBottom"][(1, -1)][0],
        33: board["pierVerticalBottom"][(1, -2)][0],
        34: board["pierVerticalBottom"][(1, -3)][0],
        35: board["pierVerticalBottom"][(1, -4)][0],
        36: board["pierVerticalBottom"][(1, -5)][0],
        37: board["pierVerticalBottom"][(0, -5)][0],
        38: board["pierVerticalBottom"][(-1, -5)][0],
        39: board["pierVerticalBottom"][(-1, -4)][0],
        40: board["pierVerticalBottom"][(-1, -3)][0],
        41: board["pierVerticalBottom"][(-1, -2)][0],
        42: board["pierVerticalBottom"][(-1, -1)][0],
        43: board["pierVerticalBottom"][(-1, 0)][0],
        44: board["pierHorizontalLeft"][(0, -1)][0],
        45: board["pierHorizontalLeft"][(-1, -1)][0],
        46: board["pierHorizontalLeft"][(-2, -1)][0],
        47: board["pierHorizontalLeft"][(-3, -1)][0],
        48: board["pierHorizontalLeft"][(-4, -1)][0],
        49: board["pierHorizontalLeft"][(-5, -1)][0],
        50: board["pierHorizontalLeft"][(-5, 0)][0],
        51: board["pierHorizontalLeft"][(-4, 0)][0],
        52: board["pierHorizontalLeft"][(-3, 0)][0],
        53: board["pierHorizontalLeft"][(-2, 0)][0],
        54: board["pierHorizontalLeft"][(-1, 0)][0],
        55: board["pierHorizontalLeft"][(0, 0)][0],
        56: (-30, 0),
    },
    "redPlayerPath": {
        0: board["pierVerticalTop"][(1, 4)][0],
        1: board["pierVerticalTop"][(1, 3)][0],
        2: board["pierVerticalTop"][(1, 2)][0],
        3: board["pierVerticalTop"][(1, 1)][0],
        4: board["pierVerticalTop"][(1, 0)][0],
        5: board["pierHorizontalRight"][(0, 1)][0],
        6: board["pierHorizontalRight"][(1, 1)][0],
        7: board["pierHorizontalRight"][(2, 1)][0],
        8: board["pierHorizontalRight"][(3, 1)][0],
        9: board["pierHorizontalRight"][(4, 1)][0],
        10: board["pierHorizontalRight"][(5, 1)][0],
        11: board["pierHorizontalRight"][(5, 0)][0],
        12: board["pierHorizontalRight"][(5, -1)][0],
        13: board["pierHorizontalRight"][(4, -1)][0],
        14: board["pierHorizontalRight"][(3, -1)][0],
        15: board["pierHorizontalRight"][(2, -1)][0],
        16: board["pierHorizontalRight"][(1, -1)][0],
        17: board["pierHorizontalRight"][(0, -1)][0],
        18: board["pierVerticalBottom"][(1, 0)][0],
        19: board["pierVerticalBottom"][(1, -1)][0],
        20: board["pierVerticalBottom"][(1, -2)][0],
        21: board["pierVerticalBottom"][(1, -3)][0],
        22: board["pierVerticalBottom"][(1, -4)][0],
        23: board["pierVerticalBottom"][(1, -5)][0],
        24: board["pierVerticalBottom"][(0, -5)][0],
        25: board["pierVerticalBottom"][(-1, -5)][0],
        26: board["pierVerticalBottom"][(-1, -4)][0],
        27: board["pierVerticalBottom"][(-1, -3)][0],
        28: board["pierVerticalBottom"][(-1, -2)][0],
        29: board["pierVerticalBottom"][(-1, -1)][0],
        30: board["pierVerticalBottom"][(-1, 0)][0],
        31: board["pierHorizontalLeft"][(0, -1)][0],
        32: board["pierHorizontalLeft"][(-1, -1)][0],
        33: board["pierHorizontalLeft"][(-2, -1)][0],
        34: board["pierHorizontalLeft"][(-3, -1)][0],
        35: board["pierHorizontalLeft"][(-4, -1)][0],
        36: board["pierHorizontalLeft"][(-5, -1)][0],
        37: board["pierHorizontalLeft"][(-5, 0)][0],
        38: board["pierHorizontalLeft"][(-5, 1)][0],
        39: board["pierHorizontalLeft"][(-4, 1)][0],
        40: board["pierHorizontalLeft"][(-3, 1)][0],
        41: board["pierHorizontalLeft"][(-2, 1)][0],
        42: board["pierHorizontalLeft"][(-1, 1)][0],
        43: board["pierHorizontalLeft"][(0, 1)][0],
        44: board["pierVerticalTop"][(-1, 0)][0],
        45: board["pierVerticalTop"][(-1, 1)][0],
        46: board["pierVerticalTop"][(-1, 2)][0],
        47: board["pierVerticalTop"][(-1, 3)][0],
        48: board["pierVerticalTop"][(-1, 4)][0],
        49: board["pierVerticalTop"][(-1, 5)][0],
        50: board["pierVerticalTop"][(0, 5)][0],
        51: board["pierVerticalTop"][(0, 4)][0],
        52: board["pierVerticalTop"][(0, 3)][0],
        53: board["pierVerticalTop"][(0, 2)][0],
        54: board["pierVerticalTop"][(0, 1)][0],
        55: board["pierVerticalTop"][(0, 0)][0],
        56: (0, 30),
    },
}






