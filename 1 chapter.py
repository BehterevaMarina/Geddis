# print("marina")
# x = int(input("enter summ"))
# y = x * 0.23
# print(y)

# x = int(input("enter square metr2"))
# print("acr", x/4047)

# x = int(input("enter 1 summ"))
# x1 = int(input("enter 2 summ"))
# x2 = int(input("enter 3 summ"))
# x3 = int(input("enter 4 summ"))
# x4 = int(input("enter 5 summ"))
# summ = x+x1+x2+x3+x4
# nal = summ*0.07
# result = nal+summ
# print(f"summ 1 = {summ} \nnal = {nal:.3f} \nresult = {result}")

# x=int(input("enter C"))
# y=(9/5)*x + 32
# print(f"celc {x} \nfarengete {y}")

#1.5 стакана сахара
#1 ст. масла
#2.75 муки

#48 булок

# x = int(input("enter quality of cakes"))
#
# print(f" сахара {1.5/48*x:.2f} масла {1/48*x:.2f} муки {2.75/48*x:.2f}")

# x = int(input("men"))
# y = int(input("women"))
#
# print(f"men {x*100/(x+y):.2f}% women {y*100/(x+y):.2f}%")

# buy 2000 things
# 40 doll for share
# 3% of share
#
# sell 2000
# 42.75 doll for share
# 3 % of share

# x = 2000*40 #уплач за акции
# y = x*0.03 #процент брокеру
# x1 = 2000*42.75 #проданы акции
# y1 = x1*0.03 #процент брокеру

# print(f"уплач за акции {x} \nпроцент брокеру {y} \n\n\nпроданы акции {x1} \n процент брокеру {y1}")
#
# if (x-y) < (x1-y1):
#     print("прибыль")
# else:
#     print("убыток")

# x = int(input("как начисляется ваш если ежемесячно введите 1 если ежеквартално введите 2"))
# if x == 1:
#     n = 12
# if x == 2:
#     n = 2
#
# r1 = int(input("введите годовую ставку"))
#
# r = r1/100
# P = 1000
# t = 1
# A = P*(1+(r/n))**(n*t)
#
# print(A)

# x = int(input("enter 1-7"))
# if x == 1:
#     print("monday")
# if x == 2:
#     print("Tuesday")
# if x == 3:
#     print("Wednesday")

# x1 = int(input("enter lenght 1"))
# y1 = int(input("enter width 1"))
# x2 = int(input("enter lenght 2"))
# y2 = int(input("enter width 2"))
#
# x=x1*y1
# y=x2*y2
#
# if x>y:
#     print("первый больше")
# if x<y:
#     print(" второй болше")
# if  x == y:
#     print("равны")


# x = 99
#
# if x <= 1:
#     y="baby"
# if 1< x <=13:
#     y="children"
# if 13 < x <= 20:
#     y="podrostok"
# if x > 20:
#     y = "old"

#кр+син = фиол
#кр+желт = оран
#син+жел = зел
#
# x = str(input("1 color"))
# y = str(input("2 color"))
#
# if x  == "кр" and y == "син":
#     print("фиол")
# elif x  == "син" and y == "кр":
#     print("фиол")
#
# elif x  == "кр" and y == "жел":
#     print("оран")
# elif x  == "жел" and y == "кр":
#     print("оран")
# elif x  == "син" and y == "жел":
#     print("зел")
# elif x  == "жел" and y == "син":
#     print("зел")
# else:
#     print("ошибка")

# сосиски по 10 штук
# булки по 8 штук


# x = int(input("кол человек"))
# y = int(input("кол хотдогов на человека"))
# q = x*y
q = 81


# print(f"хотдогов {q}")
# z = q/10 #упаковок сосисок
# z1 = q // 10 #целое
# z2 = q % 10 #остаток
# if z2>0:
#     print(f"упаковок сосисок {z1+1}, осталось сосисок {10-z2}")
# if z2 == 0:
#     print(f"упаковок сосисок {z1}, осталось сосисок {z2}")
#
#
# w = q/8 #упаковок сосисок
# w1 = q // 8 #целое
# w2 = q % 8 #остаток
#
# if w2>0:
#     print(f"упаковок булок {w1+1}, осталось булок {10-w2}")
# if w2 == 0:
#     print(f"упаковок булок {w1}, осталось булок {w2}")

# 0 - зеленый
# 1-10 неч красные чет черн
# 11-18 неч черные чет красн
# 19-28 неч кр чет черн
# 29-36 неч черн чет крас

# x = 15
#
# if x == 0:
#    print("зел")
# if 1 <=x<= 10 and x%2 == 0:
#    print(f" {x} четное черное")
# if 1 <=x<= 10 and x%2 == 1:
#    print(f"{x} нечетное красное")
#
# if 11 <=x<= 18 and x%2 == 0:
#    print(f" {x} четное красные")
# if 11 <=x<= 18 and x%2 == 1:
#    print(f"{x} нечетное черное")

#x = int(input("enter sek"))
# x=99999
# if 60 <= x < 3600:
# #минуты и секунды
#     print(f" {x//60} минут {x%60} секунд")
#
# if 3600 <= x < 86400:
# #часы и минуты и секунды
#     print(f"{x//3600} часов {(x%3600)//60} минут {(x%3600)%60} секунд")
# if  x >= 86400:
# #дни и часы и минуты и секунды
#     print(f"{x//86400}дней {(x%86400)//3600} часов {((x%86400)%3600)//60} минут {((x%86400)%3600)%60} секунд")

# x = 2012
# if x%100 == 0 and x%400 == 0:
#     print (f"{x} високосный")
# elif x%100 != 0 and x%4 == 0:
#     print(f"{x} високосный")
# else:
#     print(f"{x} НЕ високосный")

# print("перезагр комп")
# x = str(input("вы исправили проблему"))
# if x == "yes":
#      print("OK")
# if x == "no":
#     print("перезагр маршрутиз")
#     x = str(input("вы исправили проблему"))
#     if x == "yes":
#         print("OK")
#     if x == "no":
#
#         print("проверьте кабели")
#         x = str(input("вы исправили проблему"))
#         if x == "yes":
#             print("OK")
#         if x == "no":
#             print("переместите маршрутизатор")
#             x = str(input("вы исправили проблему"))
#             if x == "yes":
#                 print("OK")
#             if x == "no":
#                 print("купите новый маршрутизатр")


# x = str(input("будет на ужине вегитарианец?"))
# y = str(input("будет на ужине веган?"))
# z = str(input("будет на ужине глютен?"))
#
# w = [x,y,z]
# print(w)
#
# gjo = ['no', 'no', 'no']
# centr = ['yes', 'no', 'yes']
# zaUgl = ['yes', 'yes', 'yes']
# mama = ['yes', 'no', 'no']
# kuhny = ['yes', 'yes', 'yes']
#
#
# if w == gjo: # так лучше толко прописать вручную варианты в массиве if w == [yes yes yes] print all restor...
#     print("gjo")
# if w == centr:
#     print("centr")
# if w == zaUgl:
#     print("zaUgl")
# if w == mama:
#     print("mama")
# if w == kuhny:
#     print("kuhny")


# джо - нет нет нет
# центральная - да нет да
# за углом - да да да
# мама - да нет нет
# кухня - да да да


