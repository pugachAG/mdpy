mdpy
====

### <a name="table_of_contents">Table of Contents</a>

* [Introduction](#introduction)
* [Examples](#examples)
  * [Create document](#create_document)
  * [Heading](#heading)
    * [H5 header example](#h5_header_example)
  * [Table](#table)
  * [List](#list)
  * [Save document](#save_document)
* [Licence](#licence)

### <a name="introduction">Introduction</a>

**mdpy** is simple internal python [domain-specific language](http://martinfowler.com/bliki/DomainSpecificLanguage.html) for generating markdown documents.

### <a name="examples">Examples</a>

#### <a name="create_document">Create document</a>

```python
# create markdown document
doc = MdDocument('mdpy')

```

#### <a name="heading">Heading</a>

##### <a name="h5_header_example">H5 header example</a>

##### <a name="this_one_will_not_be_added_to_the_content_table">This one will not be added to the content table</a>

```python
# add H4 header to the document
# note that this header will be automatically added to the document table of contents  
doc.emplace_heading('H5 header example', 5)
# or you can explicitly specify if you want header to be added to the table of contents
doc.emplace_heading('This one will not be added to the content table', 5, False)

```

#### <a name="table">Table</a>

| Column align center | Column align left | Column align right |
| :-----------------: | :---------------- | -----------------: |
| 1 | To be, or not to be, that is the question | Shakespeare |
| 2 | Wow, such alignment, very left | Doge |

```python
# add table to the document
doc.add_content(
    # table definition
    MdTable(
        # column headers definitions
        ('Column align center', MdTableColumnAlignment.CENTER),
        ('Column align left', MdTableColumnAlignment.LEFT),
        ('Column align right', MdTableColumnAlignment.RIGHT))
        # add table entries (fluent interface)
    .add_entry(1, 'To be, or not to be, that is the question', 'Shakespeare')
    .add_entry(2, 'Wow, such alignment, very left', 'Doge')
)

```

#### <a name="list">List</a>

* List item 1
* The second one
  * Nested list item 1
  * Nested list item 2
* Outer list item 3

```python
# add list to the document
doc.add_content(
    # list definition
    MdList()
    # add list items (fluent interface)
    .add_item('List item 1')
    .add_item('The second one')
    .add_item(
        # nested list definition
        MdList()
        .add_item('Nested list item 1')
        .add_item('Nested list item 2')
    )
    .add_item('Outer list item 3')
)

```

#### <a name="save_document">Save document</a>

```python
# save markdown document as README.md
doc.save('README.md')

```

### <a name="licence">Licence</a>

MIT

