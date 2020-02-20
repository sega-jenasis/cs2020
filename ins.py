#! /usr/bin/python3
#jena and thomas
from textblob import TextBlob
import pandas as pd
import io
import matplotlib.pyplot as plt
import sys
import re
import warnings

warnings.filterwarnings('ignore')
#file managment
print ("Running %s " % (sys.argv[0]))
if len(sys.argv) < 2:
    print("Give file name")
    sys.exit()
else:
    text = open(sys.argv[1],"r")

txt = text.read()
print("Me read  %s" % str(sys.argv[1]))

txt = txt.replace('\n', ' ').replace('\r', ' ')

txt = txt.replace('. ', '\n')
#txt = unicode(txt, 'utf-8')
f = io.StringIO(txt)
numbered = f.readlines()

rows_list = []
i = 1
for line in numbered:
    new_row = {'line':i, 'text':line.strip()}
    rows_list.append(new_row)
    i+=1
df = pd.DataFrame(rows_list, columns = ['line', 'text', 'game', 'polarity'])

def get_polarity(text):
    try:
        return TextBlob(text).sentiment.polarity
    except Exception:
        print("Exception exist")
        return n/a

def get_game(text):
    patterns = ['avengers', 'cyberpunk', 'doom', 'dying light', 'final fantasy', 'gods', 'last of us', 'ori', 'rainbow', 'skull', 'vampire', 'watch dogs']

    for pattern in patterns:
        if re.search(pattern, text):
            return pattern
            #   it is now replaced with line 58 - 61

#fill assigned values for df1
df['polarity'] = df['text'].apply(get_polarity)
df['game'] = df['text'].apply(get_game)

i = 0
for index, row in df.iterrows():
    if df['game'][i] == None:
        df['game'][i] = df['game'][i-1]
    i+=1

#prepare df for major graph
df['polsum'] = df['polarity'].cumsum()

#prepare assigned values for df1..12 - i n   g r o u p s  !   DFG
dfg = df.groupby("game")
for key, item in dfg:
    print(dfg.get_group(key), "\n\n")

print("this cuts the info")
#individual df per game df1...12
df1 = dfg.get_group("avengers")[['line', 'text', 'game', 'polarity']]
df2 = dfg.get_group("cyberpunk")[['line', 'text', 'game', 'polarity']]
df3 = dfg.get_group("doom")[['line', 'text', 'game', 'polarity']]
df3.reset_index()
print(df3)
df4 = dfg.get_group("dying light")[['line', 'text', 'game', 'polarity']]
df5 = dfg.get_group("final fantasy")[['line', 'text', 'game', 'polarity']]
df6 = dfg.get_group("gods")[['line', 'text', 'game', 'polarity']]
df7 = dfg.get_group("last of us")[['line', 'text', 'game', 'polarity']]
df8 = dfg.get_group("ori")[['line', 'text', 'game', 'polarity']]
df9 = dfg.get_group("rainbow")[['line', 'text', 'game', 'polarity']]
df10 = dfg.get_group("skull")[['line', 'text', 'game', 'polarity']]
df11 = dfg.get_group("vampire")[['line', 'text', 'game', 'polarity']]
df12 = dfg.get_group("watch dogs")[['line', 'text', 'game', 'polarity']]

#THIS IS PLOT #1
#plottitle = "Overall Video Game Polarity After Delay"

#fig,ax = plt.subplots(facecolor ='grey')
#ax.set_facecolor('#a6a6a6')
#ax.set_title(plottitle, color ='black')
#ax.set_xlabel('Time After Delay', color ='black')
#ax.set_ylabel('Overall Polarity', color ='black')
#ax.plot(df['line'], df['polarity'], '#808080', label='Overall Polarity')
#ax.tick_params(labelcolor='grey')
#plt.legend()

#THIS IS PLOT #2
plottitle2 = "Individual Video Game Polarity After Delay"

fig,ax = plt.subplots(facecolor ='grey')
ax.set_facecolor('#a6a6a6')
ax.set_title(plottitle2, color ='black')
ax.set_xlabel('Time After Delay', color ='black')
ax.set_ylabel('Overall Polarity', color ='black')
ax.plot(df1['line'], df1['polarity'], '#917381', label='avengers')
ax.plot(df2['line'], df2['polarity'], '#518264', label='cyberpunk')
ax.plot(df3['line'], df3['polarity'], '#521434', label='doom')
ax.plot(df4['line'], df4['polarity'], '#517982', label='dying light')
ax.plot(df5['line'], df5['polarity'], '#817069', label='final fantasy')
ax.plot(df6['line'], df6['polarity'], '#018759', label='gods')
ax.plot(df7['line'], df7['polarity'], '#319706', label='last of us')
ax.plot(df8['line'], df8['polarity'], '#014782', label='ori')
ax.plot(df9['line'], df9['polarity'], '#971805', label='rainbow')
ax.plot(df10['line'], df10['polarity'], '#106030', label='skull')
ax.plot(df11['line'], df11['polarity'], '#548290', label='vampire')
ax.plot(df12['line'], df12['polarity'], '#957516', label='watch dogs')
ax.tick_params(labelcolor='grey')
plt.legend()

plt.show()
