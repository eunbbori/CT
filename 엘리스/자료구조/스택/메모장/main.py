from notepad import notepad


def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    
    s = input()
    
    n = int(input())
    
    commands = []
    
    for i in range(n) :
        commands.append(input())
        
    print(notepad(s, commands))

if __name__ == "__main__":
    main()


