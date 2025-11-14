---
title: EMu
status: draft
tags:
- template
- api
last_modified_at: 2025-09-10
hash: ec27f901a39e134d5d830ec5ae8d02f0
---

A landing page for an API reference guide

<h2>Modules</h2>
<ul>
{% for item in site["reference-guides"] %}
{% if item.parent == "EMu" %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
