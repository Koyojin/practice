def solution(n):
    n = int(input())

    line = 1
    next_num = 1

    if n == 1:
        print(1)
    else:
        while True:
            if n <= next_num:
                print(line)
                break
        
            next_num += (6 * line)
            line += 1 
    
for n in range(1, 1000000001):
    k = n // 6
    p = 0
    i = 1
    if n == 1:
        result = 1
    else:
        while True:
            p += i
            if p >= k:
                result = i + 1
                break
            i += 1
    if result != solution(n):
        print(f"Input n={n}, Expected={solution(n)}, Actual={result}")