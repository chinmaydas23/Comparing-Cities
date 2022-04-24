from django.shortcuts import redirect, render
# from django.shortcuts import render_to_response

from .forms import ProjectModel
import pandas as pd
from lxml import etree 
import json
import requests
from bs4 import BeautifulSoup
import random
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import re

# Create your views here.
def project_view(request):
    form = ProjectModel()
    return render(request, 'index.html', { 'form': form })

def test_view(request):

    metadata = pd.read_csv('/home/pal/Desktop/190953194/AP_PROJECT/myProject/project/Book1.csv', low_memory=False)
    text1 = request.GET.get('City1')
    text2 = request.GET.get('City2')

    p1 = ""
    lat1 = ""
    lng1 = ""
    p2 = ""
    lat2 = ""
    lng2 = ""
    for i in range(len(metadata)):
        x = metadata['city'].iloc[i]
        x = x.replace('ā', 'a')
        if x.lower() == text1.lower():
            p1 = metadata['population'].iloc[i]
            lat1 = metadata['lat'].iloc[i]
            lng1 = metadata['lng'].iloc[i]
        if x.lower() == text2.lower():
            p2 = metadata['population'].iloc[i]
            lat2 = metadata['lat'].iloc[i]
            lng2 = metadata['lng'].iloc[i]

    api_key = "4c919df4e86d57b891eed04790aa5c81"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = weather_url + "appid=" + api_key + "&q=" + text1
    response = requests.get(complete_url)
    x = response.json()
    print(x)
    y = x['main']
    current_temperature = round(y["temp"] - 273, 2)
    z = x["weather"]
    weather_description = z[0]["description"]
    t1 = str(current_temperature) + ' °C'
    wd1 = weather_description

    api_key = "4c919df4e86d57b891eed04790aa5c81"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = weather_url + "appid=" + api_key + "&q=" + text2
    response = requests.get(complete_url)
    x = response.json()
    print(x)

    y = x['main']
    current_temperature = round(y["temp"] - 273, 2)
    z = x["weather"]
    weather_description = z[0]["description"]
    t2 = str(current_temperature) + ' °C'
    wd2 = weather_description 

    # OPEN_WEATHER_MAP_APIKEY = '4c919df4e86d57b891eed04790aa5c81'

    # url = f'https://api.openweathermap.org/data/2.5/weather?q={text1}&appid={OPEN_WEATHER_MAP_APIKEY}'
    # print(f"Getting data via {url}")
    # r = requests.get(url)
    # print(r.json())

    #headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    # res = requests.get(
    #     f'https://www.google.com/search?q={text1}&oq={text1}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

    # soup = BeautifulSoup(res.text, 'html.parser')
    # #location = soup.select('#wob_loc')[0].getText()
    # time = soup.select('#wob_dts')
    # info = soup.select('#wob_dc')
    # weather = soup.select('#wob_tm')
    # print(time)
    # print(info)
    # print(str(weather)+"°C")

    url = "https://en.wikipedia.org/wiki/" + text1
    response = requests.get(url)

    print(url)
    store = etree.fromstring(response.text) 

    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="Country"]/td/a') 
    c1 = x[0].text
    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/a/text()="State"]/td/a')
    if len(x) == 0:
        x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="State"]/td/a')
    s1 = x[0].text
    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/a/text()="District"]/td/a')
    if len(x) == 0:
        x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="District"]/td/a')
    d1 = x[0].text
    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="Website"]/td/span/a/text()')
    y = "https://"
    for i in range(len(x)):
        y += x[i]
    w1 = y

    html_page = urlopen(url)
    images = []
    soup = BeautifulSoup(html_page)

    for img in soup.findAll('img'):
        images.append(img.get('src'))
    i1 = "https:"+ str(images[random.randint(2,10)])

    url = "https://en.wikipedia.org/wiki/" + text2
    response = requests.get(url)

    print(url)
    store = etree.fromstring(response.text) 

    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="Country"]/td/a') 
    c2 = x[0].text
    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/a/text()="State"]/td/a')
    if len(x) == 0:
        x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="State"]/td/a')
    s2 = x[0].text
    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/a/text()="District"]/td/a')
    if len(x) == 0:
        x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="District"]/td/a')
    d2 = x[0].text
    x = store.xpath('//table[@class="infobox ib-settlement vcard"]/tbody/tr[th/text()="Website"]/td/span/a/text()')
    y = "https://"
    for i in range(len(x)):
        y += x[i]
    w2 = y

    html_page = urlopen(url)
    images = []
    soup = BeautifulSoup(html_page)

    for img in soup.findAll('img'):
        images.append(img.get('src'))
    i2 = "https:"+ str(images[random.randint(2,10)])

    text1 = text1.capitalize()
    text2 = text2.capitalize()

    return render(request, 'test.html', { 'text_1_data': c1, 'text_2_data': s1, 'text_3_data': d1, 'text_4_data': p1, 'text_5_data': lat1, 'text_6_data': lng1, 'text_7_data': t1, 'text_8_data': wd1, 'text_17_data': w1, 
                                        'text_9_data': c2, 'text_10_data': s2, 'text_11_data': d2, 'text_12_data': p2, 'text_13_data': lat2, 'text_14_data': lng2, 'text_15_data': t2, 'text_16_data': wd2, 'text_18_data': w2, 'text_19_data': text1, 'text_20_data': text2,  'text_21_data': i1, 'text_22_data': i2})  