# if x == "no" and  y == "no" and  z == "no":
#     print("all restorans")
# if x == "yes" and  y == "yes" and  z == "yes":
#     print("за углом, кухня")
# if x == "yes" and  y == "yes" and  z == "no":
#     print("     ")
# if x == "yes" and  y == "no" and  z == "yes":
#     print("     ")
# if x == "no" and  y == "yes" and  z == "yes":
#     print("     ")
# if x == "no" and  y == "no" and  z == "yes":
#     print("     ")
# if x == "yes" and  y == "no" and  z == "no":
#     print("     ")

# product = 1
# print(product)
# while product < 100:
#     i = int(input("enter number"))
#     product = i*10
#     print(product)

# y = "yes"
# while y == "yes":
#     i = int(input("enter number 1"))
#     i1 = int(input("enter number 2"))
#     print(i+i1)
#     y = str(input("one more time?"))

# for i in range(0, 1001, 10):
#     print(i)

# i = 0
# W = 0
# while i < 10:
#     w = int(input("enter number"))
#     i = i+1
#     W = W + w
# print(W)

# W=0
# for x in range(1, 31):
#     w = x/(31-x)
#     W=W+w
#     print(W)

# for i in range(1,10):
#     print(" ")
#     for i in range(1, 16):
#         print("#", end="")

# i=1
# summ = 0
# while i<6:
#     x=int(input(f" enter mistakes {i}"))
#     i += 1
#     summ += x
# print(summ)

# for i in range(10,31,5):
#     x=i*4.2
#     print(i, x)

#
# x1 = " "
# x= int(input("speed km/h"))
# y= int(input("hour"))
# print(f"hour {x1:10} distance")
# print("________________________")
# for i in range(1,y+1):
#     print(f"{i:3} {i*x:15}")

# x = int(input("enter year"))
# summMonth = 0
# summRein = 0
# for i in range(1, x+1):
#     summMonth1 = 0
#     summRein1 = 0
#     for e in range(1, 13):
#         q = int(input("enter quality"))
#         summMonth += 1
#         summRein += q
#         summMonth1 += 1
#         summRein1 += q
#     print(f"average rein in month {summRein1/summMonth1} ")
# print(f"year {i} month {summMonth} rein {summRein}")


# for x in range(0,20):
#     y = (9 / 5) * x + 32
#     print(f"celc {x} nfarengete {y}")

# x = int(input("enter quality days"))
# summ = 1
# summ1 =  summ
# for i in range(1, x+1):
#     summ = summ*2
#     summ1 += summ
# if summ1 < 100:
#     print(summ1, "cent")
# if summ1 >= 100:
#     print(f"{summ1//100} doll {summ1%100} cent")

# a = 1
# summ = 0
# while a>=0:
#     a = int(input("enter number"))
#     summ += a
# print(summ-a)

# summ = 0
# for i in range(1, 26):
#     summ += 1.6
#     print(f"year {i} level {summ:.2f}")

# pay = 100
# summ = 100
# for i in range(2,6):
#     pay = pay*1.03
#     summ += pay
# print(f"{summ:.2f}")

# weight = 100
# for i in range(1,7):
#     weight -= 1.5
#     print(f"в {i} месяц -  вес {weight}")

# number = 7
# total = 1
# for i in range(0, number):
#     total *= (i+1)
#     print(total)

# start = 2
# plus = 1.3
# days = 10
# print(f"{1:10}   {start}")
# for i in range(1,days):
#     print(f"{(i+1):10}   {start*plus:.2f}")
#     start *= plus


# for i in range(8,0,-1):
#     print(i*"#")


# print("#""#")
# for i in range(0, 8):
#     print("#", i*" ", "#")

# def times_ten(time):
#     return time*10
# print(times_ten(5))

# def show_value(quantity):
#     return print(quantity)
# show_value(1)

# def my_function(a,b,c):
#     d = (a+c)/b
#     return d
#
# print (my_function(5, c=1, b=3))

import random

# rand = random.randint(1,100)
# rand1 = random.random()
# print(rand)

#
# def half(number):
#     return print(float(number/2))
# def main():
#     result = half(7)
# main()


# def main():
#     convert_km(10)
# def convert_km(km):
#     return print(f"mile = {km*0.6214:.2f}")
#
# main()

# def main():
#     x = int(input("enter summ"))
#     print(reg_nal(x))
#     print(fed_nal(x))
#     print(f"nalog+ = {reg_nal(x)+fed_nal(x)}")

# def reg_nal(x):
#     return x*0.025
#
# def fed_nal(x):
#     return x * 0.05
#
#
# main()

# def main():
#     x = int(input("enter real price"))
#     print(ocen_price(x))
#     nal_imuch(x)
#
# def ocen_price(x):
#     return x*0.6
# def nal_imuch(x):
#     return print(f"{ocen_price(x)/100*0.72:.2f}")
# main()

# def main():
#     x = int(input("enter wall"))
#     y = int(input("enter price 5L color"))
#     print(quantyty_color(x))
#     print(quantyty_hour(x))
#     print(price_color(x,y))
#     print(price_work(x))
#     print(price_all(x,y))

# def quantyty_color(x):
#         return (5 * x)/10
# def quantyty_hour(x):
#     return (8 * x) / 10
# def price_color(x,y):
#     return y*quantyty_color(x)
# def price_work(x):
#     return 2000*quantyty_hour(x)
#
# def price_all(x,y):
#     return price_color(x, y) + price_work(x)
#
# main()

# def main():
#     q1 = random.randint(1, 1000)
#     q2 = random.randint(1, 1000)
#     print(f"{q1} \n {q2}")
#     x= int(input("summ = ?"))
#     if x == q1+q2:
#         print("right")
#     if x != q1+q2:
#         print(f"Not right {q1+q2}")
# main()

# def main():
#     x = int(input("number 1"))
#     y = int(input("number 2"))
#     bigest_number(x,y)
#
# def bigest_number(x,y):
#     if x > y:
#         return print(x)
#     if x < y:
#         return print(y)
#     if x == y:
#         return print("=")
#
# main()

# def main():
#     x = int(input("number 1"))
#     x1 = int(input("number 2"))
#     x2 = int(input("number 3"))
#     x3 = int(input("number 4"))
#     x4 = int(input("number 5"))
#
#     calc_average(x,x1,x2,x3,x4)
#     determine_grade(x)
#     determine_grade(x1)
#     determine_grade(x2)
#     determine_grade(x3)
#     determine_grade(x4)
#
# def calc_average(x,x1,x2,x3,x4):
#     return print((x+x1+x2+x3+x4)/5)
# def determine_grade(q):
#     if q >= 90:
#         return print(q,  "A")
#     elif q >= 80:
#         return print(q,  "B")
#     elif q >= 70:
#         return print(q, "C")
#     elif q >= 60:
#         return print(q, "D")
#     elif q < 60:
#         return print(q,  "F")
#
# main()

# def main():
#     i = 0
#     k = 0
#     for w in range(1, 101):
#         x = random.randint(1,10000)
#
#         if chet(x):
#             i+=1
#         else:
#             k+=1
#     print(f"chet {i} nechet{k}")
#
# def chet(x):
#     if x%2 == 0:
#         return True
#
# main()

# def main():
#     x = int(input("enter number"))
#     if is_prime(x) == False:
#         print(f"number {x} notprime")
#     else:
#         print(f"number {x} prime")
# def is_prime(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#
# main()

#if x % x == 0 and x % 1 == 0 and :

