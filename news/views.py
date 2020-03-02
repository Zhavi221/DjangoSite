import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
import time, datetime

requests.packages.urllib3.disable_warnings()

def news_list(request):
    headlines = Headline.objects.all()[::-1]

    return render(request, "news/home.html", {
		'object_list': headlines,
	})


def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)%22%7D"}
    url = "https://www.ynet.co.il/home/0,7340,L-8,00.html"

    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class":"str3s str3s_small str3s_type_small"})
    Titles = soup.find_all('div',{"class":"title"})
    TitlesText = []
    for title in Titles:
        t = title.text
        TitlesText.append(t)

    i = 0
    new_headline_links = []
    for article in Headline.objects.all():
        new_headline_links.append(article.title)


    for artcile in News:
        main = artcile.find_all('a')[0]

        link = main['href']
        image_src = str(main.find('img')['src']).split(" ")[0]

        if (TitlesText[i] in new_headline_links):
            break

        if (link.find("https") != -1):
            link2 = link
        else:
            link2 = "https://www.ynet.co.il/"+link

        link2 = link2.replace('#autoplay','')
        articleContent = session.get(link2, verify=False).content
        print(link2)
        soup = BSoup(articleContent, "html.parser")

        new_headline = Headline()


        ok = "פורסם:"
        #header = soup.find_all('div', {"class":"element B3 ghcite noBottomPadding"})[0]
        dates = soup.find_all('span', string=ok)
        print(dates)


        new_headline.date = dates[1].text
        new_headline.title = TitlesText[i]
        new_headline.url = link2
        new_headline.image = image_src
        #if (new_headline.date != 'error#'):
        #    new_headline.save()
        new_headline.save()
        i = i + 1


    return redirect("../")
