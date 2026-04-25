document.addEventListener('DOMContentLoaded', function () {
  var content = document.querySelector('.md-content__inner');
  if (!content) return;

  var headings = Array.from(content.querySelectorAll('h2'));
  if (headings.length < 2) return;

  var nav = document.createElement('div');
  nav.className = 'page-nav-top';

  headings.forEach(function (h) {
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.className = 'btn-sm';
    // Strip the ¶ permalink character MkDocs appends
    a.textContent = h.textContent.replace(/\s*¶\s*$/, '').trim();
    nav.appendChild(a);
  });

  // Insert just after the h1, or at the very top if there is none
  var h1 = content.querySelector('h1');
  if (h1 && h1.nextSibling) {
    content.insertBefore(nav, h1.nextSibling);
  } else {
    content.insertBefore(nav, content.firstChild);
  }
});
