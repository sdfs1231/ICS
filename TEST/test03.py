def judge(data,signal):
    lenght=len(data)
    if lenght>=6:
        if signal=='begin' or signal=='continue':
            if data[0]+data[1]+data[2]+data[3]+data[4]+data[5]=='FLIGHT':
                return 'end'
        if data[1]+data[2]+data[3]=='fdl':
            return 'begin'
        if signal=='begin' or signal=='continue':
            return 'continue'
    else:
        if signal=='begin' or signal=='continue':
            return 'continue'
        else:
            return ''
