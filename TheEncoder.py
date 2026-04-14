#TheEncoder
import base64
answerList = ['To collect a reference genome (so like a transcript) of the cuttlefish genome to be used for comparison of the cuttlefish due to research of the organism being limited by the lack of a strong reference genome.'
,'They used PCR and gel electrophoresis in order to extract reference DNA from the fish. The DNA used for the PCR was extracted by some weird tech that we didn’t learn in AP Bio so the college board won’t test us on it.'
, 'This is a weird question because this is like asking what Bob discovered when he made his toy. What I mean is how the study was meant to achieve a DNA sequence of the cuttlefish genome in order to be used for future studies as a reference point. It’s like a benchmark test for a car seeing what it looks like and how accurate its measurements (codons are).'
, 'The genome is the entire DNA sequence while the transcriptome is the parts of the DNA that are produced from transcription (RNA). We study both in tandem because alternative splicing which is done by cuttlefish can be tracked via comparing the genome and transcriptomes as they will not be exactly much 1 to 1 due to alternative splicing. Meat is not the same when sliced into different sizes and cooked to different temperatures.']
i = 0
for ans in answerList:
    i = i+1
    ans = ans.encode(encoding='utf-8')
    ans = base64.b64encode(ans)
    ans = ans.decode(encoding='utf-8')
    try:
        pass
        #ans = ans[:ans.index('=')]
    except:
        pass
    print(f'{i}:  {ans}')
    #newAnswerList.insert(len(ans), ans)
#print(newAnswerList)