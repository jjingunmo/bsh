'''
Sum = 0
for i in range(2, 101, 2):
    Sum = Sum + i
    #print(i, ' ==>', Sum)
print(' 1 ~ 10까지의 합 : ', Sum)


for i in range(2, 10):
    print(' *** ', i, '단 ***')
    for j in range(1, 10):
        print(i, ' * ', j, ' = '    , i*j)
    print(' ****************** ')
    

while True:
    dan = int(input(' 출력할 단 [Quit => 0] : '))
    if dan == 0:
        print(' 안녕히계세요~~~ ')
        break

    for i in range(a, 10):
        print(dan, ' * ', i, ' = ', dan*i)
'''
for i in range(7):
    if i == 2:
        #break
        continue
    print(i)

print('end')


    
