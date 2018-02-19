Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/ec2017b213/emawriting.py ==================
Traceback (most recent call last):
  File "/home/ec2017b213/emawriting.py", line 4, in <module>
    s.login("saimasalutagi@gmail.com", "saima2000")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbul\n5.7.14 dahIprPQR5H7b_7DexaA_kYIum8AKapa0iYcUadZbaBrKwaGF6MvUYm9psl5m23M61iu8z\n5.7.14 eKvdYOOV-B9dW8RNlMUFgMiLwnj0XiRrKsyGE_oonVTGUEY5T6LlymeF9hBza0EqU2VKq5\n5.7.14 t6ICl9u6UYnt-EQfSfl-JUxFM_lX19mJTcfhK_7bMo76gzsyyzefIa-sHH6emp6BBrYtLy\n5.7.14 XS16F5BvdjFmomd4QM50F88m_BiUo> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 r13sm47818302pgq.25 - gsmtp')
>>> 
================== RESTART: /home/ec2017b213/emawriting.py ==================
sucess
>>> 
