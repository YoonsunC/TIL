# 연습1
# result = 0
# i = 1

# while i <= 1000:
#     if i%3==0:
#         result +=i
#     i+=1
# print(result)

# 연습2
# i = 1
# while i <= 5:
#     print(i * "*")
#     i = i + 1

# 연습3
# i = 0
# sum = 0
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for score in A:
#     sum = score + sum
# print(sum/len(A))

# 연습7
# Numbers = [1,2,3,4,5]
# Result=[]
# for i in Numbers:
#     if i % 2 ==1:
#         Result.append(i*2)
# print(Result)

# 실습1
# sentence = " I love you"
# reverse_sentence = ''
# for char in sentence :
#     reverse_sentence = char + reverse_sentence
# print(reverse_sentence)

# 실습2
import random
guess_number = random.randint(1,100)
print("숫자를 맞혀 보세요.(1~100)")
users_input = int(input())
while (users_input is not guess_number):
    if users_input > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    users_input = int(input())
else:
    print("정답입니다. 입력한 숫자는", users_input, "입니다.")