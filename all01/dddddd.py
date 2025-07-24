def 빈칸출력(파일명):
    f = open(f'all01\\{파일명}', mode='r', encoding='UTF-8')
    arr = f.readlines() 
    arr2 = []
    for row in arr:
        row = row.replace("\n", "")
        arr2.append( row.split(",") )
        print('='*30)
    for row in arr2:
        행 = ""
        for v in row:
            행 += 'O' if v == 'O' else ' '
        print(행)
    
빈칸출력('data4.csv')
빈칸출력('data5.csv')
빈칸출력('data6.csv')