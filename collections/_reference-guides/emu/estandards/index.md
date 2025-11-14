---
title: Standards
display_title: Standards
section: EMu
status: draft
parent: EMu
toc: true
toc_sticky: true
last_modified_at: 2025-11-14
hash: 39086b70f4652acf6035a39d3ed41183
---

{% assign has_pages = false %}
{% for item in site['reference-guides'] %}
  {% if item.parent == "Standards" %}
    {% assign has_pages = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% if has_pages %}
  <h2>Tabs</h2>
  <ul>
  {% for item in site['reference-guides'] %}
  {% if item.parent == "Standards" %}
    <li><a href="{{ item.url | relative_url }}">{{ item.display_title }}</a></li>
  {% endif %}
  {% endfor %}
  </ul>
{% endif %}