from collections import *

def solution(phone_book):
    answer = True
    phone_book.sort()
    prev = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(prev):
            answer = False
            break
        prev = phone_book[i]
    
    return answer