# def main():
#     for b in range(1, 101):
#
#         if is_prime(b) is not False:
#             print(f"number {b} prime")
#
# def is_prime(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
# main()

# def main():
#     P,i,t = 100, 0.01, 12
#     future_summ(P,i,t)
# def future_summ(P,i,t):
#     return print( f"{P*(1+i)**t:.2f}")
# main()


# def main():
#     i = "yes"
#     while i == "yes":
#         x = int(input("guess the number"))
#         y = random.randint(1, 100)
#         if x == y:
#             print(f"yes, number is {y}")
#         else:
#             print(f"no {y}")
#             i = str(input("play one more time? yes/no"))
# main()

# def main():
#     x1 = random.randint(1,3)
#     if x1 == 1:
#             x = "камень"
#     if x1 == 2:
#             x = "ножницы"
#     if x1 == 3:
#             x = "бумага"
#     i = 1
#     while i == 1:
#         y = str(input("камень ножницы или бумага?"))
#         if y == x:
#             print(f"компьютер тоже выбрал {x}, сыграйте еще")
#         if (x == "камень" and y == "ножницы") or (y == "камень" and x == "ножницы"):
#             print(x)
#             print(f"выиграл камень")
#             i = 2
#         if (x == "камень" and y == "бумага") or (y == "камень" and x == "бумага"):
#             print(x)
#             print(f"выиграла бумага")
#             i = 2
#         if (x == "ножницы" and y == "бумага") or (y == "ножницы" and x == "бумага"):
#             print(x)
#             print(f"выиграли ножницы")
#             i = 2
# main()

# x = open("my_name.txt", "w")
# x.write("Marina")
# x.close()

# x = open("my_name.txt", "r")
# print(x.readline())
# x.close

# x = open("number_list.txt", "w")
# for i in range(1,101):
#     x.write(str(f"{i}\n"))
# x.close
#
# x = open("number_list.txt", "r")
# for i in x:
#     #i = i.rstrip('\n')
#     #i = int(i)
#     print(i)

# x = open("number_list.txt", "r")
# summ=0
# for i in x:
#     i=int(i)
#     summ+=i
# print (summ)

# x = open("students.txt", "r")
# x1 = open("students1.txt", "w")
# for i in x:
#     if not i == "dima 3\n":
#         x1.write(i)
# x.close
# x1.close
# os.rename("students1.txt", "students.txt")
# os.remove("students1.txt")

# x = open("number_list — копия.txt", "r")
# s = 0
# try:
#     while s < 5:
#
#         print(int(x.readline()))
#         s+=1
# except ValueError:
#     print("< 5 line")
#
# x = open("my_name.txt", "r")
# q=1
# for i in x:
#     i=i.rstrip("\n")
#     print(f"{q}:{i}")
#     q+=1
# print(q-1)
# x.close

# x = open("number_list.txt", "r")
# summ = 0
# quan = 0
# for i in x:
#     i = int(i)
#     summ += i
#     quan += 1
# print(summ/quan)

# x = open("number_rand.txt", "w")
# y=6
# for i in range(1,y+1):
#     x.write(str(random.randint(1,500)))
#     x.write("\n")

# x = open("golf.txt", "w")
#
# #qul =  enter quantity line
# qul = 2
# for i in range(1,qul+1):
#     x.write(str(input("enter name"))+"\n")
#     x.write(str(input("enter lastname"))+"\n\n")

# q=str(input("Enter name"))
# w=str(input("Enter name1"))
#
# x=open("1.html","w")
# x.write(f"<html>\n<head>\n</head>\n<body>\n <center>\n  <h1>{q}</h1>\n </center>\n <hr />\n {w}\n <hr />\n</body>\n</html>")

# import array
# x=array.array("i",[23,33,3,4,5,6,7,8,9])
# print(x)
# print(type(x))
# print(min(x))

# x = ["1234","123","123456789"]
# print([len(i) for i in x if len(i)<9])

# x = [0,0,0,0,0,0,0]
# for i in range(0,7):
#     x[i] = int(input('enter summ'))
# print(x)

# x = []
# for i in range(0,7):
#     x.append(int(input('enter summ')))
# print(x)

# x = ["1234","123","123456789"]
# for i in x:
#     print(i)
#
# print([i for i in x if i=="123"])
#
# y = [i for i in x]
# print(f"y = {y}")
#
# x = ["1","5","2"]
# summ=0
# for i in x:
#     summ+=int(i)
# print(f"summ = {summ}")

# x = ["marina","dima","artem"]
# x1="dima1"
# try:
#     if x.index(x1):
#         print(f"hi, {x1}")
# except:
#     print("no dima1")

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [i**2 for i in list1]
# print (list2)

# list1 = [1,2,359,4,5,6,7,158,9]
# list2 = [i for i in list1 if i>100]
# print (list2)

# list1 = [1,2,359,4,5,6,7,158,9]
# list2 = [i for i in list1 if i%2==0]
# print(list2)

# x = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
# for i in range(0,5):
#     for q in range(0,3):
#         x[i][q] = random.randint(1,100)
#         # x[i][q] = int(input("enter number"))
# print(x)

# x = []
# for i in range(0,5):
#     x.append([0]*3)
# print(x)
#
# for i in range(0, 5):
#     for q in range(0,3):
#         x[i][q] = int(input("enter number"))
# print(x)
#
# for i in range(0, 5):
#     for q in range(0,3):
#         print(x[i][q], end=" ")


# x=[]
# summ = 0
# for i in range(1,7):
#     y = int(input(f"enter sum for day {i}"))
#     x.append(y)
#     summ+=y
#
# print(x)
# print(f"summ = {summ}")

# x=[]
# for i in range(0,7):
#     x.append(random.randint(1,9))
# print(x)

# x=[]
# summ = 0
# for i in range(1,13):
#     y = int(input(f"enter rain for month {i}"))
#     x.append(y)
#     summ += y
# print(x)
# print(f"summ = {summ} average = {summ/12} min ={x.index(min(x))+1} max={x.index(max(x))+1}")


# y=open("charge_accounts.txt", "r")
# x=[]
# r = int(7895122)
# print(r)
# for i in y:
#     x.append(int(i))
#
# if r in x:
#     print("yes")
# else:
#     print("no")
# print(x)

# def main():
#     x=[1,2,3,4,5,6,7]
#     n=4
#     print(more_n([1,2,3,4,5,6,7,8,9,11],n))
# def more_n(x,n):
#     y=[]
#     for i in x:
#         if i>n:
#             y.append(i)
#     return y
#
# main()

# x1=open("student_solution.txt", "r")
# x=[i.rstrip("\n") for i in x1]
# y1=open("student_solution1.txt", "r")
# y=[i.rstrip("\n") for i in y1]
# print(x)
# print(y)
# right = 0
# for i in range(0,len(x)):
#     if x[i] == y[i]:
#         right += 1
#     if x[i] != y[i]:
#         print(f"ansver {i+1} not {y[i]}")
# if right>=15:
#     print(f"passed the exam, {right} right answer ")
# else:
#     print(f"the exam faled {right} right answer")

# x1=open("GirlNames.txt", "r")
# x=[i.rstrip("\n") for i in x1]
# y1=open("BoyNames.txt", "r")
# y=[i.rstrip("\n") for i in y1]
# print(x)
# print(y)
#
# g = "Madison1"
# b = "Joshua"
#
# if g in x:
#     print(f"name {g} famous, top 200")
# else:
#     print(f"name {g} not famous")
# for i in range(0,len(y)):
#     if b == y[i]:
#         print(f"name {b} famous, top 200")



