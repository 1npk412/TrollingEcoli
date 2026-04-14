#ThePrinter
import base64
answerList = ['a']
for i in range(0, len(answerList)):
    answerList[i] = base64.b64encode(answerList[i])
for i in range(0, len(answerList)):
    answer = base64.b64decode(answerList[i])
    answer = answer.decode('utf-8')
    print(f'#{i+1} is: {(answer)}')