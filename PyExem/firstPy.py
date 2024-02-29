import os
import csv
#from googletrans import Translator

### 모든 파일 가져오기
def get_folder_names(file_path):
  file_list = []
  if not check_folder_exists(file_path):
    return

  for root, dirs, files in os.walk(file_path):
    for file_name in files:
      file_list.append(os.path.join(root, file_name))
  return file_list

def check_folder_exists(folder_path):
  if os.path.exists(folder_path):
    print("Folder exists.")
    return True
  else:
    print("Folder does not exist.")
    return False

def print_list(lst):
  if not lst: return
  for item in lst:
    print(item)
  print("----------------\n")

### 모든 파일 정보 수정하기
lang_list = ["KOR", "ENG", "JPN", "CHN"]

def file_update_process(file):
  text_list = []
  adding_lang = []
  exist_lang = []
  translated_list = []
  translating_data = []

  if not file.endswith('.csv'):
    return

  print("Processing " + file)

  with open(file, 'r', encoding='cp949') as f:
    reader = csv.reader(f)
    for row in reader:
      text_list.append(row)

    for row in text_list:
      exist_lang.append(row[0])

    if 'ENG' in exist_lang:
      translating_data = [row for row in text_list if row[0] == 'ENG']
    else:
      translating_data = [row for row in text_list if row[0] == 'KOR']

    adding_lang = [lang for lang in lang_list if lang not in exist_lang]

    for lang in adding_lang:
      translated_data = []
      translated_data.append(lang)
      for text in translating_data[0][1:]:
        translated_data.extend([translate_to_otherLang(text, lang)])
      translated_list.append(translated_data)

    for translated_data in translated_list:
       with open(file, 'a', newline='', encoding='cp949') as f:
         writer = csv.writer(f)
         writer.writerow(translated_data)

def translate_to_otherLang(text, target_lang):
  #return Translator().translate(text, dest=target_lang).text
  return text


def translate_to_allLang(file_list):
  for file in file_list:
    file_update_process(file)


# 실행
print("Hello Coding")
file_path = 'C:/Users/86168/Desktop/DataTest' #'C:\Users\86168\Desktop\DataTest'
file_list = list = get_folder_names(file_path)
print_list(file_list)
translate_to_allLang(file_list)
