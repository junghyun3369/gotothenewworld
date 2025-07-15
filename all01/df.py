f = open('all01\\고담팀.csv', mode='r', encoding='UTF-8')
arr = f.readlines()

def 함수1(arr):
    arr2 = []
    for row in arr:
        row = row.replace("\n","")
        arr2.append( row.split(","))
    return arr2
    
arr2 = 함수1(arr)


def 함수2(arr2):
    for row in arr2:
        arr3 = ""
        for v in row:
            arr3 += 'O' if v == 'O' else ' '
        print(arr3)
    
함수2(arr2)