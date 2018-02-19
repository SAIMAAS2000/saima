import smtplib
s= smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("saimasalutagi@gmail.com", "saima2000")
message ="take_part_in_the_culturalprogram"
s.sendmail("saimasalutagi@gmail.com", "sne94813@gmail.com",message)
print('sucess')
s.quit()