# y=[i for i in range(1950,1991)]
# print(y)
#
# x1=open("USPopulation.txt", "r")
# x=[int(i.rstrip("\n")) for i in x1]
#
# z= []
# summ=0
# for i in range(0,len(x)-1):
#     r=x[i+1]-x[i]
#     z.append(r)
#     summ+=r
# print(z)
#
# print(x)
#
# print(f"min {y[z.index(min(z))]+1} - {min(z):,.2f}")
# print(f"max {y[z.index(max(z))]+1} - {max(z):,.2f}")
# print(f"average {summ/len(z):,.2f}")

# x1 = open("WorldSeriesWinners.txt", "r")
# x = [i.rstrip("\n") for i in x1]
# summ=0
# y = "Chicago White Sox"
# print(x)
# for i in x:
#     if i == y:
#         summ += 1
#
# print(f"{y} win {summ}")


# def main():
#     x = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
#
#     if sqear(x):
#         print("yes")
# def sqear(x):
#
#
#     z = x[0][0]+x[0][1]+x[0][2]
#     z1 = x[1][0]+x[1][1]+x[1][2]
#     z2 = x[2][0]+x[2][1]+x[2][2]
#
#     q = x[0][0]+x[1][0]+x[2][0]
#     q1 = x[0][1]+x[1][1]+x[2][1]
#     q2 = x[0][2]+x[1][2]+x[2][2]
#
#     d1 = x[0][0]+x[1][1]+x[2][2]
#     d2 = x[2][0]+x[1][1]+x[0][2]
#     if z==z1==z2==q==q1==q2==d1==d2:
#         return True
#
# main()


# def main():
#
#     t = 100
#     x = [i for i in range(2, t)]
#     y = []
#     for i in x:
#         if not is_not_prime(i) == False:
#            y.append(i)
#     print(y)
#
# def is_not_prime(x):
#     q = [i for i in range(2, x)]
#     for i in q:
#         if  x % i == 0:
#             return False
# main()

# def main():
#     x = open("8_ball_responses_ru.txt","r")
#     x = [i.rstrip("\n") for i in x]
#     print(x)
#     t = "yes"
#     while t == "yes":
#         q = str(input("enter question"))
#         print(x[random.randint(1,len(x))])
#         t = str(input("one more game? yes/no"))
#
# main()

# x = "d"
# if x.upper() == "D":
#     print(x)

# x = "d t ert e"
# summ=0
# for i in x:
#     if i == " ":
#         summ+=1
# print (summ)
#
# summ1=0
# for i in x:
#     if i.isspace():
#         summ1 += 1
# print (summ1)

# x = "d t ert e 123 456"
# summ = 0
# for i in x:
#     if i.isdigit():
#         summ+=1
# print(summ)
#
# x = "D t erT e 123 456"
# summ = 0
# for i in x:
#     if i.islower():
#         summ+=1
# print(summ)
#
#
# x = "D t erT e 123 456"
# summ = 0
# for i in x:
#     if i.isupper():
#         summ+=1
# print(summ)

# x = "D t erT e 123 456.com1"
# summ = 0
# if x.endswith(".com"):
#     print(f"com there is")

# x = "D t erT e 123 456.com1"
# x= x.replace("t","T")
# print(x)

# x = "D t erT e 123 456.com1"
# y = ""
# for i in range(len(x)-1, -1,-1):
#     y += x[i]
# print(y)
#
# x = "D t erT e 123 456.com1"
# y = ""
# for i in reversed(range(0, len(x))):
#     y += x[i]
# print(y)

# x = "D t erT e 123 456.com1"
# print(x[:3])
# print(x[-3:])
# print(x.split(" "))
#
# x = "Behtereva Marina Anatolevna"
# for i in x.split(" "):
#     print(f"{i[0]}.", end="")
#
# x = "11112"
# summ=0
# for i in x:
#     summ+=int(i)
# print(summ)

# y='январь', ' февраль', ' март', ' апрель', ' май', ' июнь', ' июль', ' август', ' сентябрь', ' октябрь', ' ноябрь', ' декабрь'
# x = "16/11/1985"
# x=x.split("/")
# print(x[0],y[int(x[1])-1] ,x[2])

# x = "A.-B-...C-.-.D-..E.F..-.G--.H....I..J.---K-.-L.-..M--N-.O---P.--.Q--.-R.-.S...T-U..-V...-W.--X-..-Y-.--Z--.."
# for i in x:
#     if i.isupper():
#         x = x.replace(f"{i}",":")
# x= x[1:]
# x= x.split(":")
# print(x)
#
#
# y="A.-B-...C-.-.D-..E.F..-.G--.H....I..J.---K-.-L.-..M--N-.O---P.--.Q--.-R.-.S...T-U..-V...-W.--X-..-Y-.--Z--.."
# y1=""
# for i in y:
#     if i.isupper():
#         y1+=str(i)
# print(y1)
# # print(len(x), len(y1))
#
# q = "MAZ"
# for w in q:
#     print(x[y1.find(w)])

# x1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# y = "555-GET-FOOD"
#
# for i in y:
#     if x1.find(i) >= 0:
#         if 0 <= x1.find(i) <= 2:
#             y = y.replace(i, "2")
#         if 2 < x1.find(i) <= 5:
#             y = y.replace(i, "3")
#         if 5 < x1.find(i) <= 8:
#             y = y.replace(i, "4")
#         if 8 < x1.find(i) <= 11:
#             y = y.replace(i, "5")
#         if 11 < x1.find(i) <= 14:
#             y = y.replace(i, "6")
#         if 14 < x1.find(i) <= 17:
#             y = y.replace(i, "7")
#         if 17 < x1.find(i) <= 21:
#             y = y.replace(i, "8")
#         if 21 < x1.find(i) <= 24:
#             y = y.replace(i, "9")
# print(y)



# x1 = open("text.txt","r")
# x= x1.readlines()
#
# world = 0
# predl = 0
# for i in x:
#     i = i.rstrip()
#     i=i.split()
#     print(i)
#     print(len(i))
#     world+=len(i)
#     predl+=1
# print(world/(predl))

# x = open("text.txt", "r")
# x = x.readlines()
# print(x)
# upper = 0
# lower = 0
# digit = 0
# space = 0
# for i in x:
#     for y in i:
#         if y.isupper():
#             upper+=1
#         if y.islower():
#             lower+=1
#         if y.isdigit():
#             digit+=1
#         if y.isspace():
#             space+=1
# print(f"{upper} {lower} {digit} {space} ")

# def main():
#     x = "hi you! my name is gjo. and how are you name?"
#     x = x.split()
#     y = ""
#     q = True
#
#     for i in x:
#         if q:
#             y += zamena(i) + " "
#         else:
#             y += i + " "
#         if i[-1] == "." or i[-1] == "!" or i[-1] == "?":
#             q = True
#         else:
#             q = False
#     print(y)
# def zamena(i):
#     i = i.replace(i[0], i[0].upper())
#     return i
# main()


# x = "Hi you?"
# x = x.upper()
# x1 = "A,E,I,O,U,Y"
# x2 = "B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Z"
# x1 = x1.split(",")
# x2 = x2.split(",")
#
# print(x)
# print(x1)
# print(x2)
# gl = 0
# sogl = 0
# for i in x:
#
#     if i in x1:
#         sogl += 1
#
#     if i in x2:
#         gl += 1
#         print(i)
# print(sogl, gl)

