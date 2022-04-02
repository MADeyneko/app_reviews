import selen

# import sqlite3
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import requests
# from selenium.webdriver.common.by import By
# import csv



# def pars_link():
#     reader_object = pup()


#     with open('bruh12.csv', 'w', encoding="UTF8") as fi:
#         file_writer = csv.writer(fi, delimiter="|", lineterminator="\r")

#         # file_writer.writerow(["title", "tipe", "data_question", "question", "answer", "date_answer", "link"])

#         for i in reader_object:
#             print(i)

#             options = Options()
#             options.add_argument('--headless')
#             options.add_argument('--disable-gpu')

#             driver = webdriver.Chrome(executable_path=r"/user/deyneko-ma/repo/app_reviews/chromedriver", options=options)
#             driver.get("https://www.banki.ru" + i[0])

#             title = driver.find_elements(By.CLASS_NAME, "l5474aaa7")
#             tipe = driver.find_elements(By.CLASS_NAME, "lf1f886e6")
#             data = driver.find_elements(By.ID, "faq-date-time-2")
#             question = driver.find_elements(By.CLASS_NAME, "OdPqK")
#             answer = driver.find_elements(By.CLASS_NAME, "dmfsla")
#             date_answer = driver.find_elements(By.CLASS_NAME, "MIkZT")
#             link = "https://www.banki.ru" + i[0]

#             try:
#                 file_writer.writerow(
#                     [title[0].text, tipe[0].text, data[0].text, question[0].text, answer[0].text, date_answer[0].text, link])
#                 print(title[0].text, tipe[0].text, data[0].text, question[0].text, answer[0].text, date_answer[0].text,
#                       link)
#             except:
#                 file_writer.writerow([title[0].text, tipe[0].text, data[0].text, question[0].text, "None", "None", link])
#                 print(title[0].text, tipe[0].text, data[0].text, question[0].text, "None", "None", link)
#             finally:
#                 continue


# def pup():
#     red = []
#     line_count = 0
#     with open('bruh.csv', 'r') as f:
#         reader_object = csv.reader(f, delimiter=",")

#         for i in reader_object:
#             if line_count == 1:
#                 red.append(i)
#             else:

#                 line_count += 1
#     return red
# # sel()
# pars_link()