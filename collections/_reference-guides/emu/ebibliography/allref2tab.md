---
title: Bibliography.Reference (2)
display_title: Reference (2)
section: EMu
status: draft
parent: Bibliography
toc: true
toc_sticky: true
highlight_all_terms: true
last_modified_at: 2026-01-08
hash: ec823a5af8020f0718acdb4d270b5101
---

<p>This tab includes fields specific to different publication types, for example, volume and issue for journals and the URL for websites. Most records will need some but not all of these fields.</p>
<h2 id="reference_details">Reference Details</h2>
<p>Additional information to identify and describe publications. Unlike Publication Details, each field is used by only a subset of the available publication types.</p>
<ul class="tdwg">
<li><a href="#RefChapter">Chapter</a></li>
<li><a href="#RefVolume">Volume</a></li>
<li><a href="#RefEdition">Edition</a></li>
<li><a href="#RefIssue">Issue</a></li>
<li><a href="#RefFormat">Format</a></li>
<li><a href="#RefPages">Pages</a></li>
<li><a href="#RefPage">Page</a></li>
<li><a href="#RefFiguresPlates">Figures/Plates</a></li>
<li><a href="#RefScale">Scale</a></li>
<li><a href="#RefSeries">Series</a></li>
</ul>
<h3 class="tdwg" id="RefChapter">Chapter</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The chapter number</p></td></tr>
<tr><th>Column</th><td><p>RefChapter</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p><strong>Consider deprecating.</strong> Rarely used (n=118). Chapter number can be included in emu:RefTitle if needed.</p></td></tr>
</table>

<h3 class="tdwg" id="RefVolume">Volume</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The volume of a journal in which an article appears</p></td></tr>
<tr><th>Column</th><td><p>RefVolume</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for articles</p></td></tr>
</table>

<h3 class="tdwg" id="RefEdition">Edition</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The edition of a book</p></td></tr>
<tr><th>Column</th><td><p>RefEdition</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p>Express the edition as an ordinal (1st, 2nd, 3rd, etc.)</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">2nd</span></li>
<li><span class="term">3rd</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefIssue">Issue</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The issue of a journal in which an article appears</p></td></tr>
<tr><th>Column</th><td><p>RefIssue</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for articles</p></td></tr>
</table>

<h3 class="tdwg" id="RefFormat">Format</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefFormat</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
</table>

<h3 class="tdwg" id="RefPages">Pages</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The page range (for a chapter or article) or number of pages (for a book)</p></td></tr>
<tr><th>Column</th><td><p>RefPages</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p>Citations of paged works should include both emu:RefPages (for the parent publication) and emu:RefPage (to specify the exact citation). Page ranges for articles and chapters should omit page signifiers (p., pp., etc.)</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">123-136</span> (article or chaper)</li>
<li><span class="term">246 p.</span> (book)</li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefPage">Page</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The page or pages cited from within the larger work</p></td></tr>
<tr><th>Column</th><td><p>RefPage</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for citations</p></td></tr>
<tr><th>Comments</th><td><p>Citations of paged works should include both emu:RefPages (for the parent publication) and emu:RefPage (to specify the exact citation).</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">2</span></li>
<li><span class="term">16-17</span></li>
<li><span class="term">4-5, 7, 10-12</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefFiguresPlates">Figures/Plates</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefFiguresPlates</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
</table>

<h3 class="tdwg" id="RefScale">Scale</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The ratio of the distance on a map to actual distance</p></td></tr>
<tr><th>Column</th><td><p>RefScale</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for maps</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">1:24,000</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefSeries">Series</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefSeries</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p><strong>Suggest deprecating.</strong> Rarely used (n=2). Not clear what this field is for.</p></td></tr>
</table>

<h2 id="website_details">Website Details</h2>
<p>Information about a website</p>
<ul class="tdwg">
<li><a href="#RefWebSiteIdentifier">Website Identifier</a></li>
<li><a href="#RefLastAccessDate">Last Access Date</a></li>
</ul>
<h3 class="tdwg" id="RefWebSiteIdentifier">Website Identifier</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The URL used to access a website</p></td></tr>
<tr><th>Column</th><td><p>RefWebSiteIdentifier</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for websites</p></td></tr>
<tr><th>Comments</th><td><p>Use the complete URL</p></td></tr>
</table>