# x = "hhhhi rrrrryouuuuuuuuuuuurrrrurr"
# y=[]
# for i in x:
#     summ = 0
#     for q in x:
#         if i ==q:
#             summ+=1
#     y.append(summ)
# print(x[y.index(max(y))])

# x = "HowAreYouName"
# y=''
# for i in x:
#
#     if i.isupper():
#         y += " " + i
#     else:
#         y += i
# y = y.lstrip(" ")
# print(y)

# x = "How Are You Name"
# x = x.split()
# y=''
# for i in x:
#     y += i[1:] + i[0]+"ki"+" "
# print(y)

# def main():
#     w = open("pbnumbers.txt", "r")
#     x= ''
#     for i in w:
#         x+=i
#     x = x.split()
#     print(x)
#
#     # x1 = x
#     # print("10 наиболее распр. чисел")
#     # for i in range(0,10):
#     #     print(max_quantity(x1), end=" ")
#     #     x1 = delite(x1, max_quantity(x1))
#     #
#     # x2 = x
#     # print("")
#     # print("10 наименее распр. чисел")
#     # for i in range(0,10):
#     #     print(min_quantity(x2), end=" ")
#     #     x2 = delite(x2, min_quantity(x2))
#
#     x3 = x
#     print("")
#     print("10 выдержанных чисел")
#     for i in range(0, 10):
#         print(vyderjanoe(x3), end=" ")
#         x3 = delite(x3, vyderjanoe(x3))
#
#
#
# def vyderjanoe(x):
#     x = x[::-1]
#     y=[]
#     for i in x:
#         y.append(x.index(i))
#     return x[y.index(max(y))]
# def delite(x, t):
#     y = [i for i in x if i != t]
#     return y
#
# def max_quantity(x):
#     y=[]
#     for i in x:
#         summ = 0
#         for q in x:
#             if i ==q:
#                 summ+=1
#         y.append(summ)
#     return (x[y.index(max(y))])
#
# def min_quantity(x):
#     y=[]
#     for i in x:
#         summ = 0
#         for q in x:
#             if i ==q:
#                 summ+=1
#         y.append(summ)
#     return (x[y.index(min(y))])
# main()


# def main():
#     w = open("pbnumbers.txt", "r")
#     x= ''
#     for i in w:
#         x+=i[:-3]
#
#     x = x.split()
#     print(x)
#
#
#     x, y = chastota(x)
#     for i in range(0, 69):
#         print(f"number {x[0]} vstrechaetcj {y[0]}")
#         x = delite(x, x[0])
#         x, y = chastota(x)
#
# def chastota(x):
#     x.sort()
#
#     y = []
#     for i in x:
#         summ = 0
#         for q in x:
#             if i ==q:
#                 summ+=1
#         y.append(summ)
#
#     return x,y
#
#
# def delite(x, t):
#     y = [i for i in x if i != t]
#     return y
#
# main()

# def main():
#     w = open("pbnumbers.txt", "r")
#     x= ''
#     for i in w:
#         x+=i[-3:]
#
#     x = x.split()
#     print(x)
#
#
#     x, y = chastota(x)
#     for i in range(0, 26):
#         print(f"number {x[0]} vstrechaetcj {y[0]}")
#         x = delite(x, x[0])
#         x, y = chastota(x)
#
# def chastota(x):
#     x.sort()
#
#     y = []
#     for i in x:
#         summ = 0
#         for q in x:
#             if i ==q:
#                 summ+=1
#         y.append(summ)
#
#     return x,y
#
#
# def delite(x, t):
#     y = [i for i in x if i != t]
#     return y
#
# main()


# def main():
#     w = open("GasPrices.txt", "r")
#     x = ''
#     for i in w:
#         x += i
#     x = x.split("\n")
#     print(x)
#
#     # for i in range(1993, 2014):
#     #     y = list_year(x, str(i))
#     #     summ = 0
#     #     quant = 0
#     #     for q in y:
#     #         summ += float(q[11:])
#     #         quant +=1
#         # print(f"average = {summ/quant:.2f} for {i}")
#
#     for i in range(1, 10):
#         y = list_month_1_9(x, str(i))
#         summ = 0
#         quant = 0
#         # print(y)
#         for q in y:
#             summ += float(q[11:])
#             quant += 1
#         print(f"average = {summ/quant:.2f} for {i}")
#     for i in range(10, 13):
#         y = list_month_10_12(x, str(i))
#         summ = 0
#         quant = 0
#         # print(y)
#         for q in y:
#             summ += float(q[11:])
#             quant += 1
#         print(f"average = {summ / quant:.2f} for {i}")
#
# def list_year(x, y):
#     y1 = [i for i in x if i[6:10] == y]
#     return y1
#
# def list_month_1_9(x, y):
#     y1 = [i for i in x if (i[1:2] == y and i[0] != "1")]
#     return y1
#
# def list_month_10_12(x, y):
#     y1 = [i for i in x if i[:2] == y]
#     return y1
# main()


# def main():
#     w = open("GasPrices.txt", "r")
#     x = ''
#     for i in w:
#         x += i
#     x = x.split("\n")
#     print(x)
#
#     for i in range(1993, 2014):
#         y = list_year(x, str(i))
#         # print(y)
#
#         for l in range(1, 10):
#             r = list_month_1_9(y, str(l))
#             summ = 0
#             quant = 0
#             for q11 in r:
#                 summ += float(q11[11:])
#                 quant += 1
#             try:
#                 print(f"average = {summ/quant:.2f} for {q11[:2]} for {i}")
#             except:
#                 f="g4"
#
#         for l in range(10, 13):
#             r = list_month_10_12(y, str(l))
#             summ = 0
#             quant = 0
#             for q11 in r:
#                 summ += float(q11[11:])
#                 quant += 1
#             try:
#                 print(f"average = {summ/quant:.2f} for {q11[:2]} for {i}")
#             except:
#                 f="g4"
#
#
# def list_year(x, y):
#     y1 = [i for i in x if i[6:10] == y]
#     return y1
#
# def list_month_1_9(x, y):
#     y1 = [i for i in x if (i[1:2] == y and i[0] != "1")]
#     return y1
#
# def list_month_10_12(x, y):
#     y1 = [i for i in x if i[:2] == y]
#     return y1
# main()

# def main():
#     w = open("GasPrices.txt", "r")
#     x = ''
#     for i in w:
#         x += i
#     x = x.split("\n")
#     print(x)
#
#     for i in range(1993, 2014):
#         y = list_year(x, str(i))
#         # print(y)
#
#         for l in range(1, 10):
#             r = list_month_1_9(y, str(l))
#             summ = 0
#             quant = 0
#             for q11 in r:
#                 summ += float(q11[11:])
#                 quant += 1
#             try:
#                 print(f"average = {summ/quant:.2f} for {q11[:2]} for {i}")
#             except:
#                 f="g4"
#
#         for l in range(10, 13):
#             r = list_month_10_12(y, str(l))
#             summ = 0
#             quant = 0
#             for q11 in r:
#                 summ += float(q11[11:])
#                 quant += 1
#             try:
#                 print(f"average = {summ/quant:.2f} for {q11[:2]} for {i}")
#             except:
#                 f="g4"
#
#
# def list_year(x, y):
#     y1 = [i for i in x if i[6:10] == y]
#     return y1
#
# def list_month_1_9(x, y):
#     y1 = [i for i in x if (i[1:2] == y and i[0] != "1")]
#     return y1
#
# def list_month_10_12(x, y):
#     y1 = [i for i in x if i[:2] == y]
#     return y1
# main()

