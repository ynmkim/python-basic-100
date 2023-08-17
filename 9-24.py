# 9 ~ 24

# 9. 문자 1개 입력받아 그대로 출력하기
a = input()
print(a)

# 10. 정수 1개 입력받아 int로 변환하여 출력하기
n = input() # input에서 받아오는 데이터는 문자열이다.
n = int()
print(n)

# 11. 실수 1개 입력받아 변환하여 출력하기
f = input()
f = float(f)
print(f)

# 12. 정수 2개 입력받아 그대로 출력하기1
a = input()
b = input()
a = int(a)
b = int(b)
# 또는
# a = int(input())
# b = int(input())
print(a)
print(b)

# 13. 문자 2개 입력받아 순서 바꿔 출력하기1
a = input()
b = input()
print(b)
print(a)

# 14. 실수 1개 입력받아 3번 출력하기
a = float(input())
for i in range(3):
    print(a)

# 15. 정수 2개 입력받아 그대로 출력하기2
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 16. 문자 2개 입력받아 순서 바꿔 출력하기
a, b = input().split()
print(b, a)

# 17. 문장 1개 입력받아 3번 출력하기
a = input()
print(a, a, a)

# 18. 시간 입력받아 그대로 출력하기
a, b = input().split(':')
print(a, b, sep=':') # print('S','E','P', sep='@')

# 19. 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 20. 주민번호 입력받아 형태 바꿔 출력하기
a, b = input().split('-')
print(a, b, sep='')
# 또는
# a = input()
# a = a.replace("-", "")
# print(a)

# 21. 단어 1개 입력받아 나누어 출력하기
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# 또는
a = input()
for i in range(len(a)):
    print(a[i])

# 22. 연월일 입력받아 나누어 출력하기
a = input()
print(a[:2], a[2:4], a[4:], sep='')

# 23. 시분초 입력받아 분만 출력하기
h, m, s = input().split(':')
print(m)

# 24. 단어 2개 입력받아 이어 붙이기
a, b = input().split()
print(a+b)
# 또는
# a, b = input().split()
# print(a, b, sep='')
