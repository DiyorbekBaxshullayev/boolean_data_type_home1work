def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x=pow(a,1/2)
    if a/x==x:
        return True
    return False
print(main(100))