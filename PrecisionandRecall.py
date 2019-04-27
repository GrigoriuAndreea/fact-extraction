# true=[1,0,0,1]
# pred=[1,1,1,0]
# prec=1/3
# rec=1/2
import os
import ast
import pandas as pd
# totalpre=0
# totalrec=0
# for i in pred:
#     if i==1:
#         totalpre=totalpre+1
# for j in true:
#     if j==1:
#         totalrec=totalrec+1
# result=0
# for ind in range(len(true)):
#     if pred[ind]==1:
#         if pred[ind]==true[ind]:
#             result=result+1
# print('prec' + str(result) + str(totalpre) )
# print('rec'+ str(result) + str(totalrec))
newf=open('Unseendata\\Classification\\SVMEmbPOSPrecRecv2.csv', 'w')
newf.write('Case'+','+'Precision'+','+'Recall'+','+'Precision%'+','+'Recall%'+'\n')
for file in os.listdir('Unseendata\\Classification\\manual\\'):
    file=file.split('.')
    f = open("Unseendata\\Classification\\SVM\\EmbPOS\\" + 'N+Vpair'+file[0]+'.txt', "r",encoding='utf-8')
    text=f.readlines()
    pred=ast.literal_eval(text[0])
    df=pd.read_csv('Unseendata\\Classification\\manual\\'+file[0]+'.csv',encoding='ISO-8859-1',header=None)
    true=df[1].tolist()
    totalpre=0
    totalrec=0
    for i in pred:
        if i==1:
            totalpre=totalpre+1
    for j in true:
        if j==1:
            totalrec=totalrec+1
    result=0
    for ind in range(len(true)):
        if pred[ind]==1:
            if pred[ind]==true[ind]:
                result=result+1
    # print('prec' + str(result) + str(totalpre) )
    # print('rec'+ str(result) + str(totalrec))
    precision=result/totalpre
    recal=result/totalrec
    newf.write(file[0]+','+str(result)+'//'+str(totalpre)+','+str(result)+'//'+str(totalrec)+','+str(precision)+','+str(recal)+'\n')
