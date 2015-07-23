import inspect
from mdpy.md_table import *
from mdpy.md_list import *
from mdpy.md_document import *
from mdpy.md_common import *

TOP_HEADING_LEVEL = 3
LICENCE = 'MIT'
FILE_NAME = 'README.md'


def format_source_code(code):
    return """```python
{0}
```""".format(code)


class CodeCaptureHelper:
    def __init__(self):
        self.__begin = self.__end = -1

    def capture_begin(self):
        self.__begin = CodeCaptureHelper.__get_lineno()

    def capture_end(self):
        self.__end = CodeCaptureHelper.__get_lineno()

    @property
    def captured_code(self):
        cur_module = inspect.getmodule(CodeCaptureHelper)
        all_lines = inspect.getsourcelines(cur_module)[0]
        first_line = all_lines[self.__begin]
        indent_length = len(first_line) - len(first_line.lstrip())
        return ''.join([s[indent_length:] for s in all_lines[self.__begin: self.__end - 1]])

    @staticmethod
    def __get_lineno():
        return inspect.currentframe().f_back.f_back.f_lineno


if __name__ == '__main__':
    capt = CodeCaptureHelper()
    capt.capture_begin()
    # create markdown document
    doc = MdDocument('mdpy')
    capt.capture_end()

    # intro paragraph
    doc.emplace_heading('Introduction', TOP_HEADING_LEVEL)
    doc.add_content('**mdpy** is simple internal python [domain-specific language](http://martinfowler.com/bliki/DomainSpecificLanguage.html) for generating markdown documents.')
    # markdown usage examples
    doc.emplace_heading('Examples', TOP_HEADING_LEVEL)

    # markdown document example
    doc.emplace_heading('Create document', TOP_HEADING_LEVEL + 1)
    doc.add_content(format_source_code(capt.captured_code))

    # markdown heading example
    doc.emplace_heading('Heading', TOP_HEADING_LEVEL + 1)
    capt.capture_begin()
    # add H4 header to the document
    # note that this header will be automatically added to the document table of contents  
    doc.emplace_heading('H5 header example', 5)
    # or you can explicitly specify if you want header to be added to the table of contents
    doc.emplace_heading('This one will not be added to the table of contents', 5, False)
    capt.capture_end()
    # add heading example code
    doc.add_content(format_source_code(capt.captured_code))

    # markdown table example
    doc.emplace_heading('Table', TOP_HEADING_LEVEL + 1)
    capt.capture_begin()
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
    capt.capture_end()
    # add  table example code
    doc.add_content(format_source_code(capt.captured_code))

    # markdown list example
    doc.emplace_heading('List', TOP_HEADING_LEVEL + 1)
    capt.capture_begin()
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
    capt.capture_end()
    # add  list example code
    doc.add_content(format_source_code(capt.captured_code))

    # save document example
    doc.emplace_heading('Save document', TOP_HEADING_LEVEL + 1)
    capt.capture_begin()
    # save markdown document as README.md
    doc.save('README.md')
    capt.capture_end()
    # add save document example code
    doc.add_content(format_source_code(capt.captured_code))

    # add licence
    doc.emplace_heading('Licence', TOP_HEADING_LEVEL)
    doc.add_content(LICENCE)

    # save document
    doc.save(FILE_NAME)


