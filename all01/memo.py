def 메모장생성():
    파일명 = input("신규 파일명을 입력하세요.")
    return open(f'all01\\{파일명}.txt', mode='w', encoding='UTF-8')


def 메모장글쓰기(파일):
    while True:
        글 = input("내용을 입력하세요.")
        if 글 == '':
            글 = '\n'
        elif 글 == 'end':
            break
        파일.write(글 + '\n')
    
    파일.close()
    
메모장글쓰기( 메모장생성() )