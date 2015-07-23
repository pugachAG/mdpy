from .md_common import MdCommon


class MdTableColumnAlignment:
    LEFT = 1
    RIGHT = 2
    CENTER = 3


class MdTable:
    def __init__(self, *columns):
        self.__column_names = list(columns)
        self.__data = list()

    def add_entry(self, *values):
        assert len(values) == len(self.__column_names)
        self.__data.append([str(x) for x in values])
        return self

    def __str__(self):
        res = list()
        res.append(MdTable.__format_row([x[0] for x in self.__column_names]))
        res.append(self.__get_separator_row())
        for entry in self.__data:
            res.append(MdTable.__format_row(entry))
        return MdCommon.new_line.join(res)

    def __get_separator_row(self):
        data = [MdTable.__get_column_dashes(it) for it in self.__column_names]
        return MdTable.__format_row(data)

    @staticmethod
    def __get_column_dashes(entry):
        result = list('-' * len(entry[0]))
        if entry[1] & MdTableColumnAlignment.LEFT == MdTableColumnAlignment.LEFT:
            result[0] = ':'
        if entry[1] & MdTableColumnAlignment.RIGHT == MdTableColumnAlignment.RIGHT:
            result[-1] = ':'
        return ''.join(result)

    @staticmethod
    def __format_row(data):
        sep = ' | '
        return sep[1:] + sep.join(data) + sep[:-1]



