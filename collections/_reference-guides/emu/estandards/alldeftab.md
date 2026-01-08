---
title: Standards.Definition
display_title: Definition
section: EMu
status: draft
parent: Standards
toc: true
toc_sticky: true
highlight_all_terms: true
last_modified_at: 2026-01-08
hash: 1f152f3c3e428e11be3cf6044115113f
---

<p>Constructs a definition for a standard. Visible when {% include glossary term="RecordType" namespace="emu" %} = "Term Definition".</p>
<h2 id="standard_name">Standard Name</h2>
<ul class="tdwg">
<li><a href="#RecordType">Record Type</a></li>
<li><a href="#StandardName">Standard Name</a></li>
<li><a href="#ModuleInsert">Module</a></li>
<li><a href="#StandardVersion">Version</a></li>
<li><a href="#Status">Status</a></li>
</ul>
<h3 class="tdwg" id="RecordType">Record Type</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Used to define whether the record is of type "Term Definition" or "Standard".</p></td></tr>
<tr><th>Column</th><td><p>RecordType</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Standard</span></li>
<li><span class="term">Term Definition</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="StandardName">Standard Name</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The name of the standard the definition applies to.</p></td></tr>
<tr><th>Column</th><td><p>StandardName</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Comments</th><td><p>Standards must be preloaded into the Standard Name lookup list before they can be selected here.</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Darwin Core</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="ModuleInsert">Module</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The name of the module storing the required data.</p></td></tr>
<tr><th>Column</th><td><p>ModuleInsert</p></td></tr>
<tr><th>Format</th><td><p>System picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
</table>

<h3 class="tdwg" id="StandardVersion">Version</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The version of the standard the definition is compliant with.</p></td></tr>
<tr><th>Column</th><td><p>StandardVersion</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
</table>

<h3 class="tdwg" id="Status">Status</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Indicates whether the term is active, and hence should be included in the export of a standard.</p></td></tr>
<tr><th>Column</th><td><p>Status</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Pending</span></li>
<li><span class="term">Retired</span></li>
</ul></td></tr>
</table>

<h2 id="definition">Definition</h2>
<ul class="tdwg">
<li><a href="#Term">Term</a></li>
<li><a href="#TermURI">Term URI/IRI</a></li>
<li><a href="#FormatSpecifier">Format Specifier</a></li>
</ul>
<h3 class="tdwg" id="Term">Term</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The name of the term within the standard. The value entered into this field must be unique.</p></td></tr>
<tr><th>Column</th><td><p>Term</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Comments</th><td><p>Terms must be preloaded into the Standard Name lookup list before they can be selected here.</p></td></tr>
</table>

<h3 class="tdwg" id="TermURI">Term URI/IRI</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The URI of a resource comprising a definition of the term.</p></td></tr>
<tr><th>Column</th><td><p>TermURI</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
</table>

<h3 class="tdwg" id="FormatSpecifier">Format Specifier</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Defines whether the term is to be formatted using the Term Format String or a Script.</p></td></tr>
<tr><th>Column</th><td><p>FormatSpecifier</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Script</span></li>
<li><span class="term">String</span></li>
</ul></td></tr>
</table>

<h2 id="nested_modifiers">Nested Modifiers</h2>
<ul class="tdwg">
<li><a href="#CollapseEmptyValues">Collapse Empty Values?</a></li>
<li><a href="#RemoveDuplicateValues">Remove Duplicate Values?</a></li>
<li><a href="#NestedSeparator_tab">Nested Separator</a></li>
</ul>
<h3 class="tdwg" id="CollapseEmptyValues">Collapse Empty Values?</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Where field values are empty, this defines whether their corresponding separator should be dropped.</p></td></tr>
<tr><th>Column</th><td><p>CollapseEmptyValues</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">No</span></li>
<li><span class="term">Yes</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="RemoveDuplicateValues">Remove Duplicate Values?</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Where the same field value appears more than once, this defines whether to remove duplicates.</p></td></tr>
<tr><th>Column</th><td><p>RemoveDuplicateValues</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">No</span></li>
<li><span class="term">Yes</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="NestedSeparator_tab">Nested Separator</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Where nested tables are used to generate the data for this definition, the separator to use between each of the generated rows. If no value is specified the separator will default to the pipe character.</p></td></tr>
<tr><th>Column</th><td><p>NestedSeparator_tab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>No</p></td></tr>
</table>

<h2 id="term_format_string">Term Format String</h2>
<ul class="tdwg">
<li><a href="#TermFormatString">Term Format String</a></li>
</ul>
<h3 class="tdwg" id="TermFormatString">Term Format String</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>A string allowing custom formatting of output. This format string uses same syntax as the "Perl" printf statement.</p></td></tr>
<tr><th>Column</th><td><p>TermFormatString</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Comments</th><td><ul class="examples">
<li>Format a float with one decimal place: <code>%.1f</code></li>
<li>Zero-pad a value to three characers: <code>%03d</code></li>
</ul></td></tr>
</table>

