#반올림: round(a), round(a,b)
print(round(3.33))
print(round(3.66))
print(round(3.66,1)) #소숫점 1번째 자리까지 숫자를 만들어라(기준)

#절대값: abs(a)
print(abs(3))
print(abs(-3))

#제곱: pow(a,b)
print(pow(3,2))
print(3**2)

#나눗셈: divmod(a,b)
x,y=divmod(7,2) #7나누기2했을때
print(x) #몫
print(y) #나머지

#최대값: max(a,b,c,d,...)
print(max(1,3,5,7))
#최소값: min(a,b,c,d,...)
print(min(1,3,5,7))
#합: sum(집합형태:Iterable)
print(sum([1,3,5,7]))