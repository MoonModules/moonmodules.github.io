---
layout: about
permalink: /community/
title: Community
tags: community
headshot: https://github.com/user-attachments/assets/98ec32d7-4a86-4dd0-a7a1-c0e932c06077

---

We work closely together with many people, groups or organizations. Discord is our base platform to meet us. Some of our colaborations:

* [The Glorb](https://glorb.me) - Transform any space and occasion into a mesmerizing visual experience Glorb
* [srg74](https://github.com/srg74): Binaries, ESP flasher, hardware
* [Tarna the art car](https://www.instagram.com/jackalope_tarna/): Toronto based, north America exposed art car
* [Stefan Petrick / animartrix](https://github.com/StefanPetrick/animartrix): High quality LED animations for your next project
* [hpwit](https://github.com/hpwit): clockless (virtual) driver and ESPLiveScript
* [wladi](): Installers, hardware
* Contributors ...


<div id="stats" class="hidden">

<h3 id="dashboard"><code>#dashboard</code></h3>

<h2>Just finished.</h2>

<p>Curious what I'm reading? Here's my most recent reads, updating daily. And my <a href="https://www.goodreads.com/user/show/88184044-jonathon-belotti)" target="_blank" rel="noopener noreferrer">Goodreads profile</a> has more history.</p>

<div id="recent-finished-books"></div>

<h2>Top tracks.</h2>

<p>Curious what I'm currently listening to? Here's my top tracks on Spotify, updating daily.</p>

<ol id="top-spotify-tracks"></ol>

</div>

<script>
/**
 * @param {String} HTML representing a single element
 * @return {Element}
 */
function htmlToElement(html) {
    var template = document.createElement('template');
    /* Never return a text node of whitespace as the result */
    html = html.trim();
    template.innerHTML = html;
    return template.content.firstChild;
}

function populateDashboardHTML(data) {
    const topSpotifyTracksList = document.querySelector('#top-spotify-tracks');
    data.spotify.forEach(track => {
        topSpotifyTracksList.appendChild(htmlToElement(`
            <li>
                <a target="_blank" rel="noopener noreferrer" href="${track.link}"><strong>${track.name}</strong></a> 
                <p>${track.artist}</p>
            </li>
        `));
    });

    const recentFinishedBooks = document.querySelector('#recent-finished-books');
    data.goodreads.slice(0, 3).forEach(book => {
        recentFinishedBooks.appendChild(htmlToElement(`
            <a target="_blank" rel="noopener noreferrer" class="book-item" target="_blank" rel="noopener noreferrer" href="${book.link}">
            <div class="cover-container">
                <img class="grow-me" src="${book.cover_image_link}">
            </div>
            <div class="book-info">
                <h4>${book.title}</h4>
                <p>${book.authors[0]}</p>
            </div>
            </a>
        `));
    });
}

fetch('https://thundergolfer--thundergolferdotcom-about-page-web.modal.run')
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    return response.json();
  })
  .then((data) => {
    populateDashboardHTML(data);
    /* Reveal the now populated stats section. */
    document.getElementById("stats").classList.remove("hidden");
  });

</script>

<style>
#stats {
  background-color: #f7f7f9;
  border-radius: 1rem; 
  padding: 1.5em;
  margin-top: 2.5em;
}

#dashboard {
  margin: 0rem;
}

#dashboard code {
  background-color: #f7f7f9;
}

#recent-finished-books {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
}

#recent-finished-books a {
    color: #111;
}

.book-item {
    margin-left: 0.4em;
    margin-right: 0.4em;
}

.book-item div {
    width: 200px;
}

.book-info h4 {
    color: #222;
}

.book-info p {
    color: #555;
}

.grow-me {
  border-radius: 4px;
  transition: all .2s ease-in-out;
}

.grow-me:hover {
  transform: scale(1.02);
}

#top-spotify-tracks {
    padding-left: 1em;
}

#top-spotify-tracks li {
    color: #888;
    border-bottom: 1px solid #ededed;
    margin-top: 1rem;
}

#top-spotify-tracks a {
    color: #111;
}

#top-spotify-tracks a:hover {
    color: #1DB954; /* Spotify green */
}

#top-spotify-tracks p {
    color: #555;
}

.hidden {
    display: none;
}

@media screen and (max-width: 900px) {


  #recent-finished-books {
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .book-item div {
    width: 400px;
  }

  .book-item {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .cover-container, .book-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 80%;
  }

  #top-spotify-tracks {
    padding-left: 1.2em;
  }
}
</style>
