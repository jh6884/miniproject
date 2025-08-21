import os

def replace_and_overwrite(filename, new_char):
    """
    파일의 모든 행의 첫 글자를 새로운 글자로 바꾸어 원본 파일에 덮어씁니다.
    """
    temp_filename = filename + '.tmp'
    try:
        with open(filename, 'r', encoding='utf-8') as infile, \
             open(temp_filename, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                new_line = new_char + line.strip()[1:] + '\n'
                outfile.write(new_line)
        
        # 원본 파일을 삭제하고 임시 파일의 이름을 바꿉니다.
        os.remove(filename)
        os.rename(temp_filename, filename)
        print(f"파일 '{filename}'이 성공적으로 수정되었습니다.")
    except FileNotFoundError:
        print("오류: 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"처리 중 오류 발생: {e}")
        
paths = '../../data/Car-model.v1i.yolov11/train/labels/'
lst = os.listdir(paths)
for file in lst:
    filename = os.path.join(paths+file)
    replace_and_overwrite(filename, '5')