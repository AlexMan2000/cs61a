

def cascade(n):
    if n == 10:
        print(n)
        return

    print(n)
    cascade(n+1)
    print(n)


if __name__ == "__main__":
    import re
    print(re.match("([^/]*$)", "23232bds: sfs/fsd/s"))