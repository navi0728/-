import pandas as pd
import random
df = pd.read_excel("hiil.xlsx")
df.columns=['type','name','etc','cal']

type1=df['type'].tolist()
name1=df['name'].tolist()
cal1=df['cal'].tolist()

type3 =[]
name3 =[]
cal3 =[]
type5 =[]
name5 =[]
cal5 =[]

for type1_list in type1:
    type2 = type1_list.replace(u'\xa0', u' ')
    type3.append(type2)

for name1_list in name1:
    name2 = name1_list.replace(u'\xa0', u' ')
    name3.append(name2)

for cal1_list in cal1:
    cal2 = str(cal1_list).replace(u'\xa0', u' ')
    cal3.append(cal2)

for type1_list in type3:
    type4= type1_list.replace(" ", "")
    type5.append(type4)
    
for name1_list in name3:
    name4= name1_list.replace(" ", "")
    name5.append(name4)

for cal1_list in cal3: 
    cal4 = cal1_list.replace(" ", "")
    cal5.append(cal4)

print("총 {}개의 음식 데이터를 불러왔습니다".format(len(type5)))

date_number = len(type5)
possible_types = []

for i in range(date_number):
    if type5[i] in possible_types:
        continue
    else:
        possible_types.append(type5[i])

while True:
    try:
        want_cal = int(input('원하는 한끼 칼로리를 입력하세요 (kcal):'))
        break
    except:
        print("잘못 입력하셨습니다.")

print("")
print('가능한 음식 종류는',','.join(possible_types))
print("입니다")
print("")

want_type = input("원하는 음식 종류를 입력하세요.(','로 구분하기):")
want_type_list = want_type.replace(" ","").split(",")
want_type_list_number = len(want_type_list)

name_combination_list = []
cal_combination_list = []

for i in range(want_type_list_number):
    name_buffer =[]
    cal_buffer =[]
    if want_type_list[i] in possible_types:

      for j in range(date_number):

        if type5[j] ==  want_type_list[i]:
          name_buffer.append(name5[j])
          cal_buffer.append(cal5[j])

      name_combination_list.append(name_buffer)
      cal_combination_list.append(cal_buffer)
        
    

    else:
        print("{}는 없는 종류 입니다.".format(want_type_list[i]))
        assert False

possible_number = []

for i in range(want_type_list_number):
    possible_number.append(len(cal_combination_list[i]))

final_name_dicison = []
final_cal_dicison = []


for i in range(1000):
    cal_sum = 0
    final_name_buffer = []
    final_cal_buffer = []

    for j in range(want_type_list_number):
        target_index = random.randint(0, possible_number[j]-1)

        cal_sum += int(cal_combination_list[j][target_index])
        
        final_name_buffer.append(name_combination_list[j][target_index])
        final_cal_buffer.append(cal_combination_list[j][target_index])

    if want_cal-10 <= cal_sum <= want_cal+10:
      final_name_dicison.append(final_name_buffer)
      final_cal_dicison.append(final_cal_buffer)
    
if len(final_name_dicison) == 0:
    print("가능한 조합을 찾지 못했습니다.")
    assert False

else:
    if len(final_name_dicison) >= 5:

      final_index = random.sample(range(0, len(final_name_dicison)),5)
    else:
      final_index = random.sample(range(0, len(final_name_dicison)),len(final_name_dicison))
      final_index = random.sample(range(0, len(final_name_dicison)),len(final_name_dicison))


    print("")
    print("추천 음식 조합은 다음과 같습니다.")

    for count,i in enumerate(final_index):
        print("-------{}번 조합--------".format(count +1))
        for j in range(want_type_list_number):
            print(final_name_dicison[i][j], final_cal_dicison[i][j], "kcal")

        print("------------------------")
        print("")
