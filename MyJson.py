from flask import json


def test():
    lista=[]

    data1 = {'user': 789, 'email': 456, 'data': 123}
    lista.append(data1)
    #lista.append(data2)
    d1=json.dumps(lista)
    print d1
    print str
    return d1



if __name__=='__main__':
    test()