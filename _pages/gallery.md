---
layout: page
permalink: /gallery/
title: Gallery
description: Group photos, workshops and life in the NTU Plasma Theory group.
nav: true
nav_order: 6
---

<div class="gallery">
{%- for album in site.data.gallery %}
  <section class="gallery-album">
    <h2 class="gallery-album-title">{{ album.title }}</h2>
    {%- if album.date %}<p class="gallery-album-date">{{ album.date }}</p>{% endif %}
    <div class="gallery-grid{% if album.photos.size == 1 %} single{% endif %}">
      {%- for photo in album.photos %}
      <figure class="gallery-photo">
        <img src="{{ photo.file | prepend: '/assets/img/gallery/' | relative_url }}" alt="{{ photo.caption | default: album.title }}" loading="lazy" data-zoomable>
        {%- if photo.caption %}
        <figcaption>{{ photo.caption }}</figcaption>
        {%- endif %}
      </figure>
      {%- endfor %}
    </div>
  </section>
{%- endfor %}
</div>
