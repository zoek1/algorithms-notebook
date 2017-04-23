def insercion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        
    return a

a = [{'data': [10000, 1000, 100, 10, 0], 'expected': [0, 10, 100, 1000, 10000]},
      {'data': [1,2,43,66,3,64,56,356], 'expected': [1, 2, 3, 43, 56, 64, 66, 356]},
    ]
      
for test in a:
    result = insercion_sort(test['data'])
    print(result)
    assert result == test['expected']