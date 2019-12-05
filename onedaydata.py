from test03 import judge
from ts01 import is_del
def processdata():
    data= {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [],10:[],11:[],12:[],13:[]}
    signal=''
    final=[]
    part = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [],10:[],11:[],12:[],13:[]}
    i=0
    with open('2018_11_06.log', "r") as f:#路径C:\Program Files\CZ ICS Term\eTerm3\+filename
        lines = f.readlines()
        for line in lines:
            signal = judge(line, signal)
            if signal == '':
                continue
            if signal == 'begin' or signal == 'continue':
                data[i].append(line)
                continue
            if signal == 'end':
                signal = ''
                for go in data[i]:
                    if not is_del(go):
                        part[i].append(go)
                yield part[i]
                i=i+1



