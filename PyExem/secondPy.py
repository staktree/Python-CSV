import os
import csv
from googletrans import Translator

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

# TODO : 타겟 언어 설정
lang_list = ["ko", "en", "ja", "zh-CN", "zh-TW", "fr", "vi", "th"]

def file_update_process(file):
  text_list = []
  adding_lang = []
  exist_lang = []
  translated_list = []
  translating_data = []

  if not file.endswith('.csv'):
    return

  print("Processing " + file)

  # TODO : encoding 형식 설정
  with open(file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    text_list = list(reader)

  text_list = list(map(list, zip(*text_list)))

  for row in text_list:
    exist_lang.append(row[0])

  # 원본 언어 설정
  if 'en' in exist_lang:
      translating_data = [row for row in text_list if row[0] == 'en']
  else:
      translating_data = [row for row in text_list if row[0] == 'ko']

  print(translating_data)

  #adding_lang = [lang for lang in lang_list if lang not in exist_lang]
  adding_lang = lang_list;

  for lang in adding_lang:
    translated_data = []
    translated_data.append(lang)
    if len(translating_data) == 0:
      continue
    for text in translating_data[0][1:]:
      translated_data.extend([translate_to_otherLang(text, lang)])
    translated_list.append(translated_data)


  translated_list = list(map(list, zip(*translated_list)))
  print(translated_list)

  # 파일 초기화
  if len(translated_list) == 0 : return;
  print("Delete File Data")
  delete_file_data(file)

  # TODO : encoding 형식 설정
  # 파일 쓰기
  print("Write Data")
  for translated_data in translated_list:
    with open(file, 'a', newline='', encoding='utf-8-sig') as f:
      writer = csv.writer(f)
      writer.writerow(translated_data)

def delete_file_data(file):
  with open(file, 'w', encoding='utf-8-sig') as f:
    f.truncate(0)

def translate_to_otherLang(text, target_lang):
  return Translator().translate(text, dest=target_lang).text


def translate_to_allLang(file_list):
   for file in file_list:
     file_update_process(file)

# 실행
print("Translate")
file_path = "C:/Users/TAK/Desktop/123"
file_list = get_folder_names(file_path)
print_list(file_list)
translate_to_allLang(file_list)