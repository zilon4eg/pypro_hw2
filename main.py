import re
import csv
from pprint import pprint


def phone(phone):
  pattern_phone = r'(\+7|8)\s*\(?(\d{0,3})\)?(\s|-)?(\d{0,3})-?(\d{0,2})-?(\d{0,2})\s*\(?д?о?б?\.?\s*(\d+)?\)?'
  subst = r'+7(\2)\4-\5-\6 (доб.\7)'
  result = re.sub(pattern_phone, subst, phone)
  result = result.split()
  if len(result) == 2:
    if result[1] == '(доб.)':
      result.remove('(доб.)')
  result = ' '.join(result)
  return result


def name(contact):
  contact_list = []
  for counter, item in enumerate(contact, 1):
    if counter > 3:
      break
    item_list = item.split(' ')
    for i in item_list:
      contact_list.append(i)
    if '' in contact_list and len(contact_list) > 3:
      contact_list.remove('')
  return contact_list


def corrected_contact(contact):
  result_list = []
  for counter, item in enumerate(contact):
    if counter < 3:
      result_list.append(name(contact)[counter])
    elif counter == 5:
      result_list.append(phone(item))
    else:
      result_list.append(item)
  return result_list


def merge(contacts_list):
  for list1 in contacts_list:
    for list2 in contacts_list:
      if list1 != list2:
        if list1[0] == list2[0] and list1[1] == list2[1]:
          for index in range(len(list1)):
            if list1[index] == '':
              list1[index] = list2[index]
          contacts_list.remove(list2)
  return contacts_list


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO_1: выполните пункты 1-3 ДЗ
# Структура данных: lastname,firstname,surname,organization,position,phone,email
result_contacts_list = []
for contact in contacts_list:
  result_contacts_list.append(corrected_contact(contact))
result_contacts_list = merge(result_contacts_list)

# TODO_2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result_contacts_list)