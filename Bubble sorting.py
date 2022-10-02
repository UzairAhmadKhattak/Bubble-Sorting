numlist = [4,2,3,1]

for _ in range(len(numlist)):
    for i in range(len(numlist)):
        try:
            if numlist[i] > numlist[i+1]:
                first = numlist[i]
                second = numlist[i+1]
                numlist[i] = second
                numlist[i+1] = first 


        except:
            pass

numlist
