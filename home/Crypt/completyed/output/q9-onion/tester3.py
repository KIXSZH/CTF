import time
import sys
import string
import time
import threading
import random
t =1
count = 1


alph = string.ascii_letters
alpha ="abcdefghijklmnopqrstuvwxyzABCDEFG"
flag6 = list(alpha)

'''
flag6 = list(flag)
count = 5
flag6[count] = al[count]
flag6 = ''.join(flag6)
print(flag6)'''
al3="THIS_BEHIND_IT_NOT_THAT_YOU_THINk"
al4="THIS_BEHIND_IT_NOT_THAT_YOU_THINk"
al5="THIS_BEHIND_IT_NOT_THAT_YOU_THINk"
al6="THIS_BEHIND_IT_NOT_THAT_YOU_THINk"
al = "bYtE_BuStErS{$#Thisisurfirstfl#$}"
al1="THIS_IS_NOT_THE_REAL_FLAG_BEHIND_IT-"
al2="THIS_BEHIND_IT_NOT_THAT_YOU_THINk"
al7="THIS_BEHIND_IT_NOT_THAT_YOU_THINk"

def ct():
       global flag6
       x = random.randint(0, 32)
       flag6 = list(flag6)
       flag6[x] = al[x]
       flag6 = ''.join(flag6)
count = 0
done =True
don = False
do = False
d = False
def ct1():
       global  done
       global count
       global flag6
       x = random.randint(0, 32)
       flag6 = list(flag6)
       flag6[x] = al1[x]
       flag6 = ''.join(flag6)
       count = count + 1
       if count  == 50:
              done = False
              don = True
              

def ct2():
       global don
       global count
       global al2
       global flag6
       x = random.randint(0, 32)
       flag6 = list(flag6)
       al2[x] = flag6[x]
       flag6 = ''.join(flag6)
       count = count + 1
       if count  == 50:
              don = False
              do =True


def ct3():
       global don
       global count
       global al2
       global flag6
       x = random.randint(0, 32)
       flag6 = list(flag6)
       al3[x] = flag6[x]
       flag6 = ''.join(flag6)
       count = count + 1
       if count  == 50:
              do = False
              d =True
              

def ct4():
       global don
       global count
       global al2
       global flag6
       x = random.randint(0, 32)
       flag6 = list(flag6)
       al4[x] = flag6[x]
       flag6 = ''.join(flag6)
       count = count + 1
       if count  == 50:
              do = False
              d =False
              

done = True
def change():
       while True:

              global count
              sys.stdout.write('\r' + ' ' * len(str(flag6)))
              sys.stdout.flush()


              if done:
                     ct1()
                     
              if don:
                     ct2()
              if do:
                     ct3() 
              if d:
                     ct4()                    
              else:
                     ct()

                     # Update the variable (you can replace this with your o
              sys.stdout.write('\r ' + flag6)
              sys.stdout.flush()

              time.sleep(1)

change()























































