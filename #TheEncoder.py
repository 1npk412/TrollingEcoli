#TheEncoder

answerList = ['b', 'c', 'g']
newAnswerList = []
for ans in answerList:
    ans = ans.encode(encoding='utf-8')
    newAnswerList.insert(-1, ans)
