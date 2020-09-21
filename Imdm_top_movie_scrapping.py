import bs4
import requests
res=requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250','lxml')
soup=bs4.BeautifulSoup(res.text)
images=soup.select('img')
for rank in range(250):
    image_link=images[rank]['src']
    required_image=requests.get(image_link,'lxml')
    f=open('Extracted_Images\Rank '+str(rank+1)+'.jpg','wb')
    f.write(required_image.content)
    f.close()