import os


def get_all_files(base_path):
    # 모든 파일 찾아 "상대경로"key - 크기,절대경로 val
    file_dict = {}  # for files

    def scan_directory(current_path):  # 내부에서 재귀적으로 탐색할 함수임
        with os.scandir(current_path) as entries:
            # with문은 안전하게 닫아준다
            for entry in entries:
                if entry.is_file():
                    file_stat = os.stat(entry.path)
                    # 상태정보 가져오기
                    file_size = file_stat.st_size
                    # 사이즈 가져오기 - byte크기

                    relative_path = os.path.relpath(entry.path, base_path)
                    # entry.path는 절대경로를 포함하기 때문에
                    # relpath로 사애경로를 가져온다

                    # rb는 바이트 그대로 읽어노다
                    with open(entry.path, "rb") as f:
                        file_content = f.read()
                    # 변수에 바이트 형태로 저장

                    file_dict[relative_path] = (file_size, file_content)

                elif entry.is_dir():
                    scan_directory(entry.path)

    scan_directory(base_path)
    return file_dict


dirA = input("dir A: ").strip()
dirB = input("dir B: ").strip()

dirA_files = get_all_files(dirA)
dirB_files = get_all_files(dirB)

is_identical = True

print("\n ,.+:-*+-,.+ Result +.,-+*-:+., ")
if len(dirA_files) != len(dirB_files):
    print(
        f" 결과 : 두 디렉토리의 파일 수가 다릅니다. \n [A: {len(dirA_files)}개] [B: {len(dirB_files)}개]"
    )
    is_identical = False
else:
    # 💡 이 아래 구역의 들여쓰기를 else 레벨에 맞게 한 단계(공백 4칸) 들여쓰도록 수정했습니다.
    for file_name in dirA_files:  # 여기까지 왔으면 파일 수는 같다는 소리
        if file_name not in dirB_files:
            print(f"불일치: {file_name} 파일이 dirB에 존재하지 않습니다.")
            is_identical = False
            break

        sizeA, contentA = dirA_files[file_name]
        sizeB, contentB = dirB_files[file_name]

        if sizeA != sizeB:
            print(
                f"불일치: '{file_name}' 파일의 크기가 다릅니다. (A: {sizeA} bytes, B: {sizeB} bytes)"
            )
            is_identical = False
            break
        if contentA != contentB:
            print(f"불일치: '{file_name}' 파일의 내용이 서로 다릅니다.")
            is_identical = False
            break

if is_identical:
    print(
        "결과: 두 디렉토리의 파일 수가 같고, 모든 파일의 이름, 크기, 내용이 완전히 일치합니다!"
    )