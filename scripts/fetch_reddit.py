#!/usr/bin/env python3
"""Fetch recent posts from r/moonmodules and write docs/assets/reddit-feed.json.

GitHub Actions runs this automatically on every deploy.
"""
import json
import urllib.request

SUBREDDIT = 'moonmodules'
URL = f'https://www.reddit.com/r/{SUBREDDIT}/new.json?limit=5'
OUTPUT = 'docs/assets/reddit-feed.json'
USER_AGENT = 'web:moonmodules-site:v1.0 (by /u/ewowi)'

posts = []
try:
    req = urllib.request.Request(URL, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.load(response)
    for child in data['data']['children']:
        p = child['data']
        img_url = ''
        try:
            img_url = p['preview']['images'][0]['source']['url'].replace('&amp;', '&')
        except (KeyError, IndexError, TypeError):
            pass
        posts.append({
            'title': p.get('title', ''),
            'permalink': p.get('permalink', ''),
            'author': p.get('author', ''),
            'created_utc': p.get('created_utc', 0),
            'score': p.get('score', 0),
            'selftext': (p.get('selftext', '') or '').strip(),
            'img_url': img_url,
        })
except Exception as e:
    print(f'Reddit fetch failed: {e}')
    print('Writing empty feed.')

with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f'Wrote {len(posts)} posts to {OUTPUT}')
for post in posts:
    print(f'  {post["title"][:60]}')
