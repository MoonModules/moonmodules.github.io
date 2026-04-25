#!/usr/bin/env python3
"""Fetch the MoonModules YouTube channel RSS and write docs/assets/youtube-feed.json.

Separates Shorts (URLs containing /shorts/) from regular videos.
GitHub Actions runs this automatically on every deploy.
"""
import json
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, parse_qs

CHANNEL_ID = 'UCcDx11J_nyARSRDap0CSqIw'
RSS_URL = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'
OUTPUT = 'docs/assets/youtube-feed.json'
MAX_EACH = 6

NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'media': 'http://search.yahoo.com/mrss/',
    'yt': 'http://www.youtube.com/xml/schemas/2015',
}


def extract_video_id(url):
    parsed = urlparse(url)
    if '/shorts/' in parsed.path:
        return parsed.path.split('/shorts/')[-1].split('/')[0]
    params = parse_qs(parsed.query)
    return params.get('v', [''])[0]


shorts = []
videos = []

try:
    req = urllib.request.Request(RSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)

    for entry in root.findall('atom:entry', NS):
        title = entry.findtext('atom:title', namespaces=NS) or ''
        link_el = entry.find('atom:link', NS)
        link = link_el.get('href', '') if link_el is not None else ''
        published = entry.findtext('atom:published', namespaces=NS) or ''
        video_id = extract_video_id(link)
        thumb_el = entry.find('.//media:thumbnail', NS)
        thumbnail = thumb_el.get('url', '') if thumb_el is not None else ''
        if not thumbnail and video_id:
            thumbnail = f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg'
        desc_el = entry.find('.//media:description', NS)
        description = (desc_el.text or '').strip() if desc_el is not None else ''

        item = {
            'title': title,
            'link': link,
            'published': published,
            'thumbnail': thumbnail,
            'description': description,
        }

        if '/shorts/' in link:
            shorts.append(item)
        else:
            videos.append(item)

except Exception as e:
    print(f'YouTube fetch failed: {e}')
    print('Writing empty feed.')

output = {
    'shorts': shorts[:MAX_EACH],
    'videos': videos[:MAX_EACH],
}

with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Wrote {len(output["shorts"])} shorts and {len(output["videos"])} videos to {OUTPUT}')
