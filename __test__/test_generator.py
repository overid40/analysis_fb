def squares(n=10):  # yield는 루프가 끝날 때까지 계속 리스트에 담아줌
    for i in range(n+1):
        yield i**2


for x in squares(10):
    print(x)

