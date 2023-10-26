def markup_fee_range(amount):
    
   if amount  in range(0, 1000001):
       result = amount*0.1
       print(result)
       return result
       
   elif amount in range(1000001, 2000001):
       result = amount*0.05
       print(result)
       return result
      
   elif amount in range(2000001, 10000001):
       result = amount*0.03
       print(result)
       return result
       
   elif amount in range(10000001, 10000000000):
       result = amount*0.02
       print(result)
       return result
       
   else:
       print("Please enter a valid amount")
       
       