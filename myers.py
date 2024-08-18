def myers_diff(m, n):
    max_edits= len(m)+len(n)
    v= {1:0} #dictionary to keep track of the furthest x-coordinate we can reach at each move
    trace= [] #to keep track of v for each move
    for d in range(1, max_edits+1): #the maximum no. of edits to get to target string from source
    #string is equal to sum of lenghts of 
        for k in range(-d, d, 2): #k= x-y; k represents the diagonal. For each diagonal, determine
            #whether to move right (deletion) or downward (insert)
            #if k= -d, we move downward. if k= +d, we move rightward
            if k== -d or (k != d and v.get(k-1, 0) < v.get(k+1, 0)):
                #k==-d represents the left most diagonal we can reach after d edits, if true
                #we must move rightwards
                x= v.get(k+1, 0)
            else:
                x= v.get(k-1, 0)+1 #move down
            y= x-k


a= "abc"
b= "abb"

myers_diff(a,b)