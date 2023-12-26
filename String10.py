def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    return "(%d+%d)*2=%d"%(x,y,(x+y)*2)
print(main(4,6))