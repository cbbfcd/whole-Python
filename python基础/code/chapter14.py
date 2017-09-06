# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-06 20:21:33
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-06 21:09:31

# 使用第三方发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = '1651651@qq.com' # 发件人
password = 'XXXXXX' # 第三方SMTP给你的授权码
receivers = ['2890636389@qq.com'] # 收件人


msg = '''  
	<p>就发个邮件试一试嘛</p>
	<img src="cid:image1"></img>
'''                              # msg

mail_msg = MIMEText(msg, 'html', 'utf-8') # 构造邮件正文

message = MIMEMultipart('related') # 可构造附件
msgAlternative = MIMEMultipart('alternative') # 带图片正文
message.attach(msgAlternative)

message['From'] = Header('Python', 'utf-8')
message['To'] = Header('someone', 'utf-8')
subject = '这是一个测试'
message['Subject'] = Header(subject, 'utf-8')

# 加入邮件正文

msgAlternative.attach(mail_msg)

# 指定图片为当前目录
f = open('test.png','rb')
msgImg = MIMEImage(f.read())
f.close()

# 定义图片ID，在html中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

# 构造附件1
att1 = MIMEText(open(r'../test.txt').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
# filename 可以随便填  对方看到的就是这个名字
att1['Content-Disposition'] = 'attachment; filename="test.txt"'
message.attach(att1)

try:
	smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)# 第三方的地址和端口
	smtpObj.login(sender, password)# 登陆
	smtpObj.sendmail(sender, receivers, message.as_string())
	smtpObj.quit()
except smtplib.SMTPException:
	print('邮件发送失败')


