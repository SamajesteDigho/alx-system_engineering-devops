#!/usr/bin/python3
# Here is the exo 100
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """ Recursive workover """
    if not word_list or word_list == {} or not subreddit:
        return None
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Python3/API'
    }
    params = {'limit': 100}

    if after:
        params['after'] = after
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    collected_data = response.json()
    data = collected_data.get('data')
    children = data.get('children')

    for post in children:
        title = post.get('data', {}).get('title').lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())
    after = collected_data.get("data", {}).get('after')
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))

        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
