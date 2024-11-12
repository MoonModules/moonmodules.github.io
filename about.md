---
layout: about
permalink: /about/
title: A little bit about moonmodules.
tags: about
headshot: 
---


MoonModules has been founded in 2021 by Ewowi and Harry Baas who at the time developed audio and 2D functionality and effects for the Atuline WLED fork. Effects like Akemi, Game of Live and GEQ where developed during this time as well as developing showcases for multiple layered effects.

Since then we have worked on the first release of Aircoookie WLED 0.14 which introduced Sound Reactive and 2D support as created in the Atuline fork. At this time SoftHack007 joined. We also supported subsequent releases, which we do sence then.

At the same time we developed WLED MM, a new fork of Aircoookie WLED as we had more ideas and creativity then Aircoookie WLED could digest. The MoonModules knowledge repository gives an overview of what we made. Recent versions of WLED MM focus a lot on large LED installations, Art-Net support and Hub-75 support. Since this time, Troy, Soren and NetMindz joined MoonModules.

Since 2023, we are also developing a new product, based on our experience working with WLED. We took the module concept of WLED and took that further by making everything a module, this was called StarMod. This then allowed us to split LED and non-LED functionality and StarBase and StarLight was born. StarBase containing generic functionality and StarLight to add lighting functionality on top of that. As StarBase is generic and can be used to develop any ESP32 based application. StarLight key features are 3D support, support for any fixture, projections, up to 16384 LEDs, Live coding of fixture definitions, effects and projections, artnet and dmx support.

## edit this site

* use [kraken](https://kraken.io/web-interface) or similar to minimize image size (as 200kb + images slows down website significantly). Images and videos can be stored in the github repo (drag and drop on a page while editing) or external cloud storage can be used (maybe faster than github).
* to edit a page, press ✎ below the page (direct in repo or using PR)
* to add a post go to the [collections/_posts](https://github.com/MoonModules/moonmodules.github.io/tree/main/collections/_posts) folder and add a file there use yyyy-mm-dd-this-is-about-leds.md structure as file name

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
