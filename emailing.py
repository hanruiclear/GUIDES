# send emails
import sys
import os
import re
from smtplib import SMTP
from email.mime.text import MIMEText

def send_completed_run(address, link):
  SMTPserver = os.environ.get('SMTPserver')
  sender = os.environ.get('SMTPsender')
  password = os.environ.get('SMTPpassword')
  destination = [address, "cld.history@gmail.com"]

  text_subtype = 'plain'
  subject = "CLD Run Completed"

  content = "CRISPR Library Designer has completed processing your library. Results are available here: {0}".format(link)

  try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(sender, password)
    try:
      conn.sendmail(sender, destination, msg.as_string())
    finally:
      conn.quit()

  except Exception, exc:
    print "mail failed; %s" % str(exc)
