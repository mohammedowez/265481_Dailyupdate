if __name__ == '__main__':
    n = int(input())
    x=[]
    a=[]
    a=list(map(int,input().split()))
    x=tuple(a)
    print(hash(x),sep='')


