# my_str = "Just do it!"
# print(my_str[5:-2])


# text = "Hello, Python!"
# text = "Hello, Python!"
# text = "Hlo, ythn!"

# #콜론 뒷부분은 포함 (X)

# slice1 = text[1:5] # 결과: "ello"

# # 처음부터 5 전까지 자르기

# slice2 = text[:5] # 결과: "Hello"

# # 7부터 끝까지 자르기

# slice3 = text[7:] # 결과: "Python!"



# numbers = [10, 20, 30, 40, 50]
# # 인덱스 1부터 3 전까지 자르기
# a = numbers[1:3]  # 결과: [20, 30]
# # 뒤에서 2번째 요소부터 끝까지 자르기
# b = numbers[-2:]  # 결과: [40, 50]
# # 전체 리스트를 거꾸로 뒤집기
# c = numbers[::2] # 결과: [50, 40, 30, 20, 10]

# print(a)
# print(b)
# print(c)




# 문제: 온라인 상태인 상위 유저만 보여주기
# 온라인 게임의 접속자 명단이 딕셔너리로 주어집니다. 
# Key는 유저 아이디, Value는 온라인 상태(True는 온라인, False는 오프라인)를 나타냅니다.
# 이 딕셔너리에서 가입 순서상 앞쪽 3명의 유저 중, 
# 현재 온라인 상태(True)인 유저만 골라서 새로운 딕셔너리로 만들어 출력하는 코드를 작성하세요.

# ++++++++++문제 해결 순서 힌트+++++++++++++++

# all_users 딕셔너리의 Key들을 리스트로 만듭니다.

# 만들어진 키 리스트를 슬라이싱해서 앞의 3개만 잘라냅니다. (['KimGamer', 'LeeCoder', 'ParkPython'])

# for문을 이용해 잘라낸 키 리스트를 하나씩 확인합니다.

# if문을 이용해 각 키에 해당하는 유저의 상태(Value)가 True인지 확인합니다.

# True인 유저만 새로운 딕셔너리에 추가합니다.


# 주어진 값:

all_users = {
    'KimGamer': True,
    'LeeCoder': False,
    'ParkPython': True,
    'ChoiMaster': True,
    'YoonNoob': False
}

# 출력 예시:

# {'KimGamer': True, 'ParkPython': True}










