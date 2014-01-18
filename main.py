import spynner
from bs4 import BeautifulSoup
from getpass import getpass

username = raw_input('Enter your email address: ')
password = getpass('Enter your password: ')
b = spynner.Browser()
b.load('https://myaccount.teksavvy.com/')
b.wk_fill('input[name=login]', username)
b.wk_fill('input[name=password]', password)
b.click(".tsi-full-width > button:nth-child(1)")
b.click(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)")
b.wait(3)
b.click('a[href="/Services/ServiceDetails/466259"]')
b.wait(3)
b.click('a[href="/Services/ServiceDetails/466259/ViewUsage]')
soup = BeautifulSoup(b.html)

usage = soup.find('span', {'class' : 'tsi-monthlyUsageLabel'})
print 'Used: ' + usage.encode_contents()
remaining = soup.find('div', {'class' : 'tsi-progresLabelBottom'})
print remaining.encode_contents()
cap = soup.find('span', {'class' : 'tsi-progresLabelRigth'})
print 'Cap: ' + cap.encode_contents()