<h3 class="tdwg" id="RefLastAccessDate">Last Access Date</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The date on which the website was last accessed</p></td></tr>
<tr><th>Column</th><td><p>RefLastAccessDate</p></td></tr>
<tr><th>Format</th><td><p>A date in a format recognized by EMu</p></td></tr>
<tr><th>Required</th><td><p>Required for websites</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">1970-01-01</span></li>
<li><span class="term">1 Jan 1970</span></li>
<li><span class="term">Jan 1970</span></li>
<li><span class="term">1970</span></li>
</ul></td></tr>
</table>

<h2 id="other_identifiers">Other Identifiers</h2>
<p>Captures identifiers for the work, like the ISBN for a book. Resolvable identifiers, like DOIs or handles, should be recorded in the GUID table on the Admin tab.</p>
<ul class="tdwg">
<li><a href="#RefOtherIdentifierSource_tab">Source</a></li>
<li><a href="#RefOtherIdentifier_tab">Value</a></li>
</ul>
<h3 class="tdwg" id="RefOtherIdentifierSource_tab">Source</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The type of a book or journal identifier, like an ISBN or ISSN</p></td></tr>
<tr><th>Column</th><td><p>RefOtherIdentifierSource_tab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for each populated row</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">ISBN</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefOtherIdentifier_tab">Value</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The identifier for a book or journal, like an ISSN or ISBN</p></td></tr>
<tr><th>Column</th><td><p>RefOtherIdentifier_tab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required for each populated row</p></td></tr>
<tr><th>Comments</th><td><p>Because the ISBN uniquely identifies a book and appears in some citation formats, it should be included if known. ISSNs can be omitted.</p>
<p>DOIs are persistent, resolvable identifiers and should be recorded in emu:AdmGUIDValue_tab.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">0520268776</span> (ISBN 10)</li>
<li><span class="term">978-0520268777</span> (ISBN 13)</li>
</ul></td></tr>
</table>

<h2 id="subject_keywords">Subject/Keywords</h2>
<ul class="tdwg">
<li><a href="#RefKeywords_tab">Subject/Keywords</a></li>
</ul>
<h3 class="tdwg" id="RefKeywords_tab">Subject/Keywords</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefKeywords_tab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p><strong>Suggest deprecating.</strong> Not used.</p></td></tr>
</table>

<h2 id="rights">Rights</h2>
<ul class="tdwg">
<li><a href="#RefRightsRef">Rights</a></li>
</ul>
<h3 class="tdwg" id="RefRightsRef">Rights</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefRightsRef</p></td></tr>
<tr><th>Format</th><td><p>Attachment to erights</p></td></tr>
<tr><th>Comments</th><td><p><strong>Suggest deprecating.</strong> Not used.</p></td></tr>
</table>

<h2 id="location">Location</h2>
<ul class="tdwg">
<li><a href="#RefLocationRef">Location</a></li>
</ul>
<h3 class="tdwg" id="RefLocationRef">Location</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefLocationRef</p></td></tr>
<tr><th>Format</th><td><p>Attachment to elocations</p></td></tr>
<tr><th>Comments</th><td><p><strong>Suggest deprecating.</strong> Not used.</p></td></tr>
</table>

<h2 id="project">Project</h2>
<ul class="tdwg">
<li><a href="#RefProject_tab">Project</a></li>
</ul>
<h3 class="tdwg" id="RefProject_tab">Project</h3>
<table class="tdwg">
<tr><th>Column</th><td><p>RefProject_tab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p><strong>Suggest deprecating.</strong> Not used.</p></td></tr>
</table>


{% assign has_pages = false %}
{% for item in site['reference-guides'] %}
  {% if item.parent == "Bibliography.Reference (2)" %}
    {% assign has_pages = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% if has_pages %}
  <h2>Pages</h2>
  <ul>
  {% for item in site['reference-guides'] %}
  {% if item.parent == "Bibliography.Reference (2)" %}
    <li><a href="{{ item.url | relative_url }}">{{ item.display_title }}</a></li>
  {% endif %}
  {% endfor %}
  </ul>
{% endif %}