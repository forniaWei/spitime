import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = '245463698@qq.com'#发送者
password = "PRRKMLUOECYIXCSO"
sender = username
receivers = ','.join(['163.com'])#接收者


def email(report):
# 设置请求头信息

	msg = MIMEMultipart()
	msg['Subject'] = '接口测试报告'  # 邮件名
	msg['From'] = sender
	msg['To'] = receivers

	jpgpart = MIMEApplication(open(report, 'rb').read())
	jpgpart.add_header('Content-Disposition', 'attachment', filename=report)
	msg.attach(jpgpart)

	#发送邮件
	client = smtplib.SMTP()
	client.connect('smtp.qq.com')

	client.login(username, password)
	client.sendmail(sender, receivers, msg.as_string())
	client.quit()
	print("邮件发送成功，请查看！")

if __name__ == "__main__":
	re ="F:/测试/2.png"
	email(re)