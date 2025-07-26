def fanli(amount,rate):
    year=1
    while year<=10:
      print('year'+str(year)+':'+str(amount*0.05+amount))
      amount=amount*0.05+amount
      year+=1
fanli(100,0.05)
