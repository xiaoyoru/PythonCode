score1 = int(input('請輸入第一個成績'))
score2 = int(input('請輸入第二個成績'))
score3 = int(input('請輸入第三個成績'))

score = [score1, score2, score3]

score.sort()

final = score[0] * 0.2 + score[1] * 0.3 + score[2] * 0.5

print(final)

