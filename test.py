import smtplib
#smtp lib stands for system mail transfer protocol, basically a library that creates a system on a server sending emails
from email.message import EmailMessage
import csv

# rows1 = []
# with open("attendance.csv", 'r') as file1:
#
#     csvreader1 = csv.reader(file1)
#     header1 = next(csvreader1)
#     for row in csvreader1:
#         rows1.append(row)

# print(rows1)

# rows2 = []
# with open("student_list.csv", 'r') as file2:
#
#     csvreader2 = csv.reader(file2)
#     header2 = next(csvreader2)
#     for row in csvreader2:
#         rows2.append(row)

# print(rows2)

# for i in rows1:
#     for j in rows2:
#         if i[0] == j[0]:
#             # print(j[1])
msg = EmailMessage()
msg.set_content('this it to confirm your attendance!')
msg['Subject'] = 'AAS '
msg['From'] = "yellow.flash2680@gmail.com"
msg['To'] ="caml20052@glbitm.ac.in"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('yellow.flash2680@gmail.com', 'mynameissonu')
server.send_message(msg)




