#1
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)

#2
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})

#3
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)

#4 키값, 밸류값 순서 주의
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

#6  대소문자 구문 주의
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])

#7
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])

#8 zip 확실한 이해 필요
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2' ,'b3']
for a, b in zip(alist, blist):
    print(a, b)

#9 3개 모두가 성립이 되어야 함
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])

#
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])