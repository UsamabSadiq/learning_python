# import time

# # print(time.time())
# # print(time.ctime())


# for i in range(4):
	
# 	# using sleep() to halt execution
# 	# time.sleep(3)
# 	print(i)


# # using simple format of showing time
# s = time.strftime("%a, %d %b %Y %H:%M:%S") 
# print(s)

x = int(input('Enter any Number: '))

match x:
    case _ if x < 20:
        print('value is Less than 20')
    case _ if x > 20:
        print('value is Greater than 20')
    case _ if x == 20:
        print('value is 20')
    case _:
        print(x)



