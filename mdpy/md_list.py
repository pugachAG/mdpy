from .md_common import MdCommon


class MdList:
    def __init__(self):
        self.__items = list()

    def add_item(self, item):
        self.__items.append(item)

    def __str__(self):
        star = '*'
        space = ' '
        two_spaces = 2 * space
        res = list()
        for it in self.__items:
            if isinstance(it, MdList):
                res.extend((two_spaces + ln) for ln in str(it).split(MdCommon.new_line))
            else:
                res.append(star + space + str(it))

        return MdCommon.new_line.join(res)



