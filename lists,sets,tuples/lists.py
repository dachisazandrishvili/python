#           0          1      2
courses = ["python", "java" ,"#c"]
# დაპრინტავს ყველაფერს 1 ინდექსიდან ბოლომდე
print(courses[1::])
# დაპრინტავს ყველაპერს 0 ინდექსიდან 2 ინდექსამდე
print(courses[0:2])
# სიის ბოლოში ჩაამატებს c++ ს
courses.append("c++")
# insert ჩაამატებს სიაში მოცემულ ინდექსზე
courses.insert(0,"JavaScript")
# print(courses)
#            0        1
courses_2 = ["html", "css"]
# extend ერთ სიაში ჩაამატებს მეორე სიის ინდექსებს insert ან append ის შემთხვევაში ჩაამატებდა მთლიან სიას სიაში, ამიტომ ასეთ დროს ჯობია extend გამოვიყენოთ
courses.extend(courses_2)
# remove წაშლის ჩვენს მიერ მითითებულ მონაცემს
courses.remove("java")
# pop იც remove ის ფუნქციას ასრულებს ოღონდ ის ბოლო ინდექსს აგდებს სიიდან
courses.pop()
#       0  1  2  3
nums = [1, 2, 3, 4]
# sort სტრინგებს ანბანის, ხოლო რიცხვეს ზრდის მიხედვით ალაგებს
courses.sort()
nums.sort()
# ასეთ შემთხვევაში ჯერ sort იმუშავებს, ხოლო შემდგომ შემობრუნდება და sortის საწინააღმდეგო რამ მოხდება(   თავად დატესტეთ;)  )
courses.sort(reverse=True)
nums.sort(reverse=True)
# ფუნქცია sorted ს არ შეაქვს ცვლილება მოცემულ ლისტში ჩვენ შეგვიძლია ცვლადში შევინახოთ ახალი მონაცემი და იქიდან დავპრინტოთ
sorted = sorted(courses)
print(sorted)
# min ფუნქცია ამოიღებს მინიმუმს რიცხვთა სიიდან
min(nums)
# იღებს ყველაზე დიდ რიცხვს რიცხვთა სიიდან
max(nums)
# ითვლის ჯამს რიცხვთა სიიდან
sum(nums)
# index გაიგებს რომელ ადგილზეა მოცემული ელემენტი სიაში
courses.index("html")
# join გადააქცევს listს სტრინგად(თავად გატესტეთ)
course_str = ", ".join(courses)
print(course_str)
# split ფუნქცია გადააქცევს სტრინგს listად
course_lst = course_str.split()
print(course_lst)

st = set(courses)
print(st)