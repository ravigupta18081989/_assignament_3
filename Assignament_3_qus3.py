str = 'The quick Brow Fox'
count1=0
count2=0
for i in str:
        if (i.isupper()):
            count1=count1+1
        elif (i.islower()):
            count2=count2+1
print("No of Upper case characters: ",count1)
print("No of Lower case characters: ",count2)