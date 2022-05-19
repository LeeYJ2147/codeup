#[기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
t=ord(input())
c=ord('a')
while c<=t :
    print(chr(c), end=' ')
    c+=1