# 방법 1
def solution(cacheSize, cities):
    time = 0
    cache = []
    cities = [x.lower() for x in cities]
    for city in cities:
        if city not in cache:
            time += 5
            if cacheSize > len(cache):
                cache.append(city)
            else:
                cache.append(city)
                cache.pop(0)
        else : 
            time += 1
            cache.pop(cache.index(city))
            cache.append(city)
            
                
    
    return time

#방법 2 
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time