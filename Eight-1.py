# import  turtle as t 
# t.pensize(5)
# t.right(90)
# t.forward(100)
# t.delay(3)

# t.right(90)
# t.forward(100)
# t.delay(3)

# t.right(90)
# t.forward(100)
# t.delay(3)

# t.right(90)
# t.forward(100)
# t.delay(3)

# t.goto(150, 150)
# t.circle(150)

k = []
with open ('c:\\dd\\c2.txt', 'r', encoding='utf8') as f:
    for i in range(3):
        k.append(f.readline().split())

for i in range(3):
    k[i][1] = int(k[i][1])
    print('{} 인구는 {}만명'.format(k[i][0], k[i][1]))