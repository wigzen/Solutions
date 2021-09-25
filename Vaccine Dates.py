
def vaccine():
    # for x in range(3):
    s = list(map(int,input().split()))

    if s[1]<s[0]<s[2]:
        print("Take second dose now")
    elif s[0]<=s[1]:
        print("Too Early") 
    else:
        print("Too Late")     

t = int(input())
while t:
    vaccine()        