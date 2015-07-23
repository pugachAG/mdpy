from .md_common import MdCommon
from .md_heading import MdHeading
from .md_document_content import MdDocumentContent

class MdDocument:

    CONTENT_TABLE_HEADING_TITLE = 'Table of Contents'

    def __init__(self, name, version=None):
        self.__version = version
        self.__name = name
        self.__content = list()
        self.__content_table = MdDocumentContent()

    def add_heading(self, item, add_content_table=True):
        self.add_content(item)
        if add_content_table:
            self.__content_table.add_item(item, self.__get_level(item))

    def emplace_heading(self, text, level, add_content_table=True):
        self.add_heading(MdHeading(level, text), add_content_table)

    def add_content(self, item):
        self.__content.append(item)

    def save(self, filename):
        with open(filename, "w") as text_file:
            print(self, file=text_file)

    def __str__(self):
        nl = MdCommon.new_line
        name = self.__name
        data = [name + nl + '=' * len(name)]
        if self.__version is not None:
            data.append(self.__version)

        if self.__content_table.all_headings:
            content_table_heading = MdHeading(
                self.__content_table.all_headings[0].level,
                MdDocument.CONTENT_TABLE_HEADING_TITLE)
            data.extend([content_table_heading, self.__content_table])
        data.extend(self.__content)
        return nl.join([str(s) + nl for s in data])

    def __get_level(self, heading):
        headings = self.__content_table.all_headings
        assert (not headings) or (headings[0].level <= heading.level)
        return heading.level - headings[0].level if headings else 0

