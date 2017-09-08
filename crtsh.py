import requests
from bs4 import BeautifulSoup
import re
from MaltegoTransform import *

me = MaltegoTransform()
me.parseArguments(sys.argv)

company_name = sys.argv[1]

r = requests.get('https://crt.sh/?q=%25.' + company_name)

doc = r.content

soup = BeautifulSoup(doc, 'html.parser')

rows = []

for link in soup.findAll('td', attrs={'style': None}):
    if link.find('a'):
    	continue
    else:
    	rows.append(link.text)

regex = re.compile('Identity\sLIKE.*')
end_rows = [x for x in rows if not regex.match(x)]

new_rows = []

for row in end_rows:
  if row not in new_rows:
    new_rows.append(row)

for row in new_rows:
	ent = me.addEntity("maltego.DNSName",row)

me.returnOutput()