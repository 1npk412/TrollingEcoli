#TheEncoder
import base64
answerList = ['a', 'b', 'c', 'd', '!' '.']
newAnswerList = []
for ans in answerList:
    ans = ans.encode(encoding='utf-8')
    ans = base64.b64encode(ans)
    ans = ans.decode(encoding='utf-8')
    ans = ans[:ans.index('=')]
    newAnswerList.insert(len(ans), ans)
print(newAnswerList)