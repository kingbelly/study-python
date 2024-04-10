a=10
b=5 #int (정수형)
c=2.0 #float (실수형)
d=0.5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫만 나옴
print(a%b)
print(a**b)
print(b+c)
print(b-c)
print(b*c)
print(b/c)
print(b//c)
print(b%c)
print(b**c)
#비교연산자,논리연산자
x=10
y=-10
print(x>0)
print(x<y)
print(x==y)
print(x>0 or y>0)
print(x>0 and y>0)
print(not x<0)
#문자열형 str - 문자열 다루는 다양한 메소드 split,join,upper,lower,replace
a=5
b='5'
c=5.0
print(a+a) #int+int가능
print(b+b) #str+str 가능
print(a*b) #int*str 가능
'''
print(a+b) int + str불가능
print(b*c) int*float 불가능
'''
#군집 자료형 list, tuple, set, dictionary
#자료형 변환 - 방법: 원하는 자료형 함수에 값을 넣는다 예) str(10), int('10')
a=int(input('숫자를 입력하세요.')) #대체 어떻게 입력하라고
print(a+a)
num=5.0
range(int(num))