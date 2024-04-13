def sum(listen):
     even_list = []
     odd_list = [] 
     for i in listen: 
        if i % 2 == 0: 
             even_list.append(i) 
         else:
             odd_list.append(i) 
     sum_even = sum(even_list) 
      sum_odd = sum(odd_list) 
      return [sum_even, sum_odd] 