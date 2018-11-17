import random
from urllib import request
import urllib.request
goog_url="http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=25&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"
print  ('hey Abeer')
def download_csv(reurl):
    respone=request.urlopen(reurl)
    save=respone.read()
    convert=str(save)
    lines=convert.split('\\n')
    des_url=r'goole.csv'
    open_it=open(des_url,"w")
    for line in lines:
     open_it.write(line  +"\n")
    open_it.close()
def download_image(url):
    name=random.randrange(1,100)
    fullname=str(name)+'.jpg'
    urllib.request.urlretrieve(url,fullname)

download_image("http://www.gannett-cdn.com/-mm-/3f4774892224643ff3e9b66bc9daa4dd01767531/c=0-0-3180-4229&r=537&c=0-0-534-712/local/-/media/USATODAY/test/2013/08/15/1376574972000-AP-Film-Shailene-Woodley.jpg")
download_csv(goog_url)