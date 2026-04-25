function renderYouTubeItems(items, container) {
  if (!items.length) { container.innerHTML = ''; return; }
  container.innerHTML = items.map(item => {
    const date = item.published ? new Date(item.published).toLocaleDateString('en-GB', {
      year: 'numeric', month: 'short', day: 'numeric'
    }) : '';
    const descHtml = item.description
      ? `<div class="yt-card__desc">${item.description.slice(0, 120)}${item.description.length > 120 ? '…' : ''}</div>`
      : '';
    return `<a class="yt-card" href="${item.link}" target="_blank" rel="noopener noreferrer">
      ${item.thumbnail ? `<img src="${item.thumbnail}" alt="" loading="lazy">` : ''}
      <div class="yt-card__body">
        <div class="yt-card__title">${item.title}</div>
        <div class="yt-card__date">${date}</div>
        ${descHtml}
      </div>
    </a>`;
  }).join('');
}

async function loadYouTubeFeed() {
  const shortsContainer = document.getElementById('youtube-shorts');
  const videosContainer = document.getElementById('youtube-videos');
  if (!shortsContainer && !videosContainer) return;

  try {
    const res = await fetch('/assets/youtube-feed.json');
    if (!res.ok) return;
    const data = await res.json();
    if (shortsContainer) renderYouTubeItems(data.shorts || [], shortsContainer);
    if (videosContainer) renderYouTubeItems(data.videos || [], videosContainer);
  } catch {
    if (shortsContainer) shortsContainer.innerHTML = '';
    if (videosContainer) videosContainer.innerHTML = '';
  }
}

async function loadRedditFeed() {
  const containers = document.querySelectorAll('[data-feed="reddit"]');
  if (!containers.length) return;

  try {
    const res = await fetch('/assets/reddit-feed.json');
    if (!res.ok) return;
    const posts = await res.json();
    if (!posts.length) return;

    const html = posts.map(p => {
      const date = new Date(p.created_utc * 1000).toLocaleDateString('en-GB', {
        year: 'numeric', month: 'short', day: 'numeric'
      });
      const imgHtml = p.img_url
        ? `<img class="reddit-post__img" src="${p.img_url}" alt="" loading="lazy">`
        : '';
      const descHtml = p.selftext
        ? `<span class="reddit-post__desc">${p.selftext.slice(0, 150)}${p.selftext.length > 150 ? '…' : ''}</span>`
        : '';
      return `<a class="reddit-post" href="https://reddit.com${p.permalink}" target="_blank" rel="noopener noreferrer">
        ${imgHtml}
        <div class="reddit-post__content">
          <span class="reddit-post__title">${p.title}</span>
          ${descHtml}
          <span class="reddit-post__meta">u/${p.author} &middot; ${date} &middot; &#9650; ${p.score}</span>
        </div>
      </a>`;
    }).join('');

    containers.forEach(c => { c.innerHTML = html; });
  } catch {
    containers.forEach(c => { c.innerHTML = ''; });
  }
}

async function loadInstagramFeed() {
  const containers = document.querySelectorAll('[data-feed="instagram"]');
  if (!containers.length) return;

  try {
    const res = await fetch('/assets/instagram-feed.json');
    if (!res.ok) return;
    const posts = await res.json();
    if (!posts.length) return;

    const html = posts.map(p => {
      const date = p.date ? new Date(p.date).toLocaleDateString('en-GB', {
        year: 'numeric', month: 'short', day: 'numeric'
      }) : '';
      const captionHtml = p.caption
        ? `<span class="ig-card__desc">${p.caption.slice(0, 150)}${p.caption.length > 150 ? '…' : ''}</span>`
        : '';
      return `<a class="ig-card" href="${p.url}" target="_blank" rel="noopener noreferrer">
        ${p.thumbnail ? `<img src="${p.thumbnail}" alt="" loading="lazy">` : ''}
        <div class="ig-card__body">
          <span class="ig-card__user">@${p.username}</span>
          ${captionHtml}
          <span class="ig-card__meta">${date}${p.likes ? ` &middot; &#9825; ${p.likes}` : ''}</span>
        </div>
      </a>`;
    }).join('');

    containers.forEach(c => { c.innerHTML = html; });
  } catch {
    containers.forEach(c => { c.innerHTML = ''; });
  }
}

function init() {
  loadYouTubeFeed();
  loadRedditFeed();
  loadInstagramFeed();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
