import json
import random

file = json.load(open("qna.json",'r'))

qus=file['questions']
ans=file['answers']

inp=input("> ").lower()
inpt=inp.split(' ')
score=[]
i=0
for qus in qus:
    score.append(0)
    for q in qus:
        qu=q.split(' ')
        for que in qu:
            if que.lower() in inpt:
                score[i]+=1
    i+=1
if max(score)==0:
    print('Trouble understanding your question')
    exit(0)
ind=score.index(max(score))
answers = ans[ind]
nind=random.randint(0-1,len(answers))
print(answers[nind])