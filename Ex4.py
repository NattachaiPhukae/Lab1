i = input("Enter Step of Harmonic : ")
i = int(i)

def loop(i):
    if i == 0:
        return 0
    else:
        result = (1/(i+1)+loop(i-1))
        print(f"Limit = {i}  result = {result}")
        return result
loop(i)