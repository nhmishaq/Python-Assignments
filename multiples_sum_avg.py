def odd_from_0_to_1000 ():
    for num in range (1, 1000):
        if (num%2==1):
            print num

odd_from_0_to_1000()

def multiples_of_5 ():
    for num in range (5, 1000000):
        if (num%5==0):
            print num

multiples_of_5()

def sum_count():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for num in a:
        sum += num
    print sum
sum_count()

def avg_sum_count():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for num in a:
        sum += num
    avg = sum / len(a)
    print avg
avg_sum_count()


