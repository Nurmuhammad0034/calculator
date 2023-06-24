# while True:
#     try:
#         num1 = int(input("Enter a first number: "))
#         num2 = int(input("Enter a second number: "))
#         amal = input("Enter an operation (+-*/) or q for quit: ")

#         if amal == '+':
#             print(f"{num1}+{num2}={num1+num2}")
#         elif amal == '-':
#             print(f"{num1}-{num2}={num1-num2}")
#         elif amal == '*':
#             print(f"{num1}*{num2}={num1*num2}")
#         elif amal == '/':
#             print(f"{num1}/{num2}={num1/num2}")
#         elif amal == 'q':
#             break
#         else:
#             print("Operator noto'g'ri kiritildi.")

#     except ZeroDivisionError:
#         print("Nolga bo'lish mumkin emas!")
#     except ValueError:
#         print("Son kiritilmadi!")
#     except:
#         print("Dasturda xatolik mavjud")
#     else:
#         print("Keyingi sonlarni kiriting.")
#     finally:
#         print("Good bye. Dasturdan foydalanganingiz uchun rahmat :D")