---
title: Bibliography.Reference (1)
display_title: Reference (1)
section: EMu
status: draft
parent: Bibliography
toc: true
toc_sticky: true
highlight_all_terms: true
last_modified_at: 2026-01-08
hash: 8f856659aa18f84246e2d7df7ba22a6b
---

<p>This tab includes fields that are widely used across different publication types.</p>
<h2 id="publication_type">Publication Type</h2>
<p>Identifies what type of work is being cited. This allows users to filter by publication type and allows the client to generate summary data and citation strings.</p>
<ul class="tdwg">
<li><a href="#RefPublicationType">Type</a></li>
<li><a href="#RefPublicationSubtype">Subtype</a></li>
</ul>
<h3 class="tdwg" id="RefPublicationType">Type</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The type of work</p></td></tr>
<tr><th>Column</th><td><p>RefPublicationType</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required</p></td></tr>
<tr><th>Comments</th><td><p>Used to determine the formatting for citation strings and summary data.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Article</span></li>
<li><span class="term">Book</span></li>
<li><span class="term">Book Series</span></li>
<li><span class="term">Catalogue</span></li>
<li><span class="term">Chapter</span></li>
<li><span class="term">Citation</span></li>
<li><span class="term">Electronic</span></li>
<li><span class="term">Field Trip Guide</span></li>
<li><span class="term">Journal</span></li>
<li><span class="term">Manuscript</span></li>
<li><span class="term">Other</span></li>
<li><span class="term">Thesis</span></li>
<li><span class="term">Web Site</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefPublicationSubtype">Subtype</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The subtype of work</p></td></tr>
<tr><th>Column</th><td><p>RefPublicationSubtype</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required for citations</p></td></tr>
<tr><th>Comments</th><td><p>Used for Citation and Thesis records. For citations, the subtype should match one of the values for Publication Type. For theses, the subtype should indicate the level of degree (like bachelors, masters, or PhD). Some bibliography data standards retain this distinction, for example, BibTex.</p></td></tr>
</table>

<h2 id="manuscript">Manuscript?</h2>
<ul class="tdwg">
<li><a href="#RefManuscript">Manuscript</a></li>
</ul>
<h3 class="tdwg" id="RefManuscript">Manuscript</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Whether the work is a manuscript, that is, an unpublished work or a pre-publication version of a work that was ultimately published</p></td></tr>
<tr><th>Column</th><td><p>RefManuscript</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p>Consider including it if the pre-publication version is attached to the record.</p></td></tr>
</table>

<h2 id="publication_details">Publication Details</h2>
<p>Includes metata fields like title and author that are required for almost all publications.</p>
<ul class="tdwg">
<li><a href="#RefSeriesTitle">Series Title</a></li>
<li><a href="#RefJournalBookTitle">Journal/Book Title</a></li>
<li><a href="#RefTitle">Article/Resource Title</a></li>
<li><a href="#RefAbbreviatedTitle">Abbreviated Title</a></li>
<li><a href="#RefContributorsRef_tab">Authors/Contributors</a></li>
<li><a href="#RefContributorsRole_tab">Role</a></li>
<li><a href="#RefDate">Date</a></li>
<li><a href="#RefDateRange">Date Range</a></li>
<li><a href="#RefPublisherRef">Publisher</a></li>
<li><a href="#RefPublicationCity">Publication City</a></li>
<li><a href="#RefLanguage">Language</a></li>
</ul>
<h3 class="tdwg" id="RefSeriesTitle">Series Title</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The name of the book series in which a book appears</p></td></tr>
<tr><th>Column</th><td><p>RefSeriesTitle</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required for books that are part of a series</p></td></tr>
<tr><th>Comments</th><td><p>Series of scientific monographs are the most common book series in NMNH data. Do not use for journal or periodical titles, which should use emu:RefJournalBookTitle instead.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Open-File Report</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefJournalBookTitle">Journal/Book Title</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The name of the journal (for articles) or book (for books or chapters) in which the work appears</p></td></tr>
<tr><th>Column</th><td><p>RefJournalBookTitle</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required for articles, books, and chapters</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Science</span></li>
<li><span class="term">Proceedings of the National Academy of Sciences</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefTitle">Article/Resource Title</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The title of the work</p></td></tr>
<tr><th>Column</th><td><p>RefTitle</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required except for books</p></td></tr>
<tr><th>Comments</th><td><p>The title should be recorded as close to verbatim as possible. Omit for books, which should use emu:RefJournalBookTitle instead.</p></td></tr>
</table>

<h3 class="tdwg" id="RefAbbreviatedTitle">Abbreviated Title</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The abbreviated title of a journal</p></td></tr>
<tr><th>Column</th><td><p>RefAbbreviatedTitle</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p>Some common citation formats require an abbreviated title and will be incorrect if this field is not populated. Journal abbreviations must follow the ISO 4 standard. The ISSN International Center provides standardized abbreviations based on this standard through the <a href="https://www.issn.org/services/online-services/access-to-the-ltwa/">List of Title Word Abbreviations</a>.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Sci.</span></li>
<li><span class="term">Proc. Nat. Acad. Sci.</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefContributorsRef_tab">Authors/Contributors</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The authors (for most works) and editors (for books or chapters) of the work</p></td></tr>
<tr><th>Column</th><td><p>RefContributorsRef_tab</p></td></tr>
<tr><th>Format</th><td><p>Attachment to eparties</p></td></tr>
<tr><th>Required</th><td><p>Required</p></td></tr>
<tr><th>Comments</th><td><p>Both authors and book editors appear in common citation formats and should be included. Contributors with a less direct relationship to an individual work and that are not included in common citation formats (like journal editors) should be omitted.</p></td></tr>
</table>

