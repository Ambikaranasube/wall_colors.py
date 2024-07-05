s=list(input())
#W,R,B house,minimize the badness
#try to change the color of W house with previous color
#edge case -if 1st house is white take next house
for i in range(len(s)):
    if s[i]=="W":
        if i==0: #edge case
            for j in range(1,len(s)): 
                if s[j]!="W": #if 1st el
                    s[i]=s[j]
                    break
        else:  
            s[i]=s[i-1]
badness=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        badness+=1
print(badness)
        
