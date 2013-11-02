#!/usr/bin/python3

def drawLine(tickLength, tickLabel=''):
    """
    Draw a line of given tickLength, followed by an optional tickLabel.
    """
    line = '-' * tickLength
    if tickLabel:
        line += ' ' + tickLabel
    print(line)

def drawInterval(centerLength):
    """
    Draw tick interval based upon a central tick length.
    """
    if centerLength > 0:
        drawInterval(centerLength - 1)
        drawLine(centerLength)
        drawInterval(centerLength - 1)

def drawRuler(inches, majorTickLength):
    """
    Draw a ruler of length inches with given majorTickLength.
    """
    drawLine(majorTickLength, '0')
    for i in range(1, inches + 1):
        drawInterval(majorTickLength + 1)
        drawLine(majorTickLength, str(i))

if __name__ == '__main__':
    drawRuler(3, 5)
    drawRuler(6, 3)
