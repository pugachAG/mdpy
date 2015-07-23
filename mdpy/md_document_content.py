from .md_list import MdList
from .md_heading import MdHeading


class MdDocumentContent:
    def __init__(self):
        self.__data = list()

    def add_item(self, item, level):
        assert isinstance(item, MdHeading)
        assert level >= 0
        self.__data.append((item, level))

    @property
    def all_headings(self):
        return [it[0] for it in self.__data]

    def __str__(self):
        result = MdList()
        cur = result
        prev = dict()
        cur_level = 0
        for item in self.__data:
            lvl = item[1]
            content_str = item[0].link

            if lvl < cur_level:
                cur = prev[cur]
                cur_level = lvl

            if lvl == cur_level:
                cur.add_item(content_str)
            
            if lvl > cur_level:
                nxt = MdList()
                nxt.add_item(content_str)
                prev[nxt] = cur
                cur.add_item(nxt)
                cur = nxt
                cur_level = lvl

        return str(result)