# def main():
#     w = open("GasPrices.txt", "r")
#     x = ''
#     for i in w:
#         x += i
#     x = x.split("\n")
#     print(x)
#
#     for i in range(1993, 2014):
#         y = list_year(x, str(i))
#
#         y1 = [l[11:] for l in y]
#         print(f"min {min(y1)} in {i}", end="/")
#         print(f"max {max(y1)} in {i}")
#
#
# def list_year(x, y):
#     y1 = [i for i in x if i[6:10] == y]
#     return y1
#
# main()

# def main():
#     w = open("GasPrices.txt", "r")
#     x = ''
#     for i in w:
#         x += i
#     x = x.split("\n")
#     print(x)
#
#     z = [i[11:] for i in x]
#     print(z)
#
#     print(min_price_and_del(x,z))
#
#
# def min_price_and_del(x,x1):
#     ansver = ""
#     for i in range(0, len(x)):
#         q = x1.index(min(x1))
#         ansver += x[q] + "\n"
#         x1.pop(q)
#         x.pop(q)
#
#     return ansver
#
# main()

# def main():
#     w = open("GasPrices.txt", "r")
#     x = ''
#     for i in w:
#         x += i
#     x = x.split("\n")
#     print(x)
#
#     z = [i[11:] for i in x]
#     print(z)
#
#     print(max_price_and_del(x,z))
#
#
# def max_price_and_del(x,x1):
#     ansver = ""
#     for i in range(0, len(x)):
#         q = x1.index(max(x1))
#         ansver += x[q] + "\n"
#         x1.pop(q)
#         x.pop(q)
#
#     return ansver
#
# main()

# x = {"a": 1, "b": 2, "c": 3}
# print(x)
#
# print(x.get("a", "no 'a' "))
# print(x.get("a1", "no 'a1' "))
#
# print(x.pop("a", "no 'a' "))
# print(x)

# x = {"a": 1, "b": 2, "c": 3}
#
# if "a1" in x:
#     print(x["a"])
# else:
#     print("no 'a' ")


# x = {"a": 1, "b": 2, "c": 3}
# if "a" in x:
#     print(x["a"])
#     del x["a"]
# else:
#     print("no 'a' ")
#
# print(x)

# x=set(i for i in range(10,41,10))
# print(x)

# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
#
# set3 = set1 | set2
# set4 = set1 & set2
# set5 = set1 - set2
# set6 = set1 <= set2
# set7 = set1 >= set2
#
# print(f"{set3}, set1 | set2")
# print(f"{set4}, set1 & set2")
# print(f"{set5}, set1 - set2")
# print(f"{set6}, set1 <= set2")
# print(f"{set7}, set1 >= set2")

# numbers = [1, 2, 3, 4, 5]
# x = {i:i*10 for i in numbers}
# print(type(x), x)

# import pickle
#
# x1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# print(x1[1])
# x2 = {i:x1.get(i) for i in x1 if x1.get(i)<40}
# print(type(x2), x2)
#
# x = open("pickle1.dat", "wb")
# pickle.dump(x2, x)
#
#
# import pickle
# x = open(r'C:\Users\Admin\AppData\Roaming\JetBrains\PyCharm2023.2\light-edit\pickle1.dat' ,"rb")
#
# x1 = pickle.load(x)
# print(x1)

# rooms = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755,
#              'NT110': 1244, 'CM241': 1411}
#
# instructors = {'CS101': 'Хайнс', 'CS102': 'Альварадо',
#                    'CS103': 'Рич', 'NT110': 'Берк',
#                    'CM241': 'Ли'}
#
# times = {'CS101': '8:00', 'CS102': '9:00',
#              'CS103': '10:00', 'NT110': '11:00',
#              'CM241': '12:00'}
#
# x = 'CS101'
# print(rooms[x], instructors[x], times[x])
#
# x = {'Алабама':'Монтгомери', 'Аляска':'Джуно',
#                 'Аризона':'Феникс', 'Арканзас':'Литтл Рок',
#                 'Калифорния':'Сакраменто', 'Колорадо':'Денвер',
#                 'Коннектикут':'Хартфорд', 'Делавэр':'Довер',
#                 'Флорида':'Таллахасси', 'Джорджия':'Атланта',
#                 'Гавайи':'Гонолулу', 'Айдахо':'Бойсе',
#                 'Иллинойс':'Спрингфилд', 'Индиана':'Индианаполис',
#                 'Айова':'Де-Мойн', 'Канзас':'Топика',
#                 'Кентукки':'Франкфорт', 'Луизиана':'Батон-Руж',
#                 'Мэн':'Батон-Руж', 'Мэриленд':'Аннаполис',
#                 'Аннаполис':'Бостон', 'Мичиган':'Лансинг',
#                 'Миннесота':'Сен-Пол', 'Миссисипи':'Джэксон',
#                 'Миссури':'Джефферсон-Сити', 'Монтана':'Хелена',
#                 'Небраска':'Линкольн', 'Невада':'Карсон-Сити',
#                 'Нью-Гэмпшир':'Конкорд', 'Нью-Джерси':'Трентон',
#                 'Нью-Мексико':'Санта-Фе', 'Нью-Йорк':'Олбани',
#                 'Серерная Каролина':'Роли', 'Северная Дакота':'Бисмарк',
#                 'Огайо':'Колумбус', 'Оклахома':'Оклахома-сити',
#                 'Орегон':'Сейлем', 'Пенсильвания':'Гаррисберг',
#                 'Род-Айленд':'Провиденс', 'Южная Каролина':'Колумбия',
#                 'Южная Дакота':'Пирр', 'Теннеси':'Нэшвилл',
#                 'Техас':'Остин', 'Юта':'Солт-Лейк-Сити',
#                 'Вермонт':'Монтпилиер', 'Виргиния':'Ричмонд',
#                 'Вашингтон':'Олимпия', 'Западная Виргиния':'Чарлстон',
#                 'Висконсин':'Мэдисон', 'Вайоминг':'Шайен'}

# x2 = list(x.keys())
#
# x1 = int(input("enter quant questions"))
# q = 0
# right = 0
# not_right = 0
# while q < x1:
#     w = x2[random.randint(0,len(x))]
#     x3 = str(input(f"capital of {w}"))
#     q += 1
#
#     if x[w].lower() == x3.lower():
#         right += 1
#     else:
#         not_right += 1
# print(f"right ansver = {right}, not_right = {not_right}")


CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}', '\n':'\n', " ":" "}

# x = open("my_name.txt", "r")
# x1 = open("my_name1.txt", "w")
# x2 = [i for i in x]
# for q in x2:
#     for e in q:
#         x1.write(CODE[e])
# x.close()
# x1.close()

# x = open("my_name1.txt", "r")
# x1 = [i for i in x]
# print(x1)

# for i in x1:
#         for q in i:
#                 for r in CODE:
#                         if q == CODE[r]:
#                                 print(r, end="")

# for i in x1:
#         for q in i:
#                 if q in CODE:
#                         print(CODE[q], end="")



