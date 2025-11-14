---
title: Explanations
status: published
nav_order: 3
sidebar:
  nav:
  - sidebar
  collapsible: true
  expanded:
  - explanations
last_modified_at: 2025-09-10
hash: cbdfe44bd79f776e86aa49feee8829b9
---

A landing page for documents explaining a system or process.

<h2>Pages</h2>
<ul>
{% for item in site.explanations %}
{% unless item.parent %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endunless %}
{% endfor %}
</ul>