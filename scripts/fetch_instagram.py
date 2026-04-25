#!/usr/bin/env python3
"""Fetch recent posts from Instagram accounts and write docs/assets/instagram-feed.json.

Uses instaloader for public profile access without authentication.
Requires: pip install instaloader
"""
import json
import sys

OUTPUT = 'docs/assets/instagram-feed.json'
ACCOUNTS = ['ewoudwijma', 'milliwatt.uk', 'troy_ess']
MAX_POSTS = 3

try:
    import instaloader
except ImportError:
    print('instaloader not installed, writing empty feed')
    with open(OUTPUT, 'w') as f:
        json.dump([], f)
    sys.exit(0)

L = instaloader.Instaloader()

# Try to load a saved login session (run 'instaloader --login YOUR_USERNAME' once to create it).
# Without a session Instagram blocks requests; the script writes an empty feed gracefully.
SESSION_USER = 'ewoudwijma'
try:
    L.load_session_from_file(SESSION_USER)
    print(f'Loaded session for {SESSION_USER}')
except FileNotFoundError:
    print('No session file found: run: instaloader --login ewoudwijma')

posts = []

for username in ACCOUNTS:
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        count = 0
        for post in profile.get_posts():
            if count >= MAX_POSTS:
                break
            posts.append({
                'username': username,
                'shortcode': post.shortcode,
                'url': f'https://www.instagram.com/p/{post.shortcode}/',
                'thumbnail': post.url,
                'caption': (post.caption or '').strip()[:200],
                'date': post.date_utc.isoformat() + 'Z',
                'likes': post.likes,
            })
            count += 1
        print(f'Fetched {count} posts from {username}')
    except Exception as e:
        print(f'Failed to fetch {username}: {e}', file=sys.stderr)

with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f'Wrote {len(posts)} posts to {OUTPUT}')
