---
layout: page
title: Projects
permalink: /projects/
description: Research projects currently open in our group. We welcome motivated students and researchers interested in joining these efforts.
nav: true
nav_order: 2
horizontal: false
---

<p class="projects-intro">Interested in a project? Open it to find who to contact, or see <a href="{{ '/join/' | relative_url }}">Join us</a>.</p>

<!-- pages/projects.md: one full-width row per project, grouped by category -->
<div class="projects project-rows">
{%- if site.enable_project_categories and page.display_categories %}
  {%- for category in page.display_categories %}
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- if categorized_projects.size > 0 %}
  <h2 class="category">{{ category }}</h2>
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  {%- for project in sorted_projects %}
    {%- assign flip = forloop.index0 | modulo: 2 %}
    {%- if flip == 1 %}{% assign flip = true %}{% else %}{% assign flip = false %}{% endif %}
    {% include projects_row.html %}
  {%- endfor %}
  {%- endif %}
  {%- endfor %}
{%- else -%}
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
  {%- for project in sorted_projects %}
    {%- assign flip = forloop.index0 | modulo: 2 %}
    {%- if flip == 1 %}{% assign flip = true %}{% else %}{% assign flip = false %}{% endif %}
    {% include projects_row.html %}
  {%- endfor %}
{%- endif %}
</div>
