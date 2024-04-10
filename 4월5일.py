#한줄에 하나씩 숫자 입력받기
a=int(input('a입력')) #3
b=int(input('b입력')) #6 
c=int(input('c입력')) #9
print(a,b,c,a+b+c) # 3 6 9 18 --> int 없애면 3 6 9 369

#한줄에 여러 개의 숫자 입력받기
a,b,c=map(int,input('a b c값 입력').split())
print(a,b,c,a+b+c)

#스플릿 사용형태:문자1.split(문자2): 문자2를 기준으로 문자1을 자른다.
text+input('날짜입력 yyyy.mm.dd')#2024.04.05 넣는다 치면
y,m,d=text.split('.') #.을 기준으로 y,m,d를 자른다! ''안에 비워두면 공백 기준으로 잘림
print(text,y,m,d) #2024.04.05 2024 04 05 <---이렇게 됨