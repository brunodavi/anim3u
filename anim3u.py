#!/usr/bin/python3

import requests

from re import findall, sub
from ancli import make_cli

def anim3u(link, start=1, end=30):
    """

    Criar uma lista de animes em m3u

    Args:
        link  (str): Link da página do anime
        start (int): Episódio inicial da lista 
        end   (int): Episódio final da lista
    """

    part = 1

    if 'goyabu.com' not in link:
        link = input('Cole o link da página do anime em goyabu.com: ')

    paged = f'?paged={part}'
    started = 0

    if link[-1] != '/':
        link += f'/{peged}'
    else:
        link += f'{paged}'


    def openurl(url):
        import urllib3
        urllib3.disable_warnings()
        return requests.get(url, verify=False)


    revt = r'href="(https://goyabu.com/videos/\d+/)" title="(.+?)"'

    page = openurl(link).text
    anime = findall(revt, page)

    m3u = findall(r'<img alt="(.+?)"', page)[0]
    m3u = m3u.replace(' ', '-')
    m3u = m3u.lower()
    m3u += '.m3u'

    while len(anime) < end:
        part += 1

        link = sub(r'paged=\d+$', f'paged={part}', link)
        page = openurl(link).text
        page = findall(revt, page)

        if len(page) == 30:
            anime += page

        else:
            anime += page
            break

        print(f'Parte {part}, carregada!\n')

    anime += [(0, 1)]

    playlist = open(m3u, 'w')
    playlist.write('#EXTM3U\n\n\n')

    playlist.mode = 'a'

    for url, title in anime[start-1:end]:

        html = openurl(url).text
        title = title.replace('&#8211;', '-')

        video = findall(r"src='(.+?)'", html)[1]

        print(url, title)
        print()

        print(video)
        print('\n')

        playlist.write(f'#EXTINF:-1, {title}\n{video}\n\n')

    playlist.close()


make_cli(anim3u)
