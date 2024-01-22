# mylist = [2, 7, 3, 9, 5, 7]
# mytuple = (2, 7, 3, 9, 5, 7)
# droids = ["C3PO", "R2D2", "BB8", "K2SO"]

# num_items = len(droids)
# print(num_items)

# print(droids[1])
# print(droids)


# printing list without i in range
# for item in droids:
#    print(item)

# printing list using for loop using for i in range
# for i in range(3):
#    print(droids[i])

# for i in range(len(droids)):
#    print(droids[i])

# list = [2, 5, 8, 4, 9, 5]
# for i in range(len(list)):
#    print(list[i]**2)

# newlist = [[1, 2], [3, 4], [5, 6]]
# print(newlist[2][0])

# print(len(list))
# list.append(8)
# print(list)


# a_new_list = []
# for i in range(5):
#    num = int(input("enter a number: "))
#    a_new_list.append(num)
# print(a_new_list)

# total = 0
# for num in a_new_list:
#    total += num
# avg = total/len(a_new_list)
# print(avg)

# list = [2, 5, 8, 4, 9, 5]
# list[3] = 7
# print(list)

list = [2, 4, 8, 4, 9, 4]
for i in range(len(list)):
    if list[i] == 4:
        list[i] = 7
print(list)

# uhs_slogan = "My school is the best"
# print(len(uhs_slogan))
# print(uhs_slogan[13:])
# words = 1
# for letter in uhs_slogan:
#    if letter == " ":
#        words += 1
# print(words)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

# words = 1
# for letter in months:
#    if letter == " ":
#        words += 1
# y = int(input("enter a number 1-12: "))
# month = [y*3-3] and [y*3]
# print(month)
# score = 41237
# highscore = 1023407
# print(f"Score = {score:13,}")
# print(f"highscore = {highscore:9,}")


# for i in range(5):
#   num = int(input("enter a number: "))
#    a_new_list.append(num)
#
# print(a_new_list)
# total = 0
#    total += num
# avg = total/len(a_new_list)
# print(avg)

# mail = (input("enter your email"))
# charnum = 0
# for letter in mail:
#    if letter == "@":
#        break
#    else:
#        charnum+=1
# print(email[:charnum])

# total = 0
# a_list = [3, 12, 3, 5, 3, 4, 6, 8, 5, 3, 5, 6, 3, 2, 4]
# b_list = [4, 15, 2, 7, 8, 3, 1, 10, 9]
# c_list = [5, 10, 13, 12, 5, 9, 2, 6, 1, 8, 8, 9, 11, 13, 14, 8, 2, 2, 6, 3, 9, 8, 10]
# question = input("Enter a list a through b: ")
# if question == "A":
#    for num in a_list:
#        total += num
#    avg = total/len(a_list)
#    print(avg)
# if question == "B":
#    for num in b_list:
#        total += num
#    avg = total/len(b_list)
#    print(avg)
# if question == "C":
#    for num in c_list:
#        total += num
#    avg = total/len(c_list)
#    print(avg)