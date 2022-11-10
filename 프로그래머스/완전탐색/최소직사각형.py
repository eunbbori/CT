def solution(sizes):
    
    w = []
    h = []
    answer = 0
    
    for i in range(len(sizes)) : 
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))

    answer = max(w) * max(h)
    return answer

# 다른 사람의 풀이 
def solution(sizes):
    answer = 0
    
    sizes = [sorted(size, reverse=True) for size in sizes]
    
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    
    width, height = max(widths), max(heights)
    
    answer = width * height
    
    return answer