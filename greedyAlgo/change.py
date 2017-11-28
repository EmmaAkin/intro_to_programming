# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    if m >= 10:
        count = count + int(m/10)
        m = m%10
    if m>=5:
        count = count + int(m/5)
        m = m%5
    if m>=1:
        count = count + int(m/1)


    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))



# # Uses python3
# import sys

# def get_change(m):
#     #write your code here
#     return m

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))