# x = open("my_name.txt", "r")
# x = x.read()
# x = x.split()
# x = [i.rstrip(":").rstrip("?").lower() for i in x]
# x = set(x)
# print(x)


# x = open("my_name.txt", "r")
# y = x.read()
# q = y.split()
# q = [i.rstrip(":").rstrip("?").lower() for i in q]
# sets = set(q)
#
# print(sets)
# print(q)
#
# itog = {i:0 for i in sets}
#
# for i in q:
#         itog[i] += 1
#
# print(itog)


# x = open("my_name.txt", "r")
# x1 = open("my_name1.txt", "r")
#
# x=x.read()
# x= x.split()
# x= [i.rstrip(":").rstrip("?").lower() for i in x]
# x= set(x)
#
# x1=x1.read()
# x1= x1.split()
# x1= [i.rstrip(":").rstrip("?").lower() for i in x1]
# x1= set(x1)
#
# x3 = x|x1
# print(f"Эти уникальные слова  в обоих файлах: \n {x3}")
#
# x3 = x&x1
# print(f"Эти слова встречаются в обоих файлах:\n {x3}")
#
# x3 = x-x1
# print(f"Эти слова встречаются в первом файле и "
#       f"не встречаются во втором файле:\n {x3}")
#
# x3 = x1-x
# print(f"Эти слова встречаются во втором файле и  "
#       f"не встречаются во первом файле: \n{x3}")
#
# x3 = x.symmetric_difference(x1)
# print(f"Эти слова встречаются в первом файле или "
#       f"втором файле и не встречаются в обоих файлах: \n{x3}")

# x = open("WorldSeriesWinners.txt", "r")
# y = [i for i in range(1903, 2010)]
# x=x.read().split("\n")
# x1=set(x)
# y.remove(1904)
# y.remove(1994)
# print(y)
# print(x)
# q={}
# for i in range(0, len(x)):
#         q[y[i]] = x[i]
# print(q)
# w= {i:0 for i in x1}
# for i in x:
#         w[i]+=1
# print(w)
#
# year = 1985
#
# print(f"name command {q[year]} quantity {w[q[year]]}")

# import pickle
#
# file = open("12345.dat", "rb")
# x = pickle.load(file)
# file.close()
#
# ch = 0
# while ch < 5:
#         print("menu\n_______________________\n add name and email - 1\n"
#               " find email - 2\n chenge email - 3\n "
#               "delite name and email -4\n exit - 5" )
#         ch = int(input("enter item menu"))
#
#         if ch == 1:
#                 name = str(input("Enter name"))
#                 email = str(input("Enter email"))
#                 x[name]=email
#         if ch == 3:
#                 n = str(input("Enter name for change e-mail"))
#                 e = str(input("Enter new e-mail"))
#                 x[n] = e
#         if ch == 2:
#                 ne = str(input("Enter name for search"))
#                 print(x[ne])
#
#         if ch == 4:
#                 na = str(input("Enter name for delite"))
#                 del x[na]
#         print(x)
#
# file = open("12345.dat", "wb")
# pickle.dump(x, file)
# file.close()

# x={}
# x1 = ['jack', 'queen', 'king']
# x2 = ['hearts', 'diamonds', 'clubs', 'spades']
# for i in range(2,11):
#         x[f"{i} hearts"] = i
# for i in range(2,11):
#         x[f"{i} diamonds"] = i
# for i in range(2,11):
#         x[f"{i} clubs"] = i
# for i in range(2,11):
#         x[f"{i} spades "] = i
# for i in x1:
#         for q in x2:
#                 x[f"{i} {q}"] = 10
# for i in x2:
#         x[f"ace {i}"] = 11
# print(x)
#
# x1 = list(x.keys())
# print(x1, type(x1))
#
#
# summ1 = 0
# summ2 = 0
#
# while summ1 < 21 and  summ2 < 21:
#         g = random.randint(0, len(x)-1)
#         card1 = x1[g]
#         print(f"1 gambler take {card1}")
#         summ1 += x[card1]
#         if card1 == 'ace hearts' or card1 == 'ace diamonds' or card1 == 'ace clubs' or card1 == 'ace spades':
#                 if summ1 > 21:
#                         summ1 -= 10
#         print(f" summ card of 1 gambler {summ1}")
#         del x[card1]
#         del x1[g]

#
#         g1 = random.randint(0, len(x) - 1)
#         card2 = x1[g1]
#         print(f"2 gambler take {card2}")
#         summ2 += x[card2]
#         if card2 == 'ace hearts' or card2 == 'ace diamonds' or card2 == 'ace clubs' or card2 == 'ace spades':
#                 if summ2 > 21:
#                         summ2 -= 10
#         print(f" summ card of 2 gambler {summ2}\n")
#         del x[card2]
#         del x1[g1]
#
#
#
#
# if summ1>21 and summ2>21:
#         print(f" summ card of 1 gambler {summ1}")
#         print(f" summ card of 2 gambler {summ2}")
#         print("both lost")
# elif summ1 == summ2:
#         print(f" summ card of 1 gambler {summ1}")
#         print(f" summ card of 2 gambler {summ2}")
#         print("draw")
# elif summ1 < summ2:
#         print(f" summ card of 1 gambler {summ1}")
#         print(f" summ card of 2 gambler {summ2}")
#         print("win 1 gambler")
# elif summ1 > summ2:
#         print(f" summ card of 1 gambler {summ1}")
#         print(f" summ card of 2 gambler {summ2}")
#         print("win 2 gambler")

# x = open("Kennedy.txt", "r")
# x = x.readlines()
# x = [i.rstrip("\n") for i in x]
#
# x2=x[0]
# x2 = x2.split(" ")
#
#
# x1 = open("Kennedy.txt", "r")
# x1=x1.read()
# x1= x1.split()
# t= {i:"" for i in x1}
#
#
# for g in range(0, len(x)):
#         x[g] = x[g].split(' ')
#         for h in range(0, len(x[g])):
#                 t[x[g][h]] += f"{g+1} "
# print(t)
#
# ind = open("indexI.txt", "w")
# list1 = [f"{i}: {t[i]}" for i in t]
# list1.sort()
# for i in list1:
#         ind.write(f"{i}\n")
# print(list1)

# ________________________________________________________
#  CLASS
# ________________________________________________________

# class Car:
#         def __init__(self,my_car):
#                 self.my_car = my_car
#
# print(Car(5).my_car)
#
# class Book:
#         def __init__(self, name_book, author, publisher):
#                 self.name_book = name_book
#                 self.author = author
#                 self.publisher = publisher
#
#         def set_name(self):
#                 self.name_book = str(input("Enter name book"))
#
#         def set_autor(self):
#                 self.author = str(input("Enter author"))
#
#         def set_publisher(self):
#                 self.publisher = str(input("Enter publisher"))
#
#         def get_name(self):
#                 return  self.name_book
#
#         def get_autor(self):
#                 return  self.author
#
#         def get_publisher(self):
#                 return  self.publisher
#
#         def __str__(self):
#                 return print(f"{self.name_book}{self.author}{self.publisher}")


