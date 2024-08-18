import functools

#Tutorial: https://www.youtube.com/watch?v=tG4IeY01-xw

#Levenshtien function takes in 2 strings and returns
#the Levenshtien distance (the no. of stpes to go from)
#string s1 (source) to s2 (destination)

@functools.lru_cache(maxsize=None)
def lev_base(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[-1] == s2[-1]:
        return lev_base(s1[:-1], s2[:-1])
    return 1 + min(lev_base(s1[:-1], s2), lev_base(s1, s2[:-1]), lev_base(s1[:-1], s2[:-1]))

#custom cache
def lev_impl(s1, s2, n1, n2, cache):
    if cache[n1][n2] is not None:
        return cache[n1][n2]
    if(n1 == 0):
        cache[n1][n2]= n2
        trace_cache(cache)
        return cache[n1][n2]
    if(n2 == 0):
        cache[n1][n2]= n1
        trace_cache(cache)
        return cache[n1][n2]
    if(s1[n1-1] == s2[n2-1]):
        cache[n1][n2]= lev_impl(s1, s2, n1-1, n2-1, cache)          #ignore 
        trace_cache(cache)
        return cache[n1][n2]                              
    cache[n1][n2]= 1 + min(lev_impl(s1, s2, n1-1, n2, cache),       #remove
                lev_impl(s1, s2, n1, n2-1, cache),                  #add
                lev_impl(s1, s2, n1-1, n2-1, cache))                #replace
    trace_cache(cache)
    return cache[n1][n2]

#non-recursive approach
def lev_impl_back(s1, s2):
    cache= []
    for _ in range(len(s1)+1):
        cache.append([None]*(len(s2)+1))
    for n2 in range(len(s2)+1):   
        n1= 0
        cache[n1][n2]= n2  #initialize 1st row of cache
        trace_cache(cache)
    for n1 in range(len(s1)+1):
        n2= 0
        cache[n1][n2]= n1  #initialize 1st col of cache
        trace_cache(cache)
    for n1 in range(1, len(s1)+1):
        for n2 in range(1, len(s2)+1):
             if s1[n1-1]== s2[n2-1]:
                 cache[n1][n2]= cache[n1-1][n2-1]
                 trace_cache(cache)
                 continue
             cache[n1][n2]= 1 + min((cache[n1-1][n2]), cache[n1][n2-1], cache[n1-1][n2-1])
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
    return lev_impl(s1, s2, n1, n2, cache)


TRACE=False
if TRACE:
        def trace_cache(cache):
            for row in cache:
                for item in row:
                    print('-' if item is None else str(item).ljust(3), end=' ')
                print()
else:
    def trace_cache(*args):
        pass

#print("str distance by recursive method is ", lev("foo", "bar"))
print("\n********************************************************************\n")
print("str dist by non-recursive method is ", lev_impl_back("foo", "bar"))