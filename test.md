---
title: Test
description: Test widgets defined in the knowledge hub template
status: draft
nav_order: 1
sidebar:
  nav:
  - sidebar
  collapsible: true
  expanded:
  - community
contributors:
- Adam Mansur
tags:
- invalid
last_modified_at: 2025-11-14
hash: 4de22b5a8b7922e73fa9d28564893027
---

This paragraph includes a term defined manually in the glossaries/custom.yml file, {% include glossary term="Custom Term" namespace="" %}. It also includes a term with a {% include glossary term="Custom Acronym" namespace="" %}.

This is a paragraph includes a Darwin Core terms, like {% include glossary term="collectionID" namespace="dwc" %} and {% include glossary term="datasetID" namespace="dwc" %}. Those terms should display as links to the Darwin Core Quick Reference Guide and should show a definition on hover. Only the first appearance of a term on each page should include the tooltip, so dwc:collectionID in this sentence should appear as plain text. Note that terms do not use a widget or any other syntax. The script that builds the page identifies them automatically.

Here are some items that should not include tooltips:

- # dwc:institutionID
- [dwc:digitalSpecimenID](#link)
- <a href="#top">dwc:geologicalContextID</a>

But these should: 

- {% include glossary term="institutionID" namespace="dwc" %}
- {% include glossary term="digitalSpecimenID" namespace="dwc" %}
- {% include glossary term="geologicalContextID" namespace="dwc" %}

## Notices

{: .notice}
Created with `{: .notice}`

{: .notice--info}
Created with `{: .notice--info}`

{: .notice--warning}
Created with `{: .notice--warning}`

{: .notice--danger}
Created with `{: .notice--danger}`

{: .notice--tip}
Created with `{: .notice--tip}`

{% include resource_list tags='symbiota' %}

{% include resource_list tags='geography|georeference' %}

{% include resource_list tags='geography|georeference|data wrangling' %}