---
layout: page
permalink: /gallery/
title: Gallery
description: Group photos, workshops and life in our group.
nav: true
nav_order: 6
---

<!-- One grid of same-shape tiles, newest first; click a photo to see all of it -->
<div class="gallery-grid">
{%- for album in site.data.gallery %}
  {%- for photo in album.photos %}
  <figure class="gallery-tile">
    <img src="{{ photo.file | prepend: '/assets/img/gallery/' | relative_url }}" alt="{{ photo.caption | default: album.title }}" title="{{ photo.caption | default: album.title }}" loading="lazy" data-zoomable>
    <figcaption>
      <span class="gallery-tile-title">{{ album.title }}</span>
      {%- if album.date %}<span class="gallery-tile-date">{{ album.date }}</span>{% endif %}
    </figcaption>
  </figure>
  {%- endfor %}
{%- endfor %}
</div>
