# TIARA - The Internet Archive Research Assistant
# by Kay Savetz @KaySavetz, May 2021. Released under MIT License
# https://opensource.org/licenses/MIT
#
# Searches Internet Archive using its full text search for new items matching
# the keywords you specify (in searchlist.txt, one search term per line)
#
# Run this script once a day via crontab for daily updates about new items
# relevant to your research topics
#
# Outputs its findings to an html file, and optionally emails that file
# to you via SendGrid or your system mail (eg Sendmail or Postfix)
#
# Dependency: Internet Archive command line tool (pip install internetarchive)
# Info at https://github.com/jjjake/internetarchive
# Also requires read-write access to the directory the script lives in 

FROM_EMAIL = 'you@example.com'
TO_EMAIL   = 'you@example.com'
USE_SENDGRID = False
    # for this option you must have a SendGrid account (their free account is fine)
    # with an API key installed on your system, and the SendGrid helper library
    # installed. Your account must have your FROM_EMAIL as a verified sender. 
    # https://sendgrid.com/docs/for-developers/sending-email/quickstart-python/
USE_SYSTEMMAIL = False
    # for this option your system must have sendmail or postfix or similar installed
    # and configured. 


import internetarchive
import json
import os
from datetime import date
from datetime import timedelta
import urllib
import time

#days = 1 searches yesterday through today. You could make it search more days
#without harm if you can't run this script daily
searchstart = date.today() - timedelta(days = 1)
print("Searching from " + str(searchstart) + " to today")

todaysFilename = str(date.today()) + ".html"
if os.path.exists(todaysFilename):
    os.remove(todaysFilename)

with open('searchlist.txt') as f:
    searchList = f.readlines()
    f.close()
searchList = [x.strip() for x in searchList]

for searchTerm in searchList:
    time.sleep(5) #throttle searches to avoid offending archive.org
    print(searchTerm)
    out=''

    #get list of matching items from IA
    stream = os.popen("ia search --timeout 300 --fts '" + searchTerm +" AND publicdate:[" + str(searchstart) + " TO *]'")
    lines = stream.readlines()

    print("    " + str(len(lines)) + " item", end = '')
    if len(lines) != 1:
        print("s", end = '')
    print(" returned")

    if(len(lines)==0):
        continue;

    #get the list of items we've seen before
    if os.path.exists(searchTerm + '-known.txt'):
        knownItems = set(line.strip() for line in open(searchTerm + '-known.txt'))
    else:
        knownItems = set()
    print("    " + str(len(knownItems)) + " already known")

    f = open(searchTerm + '-known.txt',"a")
    rowcounter=0
    newcounter=0
    for line in lines:
        myDict = json.loads(line) #convert from string to dictionary
        if myDict['fields']['identifier'][0] not in knownItems:
            f.write(myDict['fields']['identifier'][0] + "\n")
            rowcounter+=1
            newcounter+=1
            if rowcounter==1:
                out += "<tr>"
            out += '<td><a href="https://archive.org/details/' + myDict['fields']['identifier'][0]
            out += '/mode/2up?q=' + urllib.parse.quote_plus(searchTerm) + '">'
            out += '<img width="180" src="https://archive.org/serve/' + myDict['fields']['identifier'][0]+ '/__ia_thumb.jpg"><br />'
            out += myDict['fields']['meta_title'][0]
            out += '</a></td>\r'
            if rowcounter==4:
                out += '</tr>\r'
                rowcounter=0
    print("    " + str(newcounter) + " new item",end='')
    if newcounter != 1:
        print("s")
    else:
        print()
    f.close()

    if(out):
        f=open(todaysFilename, "a+")
        f.write('<h1>' + searchTerm + '</h1>\r')
        f.write('<table>\r')
        f.write(out)
        f.write('</table>\r\r')
        f.close()

print("Finished searches.")

if os.path.exists(todaysFilename):
    print("New items were found")

    f=open(todaysFilename, "a+")
    f.write('<p><a href="https://archive.org/donate/"><b>Donate to Internet Archive</b></a></p>')
    f.close()

#the rest of the script deals with emailing the output
    if USE_SENDGRID or USE_SYSTEMMAIL:
        #reload entire output file for emailing
        myFile=open(todaysFilename,mode="r")
        output = myFile.read()
        myFile.close()

    if USE_SENDGRID:
    #taken from https://app.sendgrid.com/guide/integrate/langs/python
    #You (must be logged in to access that URL)
        print("Attempting to send mail with SendGrid")
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=TO_EMAIL,
            subject='TIARA Update for ' + str(date.today()),
            html_content=output)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

    if USE_SYSTEMMAIL:
    #taken from https://stackoverflow.com/questions/882712/sending-html-email-using-python
        print("Attempting to send mail with system mail")

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'TIARA Update for ' + str(date.today())
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL

        # Create the body of the message (a plain-text and an HTML version).
        text = "You need to read this in html :("
        html = output

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        s = smtplib.SMTP('localhost')
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        s.quit()

else:
    print("No new items were found")

print("Done!")
