import os

base=input()

"""ef listAll(path):
    dirfiles= os.listdir(path)
    subdirs = [path+"/"+x for x in dirfiles if os.path.isdir(path+"/"+x)]
    #print(path)
    for subdir in subdirs:
        listAll(subdir)
listAll(base)"""

def listAll_scan(path):
    with os.scandir(path) as entries: #뭔가 정보로 들어오는듯
        for entry in entries: 
            if entry.is_file(): #만약 파일이면
                if entry.name.endswith(".txt"): #이름 확인
                    print(entry.name)
            elif entry.is_dir(): #만약 디렉토리면 
                    listAll_scan(entry) #엔트리 자체가 디렉토리를 가리킴, 그 디렉토리로 들어간다.
                    #어차피 다 (all entry in entries) < all files and dirs 
                    # 돌기 때문에 subdir의 주소를 만들어서 갈 필요가 없다 for문이 바깥에 있는 형태
listAll_scan(base)