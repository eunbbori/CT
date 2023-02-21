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