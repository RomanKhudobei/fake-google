import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from search.models import RandomText, ShowLog


def main_search_page(request):
    return render(request, 'main_search_page.html')


def results_page(request):
    search_query = request.GET.get('q')
    start = request.GET.get('start')

    if request.META['HTTP_HOST'] == '46.200.74.26':
        return HttpResponseRedirect(f'http://google.com/search?q={search_query}')

    if search_query is None:
        return redirect(reverse('main_search_page'))

    user_agent = UserAgent()

    response = requests.get(
        f'https://www.google.com/search?q={search_query}{"&start=" + start if start else ""}',
        headers={'User-Agent': user_agent.random}
    )

    soup = BeautifulSoup(response.content.decode(), 'html.parser')
    search_results = soup.find('div', attrs={'class': 'srg'})

    if search_results is None:
        search_results = soup.find('div', attrs={'id': 'topstuff'})

    else:
        for result_title in search_results.find_all('div', {'class': 'r'}):

            first_child = result_title.contents[0]

            if first_child.name == 'div':
                first_child.extract()

    if search_results is None:
        return render(request, '404.html', {'search_query': search_query})

    appbar = soup.find('div', {'id': 'appbar'})
    extrares = soup.find('div', attrs={'id': 'extrares'})
    foot = soup.find('div', attrs={'id': 'foot'})

    random_text = RandomText.objects.filter(enabled=True)

    if random_text:
        random_text = random.choice(list(random_text))

        ShowLog.objects.create(
            shown=random_text
        )

    return render(request, template_name='results_page.html', context={
        'search_results': search_results.prettify() if search_results else '',
        'extrares': extrares.prettify() if extrares else '',
        'search_query': search_query,
        'appbar': appbar.prettify() if appbar else '',
        'foot': foot.prettify() if foot else '',
        'random_text': random_text.text if random_text else None
    })


def error(request):
    return render(request, template_name='404.html')
