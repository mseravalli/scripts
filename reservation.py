#!/usr/bin/env python
import os
import smtplib

path = "/opt/reservation"

cmd = "mkdir -p %s " % path
os.system(cmd)

cmd = "wget http://www.hacker-festzelt.de/index.php/reservierung -O %s/new_file" % path
os.system(cmd)

cmd = "diff %s/old_file %s/new_file | wc -l" % (path, path)
total_diff = os.popen(cmd).read().replace('\n', '')

fromaddr = 'marco.seravalli@gmail.com'
toaddrs  = 'marco.seravalli@gmail.com'
msg = "\r\n".join([
  "From: marco.seravalli@gmail.com",
  "To: marco.seravalli@gmail.com",
  "Subject: Reservation available",
  "",
  "The Reservation is now available"
  "http://www.hacker-festzelt.de/index.php/reservierung"
  ])
username = 'marco.seravalli@gmail.com'
password = ''

if int(total_diff) > 0:
  print("differences found")
  # server = smtplib.SMTP('smtp.gmail.com:587')
  # server.ehlo()
  # server.starttls()
  # server.login(username,password)
  # server.sendmail(fromaddr, toaddrs, msg)
  # server.quit()
  print("email sent")
else:
  print("no differences found")
