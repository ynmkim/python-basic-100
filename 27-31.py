# 27. 10진 정수 입력받아 16진수로 출력하기1
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
a = input()
a = int(a)
print('%x'%a)  # print(hex(a))

# 28. 10진 정수 입력받아 16진수로 출력하기2
a = input()
a = int(a)
print('%X'%a)

# 29. 16진 정수 입력받아 8진수로 출력하기
a = input()
a = int(a, 16)
print('%o'%a)

# 30. 영문자 1개 입력받아 10진수로 변환하기
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
a = ord(input())
print(a)

# 31. 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
a = int(input())
print(chr(a))


