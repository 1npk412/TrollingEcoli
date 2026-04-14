#ThePrinter
import base64


def createAnswerList():
    returnList = []
    for i in range(1,5):
        answer = input(f'Enter answer for {i}:')
        returnList.append(answer.encode(encoding='utf-8'))
    return returnList

def getAnswer(answerList):
    try:
        for i in range(0, len(answerList)):
            answer = base64.b64decode(answerList[i])
            answer = answer.decode('utf-8')
            print(f'#{i+1} is: {(answer)}')
    except:
        print('this code has no use besides looking fancy')
        for i in range(0, len(answerList)):
            answerList[i] = base64.b64encode(answerList[i])
        getAnswer(answerList)

getAnswer(createAnswerList())
