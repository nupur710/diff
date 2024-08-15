import functools

#Levenshtien function takes in 2 strings and returns
#the Levenshtien distance (the no. of stpes to go from)
#string s1 (source) to s2 (destination)

#@functools.lru_cache(maxsize=None)
def lev_impl(s1, s2, n1, n2, cache):
    #print(s1[:n1], s2[:n2])
    if cache[n1][n2] is not None:
        return cache[n1][n2]
    if(n1 == 0):
        j= cache[n1][n2]= n2
        trace_cache(cache)
        return cache[n1][n2]
    if(n2 == 0):
        k= cache[n1][n2]= n1
        trace_cache(cache)
        return cache[n1][n2]
    if(s1[n1-1] == s2[n2-1]):
        l= cache[n1][n2]= lev_impl(s1, s2, n1-1, n2-1, cache)          #ignore 
        trace_cache(cache)
        return cache[n1][n2]                              
    cache[n1][n2]= 1 + min(lev_impl(s1, s2, n1-1, n2, cache),       #remove
                lev_impl(s1, s2, n1, n2-1, cache),                  #add
                lev_impl(s1, s2, n1-1, n2-1, cache))                #replace
    trace_cache(cache)
    return cache[n1][n2]

def lev(s1, s2):
    #Levenshtein distance has O(n1*n2) time complexity
    #where len(s1)= n1 & len(s2)= n2, to improve TC
    #we implement caching
    cache= []
    n1= len(s1)
    n2= len(s2)
    for i in range(n1+1):  #we create no. of rows & cols in cache to be len+1 to accomodate case when n1=value provided
        cache.append([None]*(n2+1)) 
    print(cache)
    return lev_impl(s1, s2, n1, n2, cache)

def trace_cache(cache):
    for row in cache:
        for item in row:
            print('-' if item is None else item, end=' ')
        print()

print("str distance is " ,lev("foooooooooooooooooooooooo", "food"))