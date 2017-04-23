def radix_sort(a, count):
  l = a
  modulo = 10
  div = 1
  max = None
    
  while True:
    queue = [[] for i in range(10)]
    for value in l:
      if max == None or value > max:
        max = value
        
      digit = (value % modulo) // div
      queue[digit].append(value)
        
    modulo *= 10
    div *= 10

    l = [value for sublist in queue for value in sublist]
    
    if max < div:
      return l
    
a = [{'data': [10000, 1000, 100, 10, 0], 'expected': [0, 10, 100, 1000, 10000]},
      {'data': [1,2,43,66,3,64,56,356], 'expected': [1, 2, 3, 43, 56, 64, 66, 356]},
    ]
      
for test in a:
    result = radix_sort(test['data'], len(test['data']))
    print(result)
    assert result == test['expected']