<h2 id="definition_details">Definition Details</h2>
<ul class="tdwg">
<li><a href="#Field_tab">Field</a></li>
<li><a href="#Format_tab">Format</a></li>
<li><a href="#DefinedTerm_tab">Defined Term</a></li>
<li><a href="#RowInclusion_tab">Row Inclusion</a></li>
<li><a href="#FormatSeparator_tab">Format Separator</a></li>
<li><a href="#TypeOfWhere">Type Of Where</a></li>
<li><a href="#WhereOperator">Operator</a></li>
</ul>
<h3 class="tdwg" id="Field_tab">Field</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The EMu field from which the data is extracted to generate this term.</p></td></tr>
<tr><th>Column</th><td><p>Field_tab</p></td></tr>
<tr><th>Format</th><td><p>Field Picker picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
</table>

<h3 class="tdwg" id="Format_tab">Format</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Allows selection of a predefined reformatting function to be applied to the data, such as titlecase or date reformatting.</p></td></tr>
<tr><th>Column</th><td><p>Format_tab</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Lowercase</span></li>
<li><span class="term">Titlecase</span></li>
<li><span class="term">Uppercase</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="DefinedTerm_tab">Defined Term</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Allows a term previously defined in a standard to be used in constructing this term.</p></td></tr>
<tr><th>Column</th><td><p>DefinedTerm_tab</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
</table>

<h3 class="tdwg" id="RowInclusion_tab">Row Inclusion</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Defines which row(s) to include when the field is a nested table.</p></td></tr>
<tr><th>Column</th><td><p>RowInclusion_tab</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">All Rows</span></li>
<li><span class="term">First Row</span></li>
<li><span class="term">Last Row</span></li>
<li><span class="term">Where All</span></li>
<li><span class="term">Where First</span></li>
<li><span class="term">Where Last</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="FormatSeparator_tab">Format Separator</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Where more than one field is used in a definition, this defines the text to be used to join this field with the previous. If no value is specified the separator will default to the space character.</p></td></tr>
<tr><th>Column</th><td><p>FormatSeparator_tab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
</table>

<h3 class="tdwg" id="TypeOfWhere">Type Of Where</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Defines how the Where rules are applied. Allows selection of a row from a double nested table.</p></td></tr>
<tr><th>Column</th><td><p>TypeOfWhere</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>Yes</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Boolean</span></li>
<li><span class="term">Group Row Select</span></li>
<li><span class="term">Row Select</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="WhereOperator">Operator</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>Defines whether to combine where clauses with an AND or an OR.</p></td></tr>
<tr><th>Column</th><td><p>WhereOperator</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>No</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">AND</span></li>
<li><span class="term">OR</span></li>
</ul></td></tr>
</table>

<h2 id="where_details">Where Details</h2>
<p>Used to select which rows within a table are used when constructing the definition</p>
<ul class="tdwg">
<li><a href="#WhereField_nesttab">Field</a></li>
<li><a href="#WhereValue_nesttab">Value</a></li>
<li><a href="#WhereCondition_nesttab">Condition</a></li>
<li><a href="#WhereBetweenValue_nesttab">Between Value</a></li>
</ul>
<h3 class="tdwg" id="WhereField_nesttab">Field</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The EMu field to search to choose a table row.</p></td></tr>
<tr><th>Column</th><td><p>WhereField_nesttab</p></td></tr>
<tr><th>Format</th><td><p>Field Picker picklist</p></td></tr>
<tr><th>Required</th><td><p>No</p></td></tr>
</table>

<h3 class="tdwg" id="WhereValue_nesttab">Value</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The value to test against the condition. If the {% include glossary term="WhereCondition_nesttab" namespace="emu" %} is Between, this is the lower bound.</p></td></tr>
<tr><th>Column</th><td><p>WhereValue_nesttab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>No</p></td></tr>
</table>

<h3 class="tdwg" id="WhereCondition_nesttab">Condition</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>The condition to be used to match the table row.</p></td></tr>
<tr><th>Column</th><td><p>WhereCondition_nesttab</p></td></tr>
<tr><th>Format</th><td><p>Controlled picklist</p></td></tr>
<tr><th>Required</th><td><p>No</p></td></tr>
<tr><th>Examples</th><td><ul class="examples">
<li><span class="term">Between</span></li>
<li><span class="term">Contains</span></li>
<li><span class="term">Does Not Equal</span></li>
<li><span class="term">Does Not Contain</span></li>
<li><span class="term">Equals</span></li>
<li><span class="term">Greater Than</span></li>
<li><span class="term">Is Not Null</span></li>
<li><span class="term">Is Null</span></li>
<li><span class="term">Less Than</span></li>
</ul></td></tr>
</table>

<h3 class="tdwg" id="WhereBetweenValue_nesttab">Between Value</h3>
<table class="tdwg">
<tr><th>Definition</th><td><p>If the {% include glossary term="WhereCondition_nesttab" namespace="emu" %} is Between, the upper bound of the between comparison.</p></td></tr>
<tr><th>Column</th><td><p>WhereBetweenValue_nesttab</p></td></tr>
<tr><th>Format</th><td><p>Text</p></td></tr>
<tr><th>Required</th><td><p>No</p></td></tr>
</table>


{% assign has_pages = false %}
{% for item in site['reference-guides'] %}
  {% if item.parent == "Standards.Definition" %}
    {% assign has_pages = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% if has_pages %}
  <h2>Pages</h2>
  <ul>
  {% for item in site['reference-guides'] %}
  {% if item.parent == "Standards.Definition" %}
    <li><a href="{{ item.url | relative_url }}">{{ item.display_title }}</a></li>
  {% endif %}
  {% endfor %}
  </ul>
{% endif %}