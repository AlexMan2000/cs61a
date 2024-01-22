

def cascade(n):
    if n == 10:
        print(n)
        return

    print(n)
    cascade(n+1)
    print(n)


if __name__ == "__main__":
    cascade(1)