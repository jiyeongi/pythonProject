# # """
# #
# # print ("hello world!")
# #
# # print(1+5)
# # print(1*5)
# # print(5/2)
# # print(5%2)
# #
# # professor= "Jiyeong Jeong"
# # print (professor)
# #
# # a= 7
# # b=5
# # print(a+b)
# # print("a+b")
# #
# # # 주석처리
# #
# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a%b)
# # # ctrl d 코드붙여넣기
# #
# # a=1
# # b=2
# # print(a,b)
# #
# # a=1.5
# # b=3.5
# # print(a,b)
# #
# # a="ABC"
# # b="101010"
# # print(a,b)
# #
# # a=True
# # b=False
# # print(a,b)
# #
# # print(type(a),type(b))
# #
# # print (3**5) # 제곱으로 계산
# # print(7//2) # 정수형으로 몫만 계산
# # print(7/2) #자동으로 실수형으로 계산
# #
# # a=1
# # a= a+1
# # print (a)
# #
# # a+=1
# # # 헷갈리는것 증가연산
# #
# # b=1
# # b=b-1
# # print(b)
# # b-=1 # 감소연산
# # print(b)
# #
# # """
# # #
# # # a=input ()
# # # print(a)
# # # # 시스템 인터페이스 파이선스크립트 CLI
# # # a=input()
# # # print(a)
# # # print(type(a))
# #
# # #스트링타입으로 출력한다
# #
# # #a=input()
# # #b=input()
# # #print(int(a)+int(b)) # int를 써서 정수형으로
# #
# # # a=input()
# # # b=input()
# # # num1=int(a)
# # # num2=int(b)
# # # print (num1+num2)
# # # # int 정수형만 출력한다 문자열은 에러
# #
# # """
# # celsius=input("섭씨온도를 입력하세요"))
# # fahrenheit=((9/5)celsius)+32
# # print("섭씨온도:", celsius, "화씨온도:", fahrenheit)
# # """
# #
# # # '' 문자 "" 문장
# #
# # #a=572
# # #print(type(a))
# #
# # # print ("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
# # # print ("변환하고 싶은 섭씨온도를 입력하세요.")
# # #
# # # celsius = input()
# # # fahrenheit =(float(celsius)*1.8)+32  #실수형으로 변환 함수를 써준다 float
# # # print ("섭씨온도:",celsius)
# # # print ("화씨온도:",fahrenheit)
# #
# #
# #
# # # celsius = input()
# # # fahrenheit =(celsius*1.8)+32  #실수형으로 변환 함수를 써준다 float
# # # print ("섭씨온도:",celsius)
# # # print ("화씨온도:",fahrenheit)
# # #
# # # print(f"사용자가 입력한 섭씨온도 : {celsius}입니다")
# # # # print(f"사용자가 입력한 화씨온도 : {fahrenheit}입니다")
# #
# # # 한번에 주석처리하기 ctrl /
# #
# # # colors = ['red','blue','green']
# # # print (colors [0])
# # # print (colors [2])
# # # print (len(colors))
# #
# # # cities=['서울','부산','인천','대구','대전','광주','울산','수원']
# # # print(cities[0:6])
# # #
# # # cities[0:5]
# # #
# # # cities[5:]
# #
# # # color1=['red','blue','green']
# # # color2=['orange','black','white']
# # # print (color1+color2)
# # # print (len(color1))
# # #
# # # total_color=color1+color2
# # #
# # # print('blue'in color2)
# #
# # # color =['red','blue','green']
# # # color.append ('white')
# # # print (color)
# #
# # # color =['red','blue','green']
# # # color. extend(['black','purple'])
# # # print (color)
# #
# # # color =['red','blue','green']
# # # color.insert(0,'orange')
# # # print (color)
# #
# # # color =['red','blue','green']
# # # color .remove ('red')
# # # print(color)
# #
# # # t=[1,2,3]
# # # a,b,c=t
# # # print (t,a,b,c)
# # #
# # # a_list=[1,2,3]
# # # b_list=[4,5,6]
# # # c_list=[a_list,b_list]
# # #
# # # print (c_list)
# # # print (c_list[1][0])
# #
# # # print("I eat %d apples"%3)
# # # print("I eat %s apples"%"five")
# # # number=3
# # # print("I eat %d apples"%number)
# # # print("I eat %0.2f apples"%1.321441)  #소수점 자리수지점
# # #
# # # print ("%10s"% "hi")   # 공백주기
# # # # print ("%-10sjane"%"hi")
# # #
# # # kor_score=[49,79,20,100,80]
# # # math_score=[43,59,85,30,90]
# # # eng_score=[49,79,48,60,100]
# # # midterm_score=[kor_score,math_score,eng_score]
# # # print(midterm_score)
# # #
# # # math_score[0]=1000
# # # print(math_score)
# # # print(midterm_score)
# # # print (midterm_score[1][2])
# # # a=300
# # # b=300
# # # print (a is b)
# # #
# # # print (a==b)
# #
# # score1=["김연화",85,70,82]
# # score2=["이태진",85,75,95]
# # score3=["전승훈",85,90,80]
# # score4=["정다진",85,90,80]
# # score5=["황윤정",85,90,80
# #
# #2023/02/06
#
#
# # print("Tell me your age?")
# # myage=int(input())
# # if myage<30:
# #     print("Welcome to the club")
# # else:
# #     print("oh!no.you are not accepted.")
# # 홀짝비교
# # print("숫자를입력해주세요")
# # num=int(input())
# # if num %2==0 :  #2로나눈나머지가 0이다
# #     print("짝수입니다")
# # else :
# #     print("홀수입니다")
# #
# #두시비교
# # print("1번째숫자를 입력해주세요")
# # num=int(input())
# # print ("2번째숫자를 입력해주세요")
# # num1=int(input())
# # if num >  num1 :
# #     print("더큰수는%d입니다"%num)
# # else :
# #     print("더큰수는%d입니다"%num1)
#
# #목욕탕요금
# # 7세이하는 어린이요금 5000 7세이상은 성인요금7000 65세이상은 어르신요금6000
#
# #  userinput=input("나이를입력해주세요")
# #  age=int(userinput)
# # payment =0
# #
# # if age > 7:
# #     payment = 5000
# # elif age < 60: payment = 7000
# # elif payment = 6000
# #
# # print (f"요금은 {payment}원 입니다 ")
#
# #영어점수결과
# #영어점수를 입력받는다
# #영어점수가 60점이하면 혼남
# #70점 이하면 아무일도 없다
# #80점 이상 용돈10만원
# #90점이상이면 노트북
#
# # print("영어점수를입력하세요")
# # engscore=int(input("영어점수를 입력하세요"))
# #
# # if engscore >= 90 : grade = '노트북'
# # elif engscore >= 80  : grade ='용돈10만원'
# # elif engscore >= 70 : grade = '좀더노력하자'
# # elif engscore <=60 : grade = '혼나야겠다'
# # print (grade)
#
# # #세수를 비교하기
# # print ("1번째숫자를 입력하세요 ")
# # num1=int(input("1번째숫자입력"))
# # print ("2번째 숫자를 입력하세요")
# # num2=int(input("2번째숫자입력"))
# # print("3번째 숫자를 입력하세요")
# # num3=int(input("3번째숫자입력"))
# # num4 = 0
# # if num1 > num2:
# #     num4=num1
# # else :
# #     num4=num2
# # if num4>num3 :
# #     pass
# # else :
# #     num4 =num3
# # print ( "가장큰수는%d입니다"%num4)
# #
# # print ("당신이 태어난 연도를 입력하세요")
# # year=int(input ())
# # age =2020-int(year)+1
# #
# # if age <= 26 and age>=20 :
# #     print("대학생")
# #
# # elif age <20  and age >= 17:
# #     print ("고등학생")
# #
# # elif age<17 and age >= 14 :
# #     print ("중학생")
# #
# # elif age<14 and age>= 8 :
# #     print ("초등학생")
# #
# # else :
# #     print ("학생이아닙니다")
# #
# # print ("주민번호 숫자만13자리를 입력해주세요")
# # num= input (str("주민번호13자리숫자만입력"))
# # age = 0
# # gender = 0
# # if num[6]=='1'or num[6]='3' :
# #
# #
# # elif num[6] =='2' or num[6] = '4' :
# #
# #
# # else :
# # print ('확인할수없습니다')
# #
# #
# #
# # print ("주민번호 숫자만7자리를 입력해주세요")
# # num= input (str("주민번호뒤7자리숫자만입력"))
# # age = 0
# # gender = 0
# #
# # if num [6]=='3' or num[6]=='4' :
# # year = '20'+ num[0:2]
# # elif : year=='19' = num[0:2]:
# # age =2023-int(year)
#
#
# #반복문
# #while
#
# # treehit=0
# #
# # while treehit <10:
# #     treehit+=1
# #     print (f"나무를 {treehit}찍었습니다")
# #     if treehit == 10 :
# #         print("나무가쓰러집니다")
#         #순차적으로 1부터 10까지 출력되고 10이후는 나무가 쓰러집니다가 출력된다
#
# # num=0
# # promt="""
# # while num ! = 4:
#
# #숫자범위를 지정해서 반복하는 for문
# # for i in range(1,10):
# #     print (i)
# #
# # #list같은 순서가 있는 자료구조에서 요소를 꺼내면서 반복
# #
# # num_list =[1,3,5,7,9,]
# #
# # for num in num_list :
# #     print (num)
#
# #
# # num_list = [1, 3, 5, 7, 9]
# # kor_score = [49, 70, 20, 100, 80]
# # math_score = [43, 59, 85, 30, 90]
# # eng_score = [49, 79, 48, 60, 100]
# # # for num in num_list:
# # #     print(num)
# # score_sum = 0
# # count = 0
# # for score in kor_score:
# #     score_sum += score
# #     print(score_sum)
# #     count += 1
# #
# # print(f"길이{len(kor_score)}")
# # print(score_sum, count, score_sum/count)
#
# # for i in range(1,10):
# #     #print (i, end = '')
# #     print (f"2x{i} = {2*1}",end ='')
#
# # print ("구구단 몇단을 해볼까")
# # uinput = input ()
# # print ("구구단",user_input,"단을 계산한다")
# # sum=0
# # for i in range(1,100):
# #     if i % 2 == 0:
# #     sum += i
# #
# # print (sum)
#
#
# #반복문 제어해주기 break
#
# # i=0
# # while i < 10 :
# #     if i == 5:
# #         break
# #         print (i)
# #     i+=1
#
# student_list=['연화','남호','민지','상호','소연']
# count =0
# # for student in student_list :
# #     if student == '민지':
# #         print (f"찾았다!{student},{count}")
# #         break
# #     count += 1
#
#     for student in student_list :
#         if student == '소연':
#         print (f"찾았다!{student}")
#         break
#     else:
#         print ("소연이는없다")
#
#
# import random
#
# g_number=random.randint(1,100)
# print ("1~100중에 숫자를 맞춰보세요")
# u_input=int(input())
# while (u_input is not g_number ) :
#     if u_input > g_number :
#         print ("숫자가 큽니다 ")
#     else :
#         print ("숫자가 너무 작습니다")
#     u_input =int(input ())
# else :
#     print ("정답입니다","입력한숫자는",u_input,"입니다")
#
# for i in range(2,10):
#     for j in range(1,10):
#         print ( f" {i }*{j}={i*j}",end ='')
#     print()
#
#
#
# student_list = [['연화', '남호', '민지', '상훈', '소연'],
#                 ['수민', '수성', '영호', '재현', '준영'],
# #
#  for students in student_list:
#     for student in students:
#         print(student)
#
#
# kor_score = [49,80,20,100,80]
# math_score=[43,60,85,30,90]
# eng_score=[49,79,48,60,100]
# midterm_score=[kor_score,math_score,eng_score]
#
# student_score=[0,0,0,0,0]
# i=0
#
# for subject in midterm_score :
#     for score in subject :
#         student_score [i]+=score
#         i+=1
#     i=0
# else:
#     a,b,c,d,e=student_score
#     student_avg=[round(a/3,1),round(b/3,1),round(c/3,1),round(d/3,1),round(e/3,1)]
#     print(student_avg)
#
# for a in range(8):
#     a *=(a-1)
# print (a)
#
# test = '5'
# for n in range (int(test)):
#     print ('test')
#
# a=1
# while a<11:
#     if a %2 == 0:
#         print (a)
#         a+=1
#     else:
#         a+=1
#     if a == 0:
#         break
#
# num=[1,2,3,4,5,6]
# total = 0
# for n in num :
#     total *=n-1
#
# print (total)
#
# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end='')
#     print()  # * ** *** **** *****
#
# for i in range(1,6):
#     for j in range(1,7 -i):
#         print ('*',end='')
#     print()
#
# for i in range(1,8):
#     for j in range(0,i:)
#     print ("*",end='')
#     print()
#
# for i in range(6) :
#     triangle=i
#     print(''*triangle,end='')
#     print('*'*(11-2*i))
#
# print (" "*4, "*"*1 )
# print (" "*3, "*"*3 )
# print (" "*2, "*"*5 )
# print (" "*1, "*"*7 )
#
# 20230207 화요일 165 함수기초
#
# def somthingDo (num1,num2) :
#     #코드
#     return num1+ num2
#
# def calculate_rectangle_area(x,y):
#     return x*y
# rectangle_x=10
#
# rectangle_y=20
# print (f"사각형 x의길이 : " ,rectangle_x)
# print (f"사각형 y의길이 : {rectangle_y}")
#
# result = calculate_rectangle(rectagle_x,rectangle_y)
# print(f"사각형의 넓이는 {resulf}입니다.")
#
# def a_rectangle_area():
#     print (5*7)
# def b_rectangle_area(x,y):
#     print(x*y)
# def c_rectangle_area():
#     return (5*7)
# def d_rectangle_area(x,y):
#     return(x*y)
#
# a_rectangle_area()
# b_rectangle_area(5,7)
# print (c_rectangle_area())
# print (d_rectangle_area(5,7))  # 모두다 값이 35가 나온다
#
# 성적표출력하기 과제 함수화 list 합과 평균을 return 하는 함수사용
# 길이는 len사용
# ascore = [85,80,90,95]
# bscore=[85,70,50,90]
# cscore=[70,50,60,80]
#
#
# def sumlist(collection) :
#     result = 0
#     for i in collection :
#         if type (i) in not int :
#             return print ("숫자가 아닌 요소")
#         result += i
#     else :
#         return result
#
#
# def avglist(collection):
#     return sumlist (collection)/len (collection)
#
# def f(x):
#     y=x
#     x=5
#     return y*y
# x=3
# print (f(x)) # 9출력
# print (x) # 3출력
#
#
# def spam(eggs):
#     eggs.append(1) #항목마지막1을추가
#     eggs=[2,3]
# ham=[0]
# spam(ham)
# print(ham)  #0,1이출력된다
#
#
# 변수의 사용범위
#
# def test(t) :
#     print (x)
#     t=20
#     print ("In Function",t)
# x=10
# test(x)
# print("In Main :",x)
# print("In Main :",t)  # 호출하지못한다
#
# def f() :
#     s= "I love Londen !"
#     print(s)
#
# s= "I love paris!"
# f()
# print (s)
#
# # I love Londen  변수가 같은 메모리 주소를 갖기위해서는
# # global 키워드를 사용한다
# def f() :
#     global s
#     s= "I love Londen !"
#     print(s)
#
# s= "I love paris!"
# f()
# print (s)
#
# def globlssum():
#     global num
#     num += 1
#     print (num)
#
# num=0
# globlssum()
# globlssum()
# globlssum() # 증가하여 1,2,3 출력
#
# def calculate(x,y):
#     total = x + y
#     print ("In function")
#     print ("a",str(a),"b:",str(b),"a+b",str(a+b),"total:",str(total))
#     return total
#
# a=5
# b=7
# total=0
# print (f'inprogram-1')
# print (f"a:{a},b:{b},a+b:{a+b},total:{total}")
#
# def factorial (n):
#     if n == 1 :
#         return 1
#     else :
#         return n * factorial(n-1)
# print(factorial(int(input("Input Number for Factorial Clculation:"))))
#
# def print_something(my_name,your_name):
#     print("Hello {0},My name is {1}.".format(your_name,my_name))
#
# print_something("sungchul"," teamlab")
# print_something(your_name="teamlab",my_name="sungchul")
#
# def asterisk_test(a,b,*args):
#     return a+b+sum(args)
# print(asterisk_test(1,2,3,4,5))
#
# def asterisk_test(a,b,*args):
#     print (args)
# print(asterisk_test(1,2,3,4,5)) # 실행되지않는다.
#
# def asterisk_test_2(*args):
#     x,y,*z=args
#     return x,y,z
# print(asterisk_test_2(3,4,5))
#
# def print_hello():
#     print("안녕")
#     print("Hi")
#
# a= 8
# if (a>3) :
#     print_hello()
# if (a>4) :
#     print_hello()
# if (a>5) :
#     print_hello()
# if (a>6) :
#     print_hello()
# if (a>7) :
#     print_hello()
# if (a>8) :
#     print_hello()
#
# def test(k):
#     print ("input is ",k)
# k=100
# test(k)
#
# def counter(*args):
#     count=len(args)
#     return count
# print (counter(["1","2","3"]))
#
# def f(x):
#     y=7
#     return y*x
#
# x=4
# print(f(3))
# print(x)
#
# f=open("yesterday.txt",'r')
# yesterday_lyric=f.readlines()
# f.close()
#
# contents=""
# for line in yesterday_lyric:
#     contents=contents+line.strip()+"\n"
#
# n_of_yesterday=contents.lower().count("yesterday")
# print("number of a word 'yesterday'",n_of_yesterday)
#
# print(ord('a')) #아스키코드 97
# print(ord('A')) #아스키코드 65
#
# print(chr(ord('a')-32))  #변환해주는 함수 A로 출력이된다 97-32=65
#
# def userupper(list_string,opt='U') :
#     contents = ""
#     optnum=0
#     if opt == 'U':
#         optnum=-32
#     elif opt== 'L':
#         optnum== 32
#
#     for char in list_string:
#         contents+=chr(ord(char)+optnum)
#     else:
# #         return contents
# #
# result=userupper("abcdefhoogk",'U')
# print(result)
#
#
# create_dic={}
# country-code={"America":1,"korea":2 }
# print(county_code['America'])
#
#
# #김밥헤븐pos프로그램만들기
# """
# 변수이름은 다 영어로
# 되도록 함수를 사용할것
# 1)주문의 총합과 내역에대한 내용이 최종결과에 출력될것
# 2)총합을 출력한후 할인내역이 따로 적용하여 출력 할것
# 3)프로그램 종료직전까지의 매출의 총합을 조회시 출력할것
# 4)주문할때 포장(전체금액 10% 할인 )/매장식사/배달(배달료8900원) 선택
# 세트
# 2개 시키면 20% 할인
# 3개시키면 25% 할인
# 4개 시키면 30%할인
# """
#
# price_gimbap={"김밥":2500,"참치김밥":3000,"돈가스김밥":3500,"고추참치김밥":3500,
#               "소고기김밥":4500,"치즈김밥":3000,"샐러드김밥":2500,"꼬마김밥":1200,
#               "충무김밥":20000,"꽈리김밥":3500,"진미김밥":3700}
#
# price_noodle={"라면":4000,"치즈라면":4500,"된장라면":4700,"떡라면":4800,
#               "만두라면":4500,"떡만두라면":5000,"카레라면":4500,"해물라면":5500
#               "짜장라면":4200,"비빔라면":4200}
#
# price_steak={"돈가스":8000,"치즈돈가스":9000,"등심돈가스":7500,"안심돈가스":7500,
#              "피카츄돈가스":500,"새우돈가스":7500,"대왕돈가스":12000,
#              "치킨돈가스":6000,"함박스테이크":9500}
#
# price_rice={"제육덮밥":7000,"오무라이스":7000,"하이라이스":7000,"오징어덮밥":7500,
#             "짜장덮밥":6500,"소고기덮밥":8000,"카레덮밥":6500,"돌솦비빔밥":7000,
#             "김치덮밥":6500}
#
# price_stew={"김치찌개":6500,"된장찌개":6500,"순두부찌개":6500,"내장찌개":6500,
#            "해물된장찌개":8500,"부대찌개":7800 }
#
# price_tteok={"떡볶이":3000,"치즈떡볶이":4500,"라볶이":5000,"마약떡볶이":9900,
#              "컵떡볶이":500}
#
# price_udon={"우동":3000,"튀김우동":4500,"김치우동":4500,"유부우동":4500}
#
# price_soup={"육개장":6000,"알탕":7500,"갈비탕":8000,"황태해장국":7000,
#             "순대국밥":5500,"명태국밥":7000,"공기밥":1000}
# menudic=[price_gimbap,price_noodle,price_steak,price_rice,price_stew,
#       price_tteok,price_udon,price_soup]
# menulist=['김밥류','라면류','돈가스류','덮밥류','찌개류','떡볶이','우동류','국물류]
#
# bill = 0
# menu={}
# order=[] # 주문내역
# table_no="" # 테이블번호
# foodlist='음식'
# allmenu='음식류'
#
# while(1):
#     flag=false
#     for i in menulist : print (f'[{i}]')
#     print ('')
#     foodlist=input('메뉴의 이름을 입력해주세요:')
#
#     for i in menulist :
#         if (i==foodlist):
#             print(f'\n<{i}>')
#             menu=menulist
#
#
#
#
#
#
#
