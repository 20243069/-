# while 반복문
#  - 반복 횟수를 모르는 경우
#  - 조건이 만족하는 동안 계속 반복
#  - 조건 True → 반복
#  - 조건 False → 반복 종료
#  - while 조건에 True 명시하면 → 무한 Loop
#    (break문과 함께 사용)

#  * for, while 반복문에서 사용할 수 있는 키워드
#   1. break: 즉시 반복문을 빠져 나오세요(반복문 종료)
#   2. continue: 즉시 다음 반복으로 넘어가세요


while True:
    if True:
        break

print("Code")

# 숙제: for문으로 작성한 구구단 2단 코드를 while문으로 변경하세요.
#for i in range(1,10):
#    print(f"2x{i}= {2*i}")
i=1;
while i<10:
    print("2*%d=%d"%(i,i*2))
    i+=1