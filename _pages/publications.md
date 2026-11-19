---
layout: page
permalink: /publications/
title: Publications
description: Publications by year, most recent first. Group members are shown in bold.
first_year: 2023 # earliest year with its own heading; older papers go under "Before ..."
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

<div class="pub-filter" role="group" aria-label="Filter publications by research area">
  <button type="button" class="pub-filter-btn active" data-topic="all" aria-pressed="true">All</button>
  <button type="button" class="pub-filter-btn" data-topic="core" aria-pressed="false">Core turbulence &amp; transport</button>
  <button type="button" class="pub-filter-btn" data-topic="edge" aria-pressed="false">Edge &amp; SOL</button>
  <button type="button" class="pub-filter-btn" data-topic="mhd" aria-pressed="false">MHD &amp; energetic particles</button>
  <button type="button" class="pub-filter-btn" data-topic="ai" aria-pressed="false">AI &amp; data-driven models</button>
</div>

<div class="publications">

{%- capture preprints %}{% bibliography -f papers -q @*[is_preprint=true]* %}{% endcapture %}
{%- if preprints contains 'class="row"' %}
  <section class="pub-group">
  <h2 class="year">Preprints</h2>
  {{ preprints }}
  </section>
{%- endif %}

{%- assign this_year = site.time | date: "%Y" | plus: 0 %}
{%- for y in (page.first_year..this_year) reversed %}
  {%- capture year_pubs %}{% bibliography -f papers -q @*[year={{y}}, is_preprint!=true]* %}{% endcapture %}
  {%- if year_pubs contains 'class="row"' %}
  <section class="pub-group">
  <h2 class="year">{{ y }}</h2>
  {{ year_pubs }}
  </section>
  {%- endif %}
{%- endfor %}

{%- capture older_pubs %}{% bibliography -f papers -q @*[year<{{ page.first_year }}, is_preprint!=true]* %}{% endcapture %}
{%- if older_pubs contains 'class="row"' %}
  <section class="pub-group">
  <h2 class="year">Before {{ page.first_year }}</h2>
  {{ older_pubs }}
  </section>
{%- endif %}

<p class="pub-filter-empty" hidden>No publications in this area yet.</p>

</div>

<script>
  // Topic filter: shows only papers tagged with the chosen area (tags are the "research_area" field in papers.bib)
  (function () {
    var buttons = document.querySelectorAll('.pub-filter-btn');
    var groups = document.querySelectorAll('.publications .pub-group');
    var empty = document.querySelector('.pub-filter-empty');
    function apply(topic) {
      var shownTotal = 0;
      groups.forEach(function (group) {
        var shown = 0;
        group.querySelectorAll('ol.bibliography > li').forEach(function (li) {
          var row = li.querySelector('.row[data-topics]');
          var tags = row ? row.getAttribute('data-topics').split(/\s+/) : [];
          var match = topic === 'all' || tags.indexOf(topic) !== -1;
          li.hidden = !match;
          if (match) shown++;
        });
        group.hidden = shown === 0;
        shownTotal += shown;
      });
      empty.hidden = shownTotal !== 0;
    }
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
        apply(btn.getAttribute('data-topic'));
      });
    });
  })();
</script>
