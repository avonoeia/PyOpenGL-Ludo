def onClickDetectPier(x, y):
    if x >= 30 and x <= 225:
        if y >= -45 and y <= 45:
            return "pierHorizontalRight"
    if x <= -30 and x >= -225:
        if y >= -45 and y <= 45:
            return "pierHorizontalLeft"
    if x >= -45 and x <= 45:
        if y >= 45 and y <= 225:
            return "pierVerticalTop"
    if x >= -45 and x <= 45:
        if y <= -45 and y >= -225:
            return "pierVerticalBottom"
        
    return False


def onClickDetectCoordinates(x, y):
    xCoordinate = None
    yCoordinate = None

    if onClickDetectPier(x, y) == "pierHorizontalRight":
        x -= 45
        xCoordinate = x // 30
        if y > 15:
            yCoordinate = 1
        elif y < -15:
            yCoordinate = -1
        else: 
            yCoordinate = 0

    elif onClickDetectPier(x, y) == "pierHorizontalLeft":
        x += 45
        xCoordinate = abs(x) // 30
        xCoordinate = -xCoordinate if xCoordinate != 0 else xCoordinate
        if y > 15:
            yCoordinate = 1
        elif y < -15:
            yCoordinate = -1
        else: 
            yCoordinate = 0

    elif onClickDetectPier(x, y) == "pierVerticalTop":
        y -= 45
        yCoordinate = y // 30
        if x > 15:
            xCoordinate = 1
        elif x < -15:
            xCoordinate = -1
        else: 
            xCoordinate = 0
        
    elif onClickDetectPier(x, y) == "pierVerticalBottom":
        y += 45
        yCoordinate = abs(y) // 30
        yCoordinate = -yCoordinate if yCoordinate != 0 else yCoordinate
        if x > 15:
            xCoordinate = 1
        elif x < -15:
            xCoordinate = -1
        else: 
            xCoordinate = 0
    if xCoordinate == None or yCoordinate == None:
        return False
    return (int(xCoordinate), int(yCoordinate))


