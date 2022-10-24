from queue import Queue

'''
함수 processOrder를 구현하세요.
'''

class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue,vipQueue,time,orders) : 
    #삼항 연산자 
    normalIndex = -1 if len(normalQueue.queue) == 0 else normalQueue.queue[0]
    vipIndex = -1 if len(vipQueue.queue) == 0 else vipQueue.queue[0]

    if vipIndex == -1 : 
        return normalQueue

    if normalIndex == -1 : 
        return vipQueue    

    #우리가 밀린 작업이 normal에도 없고 vip에도 없는경우
    #더 빨리 도착한 주문을 처리한다 
    if time < orders[normalIndex].time and time < orders[vipIndex].time : 
        if orders[vipIndex].time <= orders[normalIndex].time  : 
            return vipQueue
        else : 
            return normalQueue 

    #우리가 밀린 작업이 normal에만 있는 경우 
    if time >= orders[normalIndex].time and time < orders[vipIndex].time : 
        return normalQueue

    #우리가 밀린 작업이 vip에만 있는 경우 
    if time >= orders[vipIndex].time and time < orders[normalIndex].time : 
        return vipQueue    

    #우리가 밀린 작업이 normal에도 있고 vip에도 있는경우 
    #vip를 반환한다 
    return vipQueue

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''
    result = []

    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0  
    curTime = -1 #절대로 존재할 수 없는 값 

    for i in range(len(orders)) : 
        curTime = orders[i].time 

        if orders[i].vip == 0 : 
            normalQueue.put(i)
        else : 
            vipQueue.put(i)


    while jobEndTime <= curTime and not(normalQueue.empty() and vipQueue.empty()) :   #주문이 밀려있고(현재시간보다 일이끝난시간이 더 작다) 
            targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders) # normalQueue 또는 vipQueue를 선택한다 

            #우리가 처리할 주문 번호를 가져온다 
            index = targetQueue.queue[0]

            #주문을 처리한다 = jobEndTime을 증가시킨다 
            #jobEndTime이 order[index].time 보다 큰 경우 : 
                #주문이 밀려있어서 이전 작업이 끝나자마자 바로 다음 작업을 시작한 경우 
            #order[index].time이 jobEndTime보다 큰 경우 : 
                #주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우
                #다음 작업이 들어온 시점에 처리한다 
            jobEndTime = max(jobEndTime,orders[index].time) + orders[index].duration 
            result.append(index+1)
            targetQueue.get()

    while not(normalQueue.empty() and vipQueue.empty() ) :   #주문이 밀려있고(현재시간보다 일이끝난시간이 더 작다) 
            targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders) # normalQueue 또는 vipQueue를 선택한다 

            #우리가 처리할 주문 번호를 가져온다 
            index = targetQueue.queue[0]

            #주문을 처리한다 = jobEndTime을 증가시킨다 
            #jobEndTime이 order[index].time 보다 큰 경우 : 
                #주문이 밀려있어서 이전 작업이 끝나자마자 바로 다음 작업을 시작한 경우 
            #order[index].time이 jobEndTime보다 큰 경우 : 
                #주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우
                #다음 작업이 들어온 시점에 처리한다 
            jobEndTime = max(jobEndTime,orders[index].time) + orders[index].duration 
            result.append(index+1)
            targetQueue.get()


    

    return result