# class Pet:
#         def __init__(self, name, animal_type, age):
#                 self.__name = name
#                 self.__animal_type = animal_type
#                 self.__age = age
#
#         def set_name(self):
#                 self.__name = str(input("enter name"))
#         def set_animal_type(self):
#                 self.__animal_type = str(input("enter type"))
#         def set_age(self):
#                 self.__age = str(input("enter age"))
#
#         def get_name(self):
#                 return self.__name
#         def get_animal_type(self):
#                 return self.__animal_type
#         def get_age(self):
#                 return self.__age
#
# def main():
#         x1 = Pet("gg","fff","ddd")
#         x1.set_age()
#         print(x1.get_age())
# main(
#
# pet_name=input('Введите кличку животного: ')
# pet_type = input('Введите вид животного: ')
# pet_age = int(input('Введите возраст животного: '))
#
# # Создать экземпляр класса Pet.
# mypet = pet.Pet(pet_name, pet_type, pet_age)

# if __name__ == '__main__':
#     main()

# class Car:
#         def __init__(self, year_model, make):
#                 self.__year_model = year_model
#                 self.__make = make
#                 self.__speed = 0
#         def accelerate(self):
#                 self.__speed += 5
#
#         def break1(self):
#                 self.__speed -= 5
#         def get_speed(self):
#                 return print(self.__speed)
# x1 = Car("1999","car")
# for i in range(0,5):
#         x1.accelerate()
#         x1.get_speed()
# for i in range(0,5):
#         x1.break1()
#         x1.get_speed()

# если в обекте то import car (- имя файла) и тогда x1 = сar.Car("1999","car")

# class Information:
#         def __init__(self,name,age,adress,tel):
#                 self.__name = name
#                 self.__age = age
#                 self.__adress = adress
#                 self.__tel = tel
#         def set_name(self):
#                 self.__name = str(input("enter name"))
#         def set_age(self):
#                 self.__age = int(input("enter age"))
#         def set_adress(self):
#                 self.__adress = str(input("enter adress"))
#         def set_tel(self):
#                 self.__tel = str(input("enter tel"))
#
#         def get_name(self):
#                 return print(self.__name)
#         def get_age(self):
#                 return print(self.__age)
#         def get_adress(self):
#                 return print(self.__adress)
#         def get_tel(self):
#                 return print(self.__tel)
#
#
# x1 = Information("Marina", 37, "Samara","777-77-77")
# x2 = Information("Marina1", 38, "Samara1","777-77-771")
#
# def show(x):
#         x.get_age()
#         x.get_adress()
#         x.get_name()
#         x.get_tel()
#
# show(x1)
# show(x2)


import pickle
# class Employee:
#         def __init__(self,name,id,department,position):
#                 self.__name = name
#                 self.__id = id
#                 self.__department = department
#                 self.__position = position
#         def set_name(self, name):
#                 self.__name = name
#         def set_id(self, id):
#                 self.__id = id
#         def set_department(self, department):
#                 self.__department = department
#         def set_position(self, position):
#                 self.__position = position
#
#         def get_name(self):
#                 return self.__name
#         def get_id(self):
#                 return self.__id
#         def get_department(self):
#                 return self.__department
#         def get_position(self):
#                 return self.__position
#
#
#         def get_all(self):
#                 return self.__name,self.__department, self.__position
#         def __str__(self):
#                 return f"{self.__name}, {self.__id}, {self.__department}, {self.__position}"

# x1 = Employee("Susen", 47899, "buh", "president")
#         x2 = Employee("Mark", 39119, "IT", "developer")
#         x3 = Employee("Joy", 123, "Proi", "engeneer")
#         s = [x1, x2, x3]
#         x = {i.get_id(): i for i in s}

# try:
#         f = open("empl.dat", "rb")
#         x = pickle.load(f)
#
# except:
#         x={}
# def main():
#         m=0
#         while m < 5:
#                 print("MENU\n----------------------")
#                 print(f"find employee -1\nadd employee -2\nchenge name, "
#                    "department,position -3\ndell employee -4\nEXIT - 5")
#
#                 m = int(input())
#                 if m == 1:
#                         t = int(input("Enter ID employee fo find"))
#                         print(x.get(t, f"{t} not in"))
#                 if m == 2:
#                         q1 = str(input("Enter name"))
#                         q2 = int(input("Enter id"))
#                         q3 = str(input("Enter department"))
#                         q4 = str(input("Enter position"))
#
#                         x[q2] = Employee(q1,q2,q3,q4)
#
#                 if m == 3:
#                         q2 = int(input("Enter id employee for change"))
#                         if q2 in x:
#                                 q1 = str(input("Enter name"))
#                                 q3 = str(input("Enter department"))
#                                 q4 = str(input("Enter position"))
#                                 x[q2] = Employee(q1, q2, q3, q4)
#
#                         else:
#                                 print("employee not find")
#                 if m == 4:
#                         q2 = int(input("Enter id employee for del"))
#                         if q2 in x:
#                                 del x[q2]
#                         else:
#                                 print("employee not find")
#                 if m == 5:
#                         print("end")
#         f = open("empl.dat", "wb")
#         pickle.dump(x, f)
#         print(x)
#
# main()


# class RetailItem:
#         def __init__(self, description, quantity, price):
#                 self.__description = description
#                 self.__quantity = quantity
#                 self.__price = price
#         def get_price(self):
#                 return self.__price
#
#         def ret(self):
#                 return f"{self.__description} {self.__quantity} {self.__price}"
#
#         def __str__(self):
#                 return f"{self.__description} {self.__quantity} {self.__price}"
#
# class CashRegister:
#         def __init__(self):
#                 self.__list1 = []
#
#         def purchase_item(self, RetailItem_item):
#                 self.__list1.append(RetailItem_item)
#
#         def get_total(self):
#
#                 summ = 0
#                 # for i in range(0, len(self.__list1)):
#                 #         summ += float(str(self.__list1[i]).split()[2])
#                 # return summ
#                 for i in self.__list1:
#                         summ += i.get_price()
#                 return summ
#         def show_item(self):
#                 l=""
#                 for i in self.__list1:
#                          l += str(i) + " "
#
#                 return print(l)
#
#         def clear(self):
#                 self.__list1 = []
#
#
#
# def main():
#         x1 = RetailItem('Пиджак', 12, float(59.95))
#         x2 = RetailItem('Дизайнерские джинсы', 40, float(34.95))
#         x3 = RetailItem('Рубашка', 20, float(24.95))
#
#
#         y = CashRegister()
#
#         s=0
#         while s != 1:
#                 w = int(input("what do you wanr to buy?: "
#                           "'Пиджак' enter 1\n"
#                           " 'Дизайнерские джинсы'\n 2"
#                           " 'Рубашка' enter 3 "))
#                 if w == 1:
#                         y.purchase_item(x1)
#                         y.show_item()
#                         print(y.get_total())
#                 if w == 2:
#                         y.purchase_item(x2)
#                         y.show_item()
#                         print(y.get_total())
#                 if w == 3:
#                         y.purchase_item(x3)
#                         y.show_item()
#                         print(y.get_total())
#
#                 s = int(input("what do another buy, enter 1 if no"))
#
# main()

class Question:
        def __init__(self,question, answer1,answer2, answer3, solution):
                self.__question = question
                self.__answer1 = answer1
                self.__answer2 = answer2
                self.__answer3 = answer3
                self.__solution = solution

        def get_question(self):
                return self.__question
        def get_answer1(self):
                return self.__answer1
        def get_answer2(self):
                return self.__answer2
        def get_answer3(self):
                return self.__answer3
        def get_solution(self):
                return self.__solution

        def set_solution(self, solution):
                self.__solution = solution









