# ch5_9.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
BMI = weight / (height / 100) ** 2 
if BMI >= 18.5 and BMI < 24:
    print(f"{BMI = :5.2f}體重正常")
else:
    print(f"{BMI = :5.2f}體重不正常")







