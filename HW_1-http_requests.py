import requests


def get_heroes(heroes_dict):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    heroes = response.json()
    stats_dict = {}
    int_list = []
    for person in heroes:
        intellegence = person['powerstats']['intelligence']
        name_hero = person['name']
        if name_hero in heroes_dict:
            int_list.append(intellegence)
            if intellegence not in stats_dict:
                stats_dict.setdefault(intellegence, [name_hero])
            else:
                stats_dict[intellegence].append(name_hero)

    smart_hero = ', '.join(stats_dict[max(int_list)])
    return print(f'Самый умный герой - {smart_hero}. Интеллект: {max(int_list)}')


if __name__ == "__main__":
    get_heroes(['Hulk', 'Captain America', 'Thanos'])