1. 注册126邮箱
2. 登录并配置  
设置 -> POP3/SMTP/IMAP -> POP3/SMTP服务 -> 开启 -> 发送短信 ->保存**授权码**
3. 发送携带账户和凭证+邮箱内容+目标  

```python
# 模块导入
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 输入参数
key = 'POYRNXPTSWWGDHHR' # 授权码
main_content = '你好，测试发邮件'  # 文件内容
sender_name = 'zql'  # 发送人名称
sender_mail = 'xiaowei_1990617@126.com'  # 发送人邮箱
receiver_mail = 'xiaowei_1990617@126.com' # 接收人邮箱
subject = '学习python' # 主题

# 构建邮件内容
msg = MIMEText(main_content, 'html', 'utf-8')
msg['From'] = formataddr([sender_name, sender_mail])
msg['to'] = receiver_mail
msg['Subject'] = subject

# 发送邮件
server = smtplib.SMTP_SSL('smtp.126.com')
server.login(sender_mail, key) # 账户/授权码
server.sendmail(sender_mail, receiver_mail, msg.as_string())
server.quit()
```