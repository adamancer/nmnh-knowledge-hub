---
title: Bibliography
display_title: Bibliography
section: EMu
status: draft
parent: EMu
toc: true
toc_sticky: true
highlight_all_terms: true
last_modified_at: 2026-01-08
hash: 9601c7f1533f825c9ac39b768f6d743d
---

{% assign has_pages = false %}
{% for item in site['reference-guides'] %}
  {% if item.parent == "Bibliography" %}
    {% assign has_pages = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% if has_pages %}
  <h2>Tabs</h2>
  <ul>
  {% for item in site['reference-guides'] %}
  {% if item.parent == "Bibliography" %}
    <li><a href="{{ item.url | relative_url }}">{{ item.display_title }}</a></li>
  {% endif %}
  {% endfor %}
  </ul>
{% endif %}