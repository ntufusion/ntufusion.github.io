---
layout: page
permalink: /publications/
title: Publications
description: Publications by year, most recent first.
first_year: 2023 # earliest year with its own heading; older papers go under "Before ..."
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

<div class="publications">

{%- assign this_year = site.time | date: "%Y" | plus: 0 %}
{%- for y in (page.first_year..this_year) reversed %}
  {%- capture year_pubs %}{% bibliography -f papers -q @*[year={{y}}]* %}{% endcapture %}
  {%- if year_pubs contains 'class="row"' %}
  <section class="pub-group">
  <h2 class="year">{{ y }}</h2>
  {{ year_pubs }}
  </section>
  {%- endif %}
{%- endfor %}

{%- capture older_pubs %}{% bibliography -f papers -q @*[year<{{ page.first_year }}]* %}{% endcapture %}
{%- if older_pubs contains 'class="row"' %}
  <section class="pub-group">
  <h2 class="year">Before {{ page.first_year }}</h2>
  {{ older_pubs }}
  </section>
{%- endif %}

</div>
