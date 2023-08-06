from bs4 import BeautifulSoup
import requests


def anime_ranking(i, start_rank, user_anime_name, end_rank, l_pop, h_pop):
    if start_rank > end_rank:
        exit('end limit is less than start')
    if l_pop > h_pop:
        exit('low popularity should be less than high popularity')
    limit_fake = range(start_rank, end_rank, 50)
    limit = []
    for k in limit_fake:
        limit.append(k)
    count = 0
    # proxies = {"https": "http://172.16.199.40:8080", "http": "http://172.16.199.40:8080"}
    for k in limit:
        html_text = requests.get(f'https://myanimelist.net/topanime.php?limit={k}').text
        soup = BeautifulSoup(html_text, 'lxml')
        all_anime = soup.find_all('tr', class_="ranking-list")
        for anime in all_anime:
            # noinspection SpellCheckingInspection
            anime_name = anime.find('h3', class_='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3').text
            anime_rank = anime.find('td', class_='rank ac').text
            anime_score = anime.find('span', class_=f'text on score-label score-{i}')
            anime_info = anime.find('div', class_="information di-ib mt4").text
            anime_episodes = anime_info.strip().split('\n')[0].strip()
            anime_aired = anime_info.strip().split('\n')[1].strip()
            anime_popularity = anime_info.strip().split('\n')[2].strip()
            fake_number = str(anime_popularity)
            fake_number = fake_number.split(' ')
            number = int(fake_number[0].replace(',', ''))
            while anime_score is None:
                i = i - 1
                anime_score = anime.find('span', class_=f'text on score-label score-{i}')
            anime_link = anime.h3.a['href']
            if start_rank <= int(anime_rank) <= end_rank:
                if user_anime_name in str(anime_name).lower():
                    if l_pop <= number <= h_pop:
                        # if len(str(anime_aired)) < 11:
                        print(f'{anime_rank.strip()}.  {anime_name}  {anime_score.text.strip()}')
                        if len(str(anime_aired)) < 11:
                            print(f'{anime_episodes}   {anime_aired} STILL AIRING   {number:,} members')
                        else:
                            print(f'{anime_episodes}   {anime_aired}   {number:,} members')
                        print(f'{anime_link}')
                        print('')
                        count = count + 1
    print(f'Count = {count}')


start = int(input('enter start limit: '))
stop = int(input('enter end limit: '))
least_popularity = input("enter least popularity: ")
highest_popularity = input('enter highest popularity: ')
if least_popularity == '' and highest_popularity == '':
    least_popularity = 0
    highest_popularity = 999999999999
elif least_popularity == '':
    least_popularity = 0
elif highest_popularity == '':
    highest_popularity = 999999999999
least_popularity = int(least_popularity)
highest_popularity = int(highest_popularity)
user_a_name = input('Enter anime name: ')
print('')
anime_ranking(9, start - 1, user_a_name.lower(), stop, least_popularity, highest_popularity)
yes_continue = 'y'
while yes_continue in 'y1':
    yes_continue = input('again? [y/1]')
    if yes_continue in 'y1':
        start = int(input('enter start limit: '))
        stop = int(input('enter end limit: '))
        least_popularity = input("enter least popularity: ")
        highest_popularity = input('enter highest popularity: ')
        if least_popularity == '' and highest_popularity == '':
            least_popularity = 0
            highest_popularity = 999999999999
        elif least_popularity == '':
            least_popularity = 0
        elif highest_popularity == '':
            highest_popularity = 999999999999
        least_popularity = int(least_popularity)
        highest_popularity = int(highest_popularity)
        user_a_name = input('Enter anime name: ')
        print('')
        anime_ranking(9, start - 1, user_a_name.lower(), stop, least_popularity, highest_popularity)
