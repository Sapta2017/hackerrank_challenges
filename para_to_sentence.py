# Enter your code here. Read input from STDIN. Print output to STDOUT
import nltk
from nltk import pos_tag, word_tokenize, FreqDist

txt=raw_input()
txt=txt.replace("?","? ")
txt=txt.replace(".",". ")
txt=txt.replace('. "','."')
txt=txt.replace('? "','?"')
sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer()
output=sent_tokenizer.tokenize(txt)

op123 = []
idx=999
for op in output:
    if op.startswith('"') & op.endswith('"'):
            idx = output.index(op)
            op12 = output[idx] + " " + output[idx+1]
            op123.append(op12)
            idx=idx+1
    elif output.index(op) == idx:
            pass
    else:
        op123.append(op)
        
for stdout in op123:
    print stdout