<h3 class="tdwg" id="RefContributorsRole_tab">Role</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The role of a contributor in creating the work</p></td></tr>
<tr><th>Column</th><td><p>RefContributorsRole_tab</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required for each populated row</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Author</span></li>
<li><span class="term">Editor</span></li>
</ul></td></tr>
<tr><th>Notes</th><td><ul class="examples">
<li><strong>Mineral Sciences</strong>: Many authors and editors are not affilaited with the collection beyond their appereance in a Bibliography record. Set the emu:SecRecordStatus = Unlisted on those records to exclude them from default searches of the Parties module.</li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefDate">Date</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The date of publication or, for regularly updated works like websites, the last modified date</p></td></tr>
<tr><th>Column</th><td><p>RefDate</p></td></tr>
<tr><th>Format</th><td><p>A date in a format recognized by EMu</p></td></tr>
<tr><th>Required</th><td><p>Required</p></td></tr>
<tr><th>Comments</th><td><p>For most works, this will be the original publication date. For websites and other regularly updated works, it should be the last modified date at the time the resouce was accessed.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">1970-01-01</span></li>
<li><span class="term">1 Jan 1970</span></li>
<li><span class="term">Jan 1970</span></li>
<li><span class="term">1970</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefDateRange">Date Range</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The verbatim date of publication</p></td></tr>
<tr><th>Column</th><td><p>RefDateRange</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Required</p></td></tr>
<tr><th>Comments</th><td><p>For most works, this will be the original publication date. For websites and other regularly updated works, this should be the last modified date at the time the resouce was accessed. </p>
<p>Dates should omit trailing letters used to differentiate publications by the same author in the same year <em>unless</em> the record has limited metadata (for example, only author and year). In this case, the trailing letter can be retained until the record can be fleshed out.</p></td></tr>
</table>

<h3 class="tdwg" id="RefPublisherRef">Publisher</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The entity that published a book</p></td></tr>
<tr><th>Column</th><td><p>RefPublisherRef</p></td></tr>
<tr><th>Format</th><td><p>Attachment to eparties</p></td></tr>
<tr><th>Required</th><td><p>Required for books</p></td></tr>
</table>

<h3 class="tdwg" id="RefPublicationCity">Publication City</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The city in which the publisher is located</p></td></tr>
<tr><th>Column</th><td><p>RefPublicationCity</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Required</th><td><p>Required for books</p></td></tr>
<tr><th>Comments</th><td><p>For American cities, include the city and state code. For cities in other countries, include the city and country name.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Tokyo, Japan</span></li>
<li><span class="term">Washington, DC</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RefLanguage">Language</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The primary language of the work</p></td></tr>
<tr><th>Column</th><td><p>RefLanguage</p></td></tr>
<tr><th>Format</th><td><p>Uncontrolled picklist</p></td></tr>
<tr><th>Comments</th><td><p>Use the full name of the language. For multilingual works, specify the primary language.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">English</span></li>
<li><span class="term">Spanish</span></li>
</ul></td></tr>
</table>

<h2 id="citation_text">Citation Text</h2>
<ul class="tdwg">
<li><a href="#RefCitationText">Citation Text</a></li>
</ul>
<h3 class="tdwg" id="RefCitationText">Citation Text</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>A snippet of text from the work</p></td></tr>
<tr><th>Column</th><td><p>RefCitationText</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p>In addition to one or more snippets, this field may include the pages, figures, or plates in which relevant informationis cited.</p></td></tr>
</table>

<h2 id="data_provider">Data Provider</h2>
<p>Information about the provenance of the data in the record</p>
<ul class="tdwg">
<li><a href="#RefDataSource">Source</a></li>
<li><a href="#RefDataProvider">Provider</a></li>
</ul>
<h3 class="tdwg" id="RefDataSource">Source</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The kind of data provider</p></td></tr>
<tr><th>Column</th><td><p>RefDataSource</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p><strong>Consider deprecating.</strong> Potentially out of scope for typical use of this module.</p></td></tr>
</table>

<h3 class="tdwg" id="RefDataProvider">Provider</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The source that provided the data</p></td></tr>
<tr><th>Column</th><td><p>RefDataProvider</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Comments</th><td><p><strong>Consider deprecating.</strong> Potentially out of scope for typical use of this module.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Biodiversity Heritage Library</span></li>
<li><span class="term">Crossref</span></li>
</ul></td></tr>
</table>


{% assign has_pages = false %}
{% for item in site['reference-guides'] %}
  {% if item.parent == "Bibliography.Reference (1)" %}
    {% assign has_pages = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% if has_pages %}
  <h2>Pages</h2>
  <ul>
  {% for item in site['reference-guides'] %}
  {% if item.parent == "Bibliography.Reference (1)" %}
    <li><a href="{{ item.url | relative_url }}">{{ item.display_title }}</a></li>
  {% endif %}
  {% endfor %}
  </ul>
{% endif %}