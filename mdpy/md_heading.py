class MdHeading:

    def __init__(self, level, title):
        self.__level = level
        self.__title = title

    @property
    def title(self):
        return self.__title

    @property
    def level(self):
        return self.__level

    @property
    def name_key(self):
        return MdHeading.get_name_key(self.__title)

    @property
    def link(self):
        return MdHeading.create_link(self.__title)

    def __str__(self):
        return self.__level * '#' + ' <a name=\"' + self.name_key + '\">' + self.__title + '</a>'

    @staticmethod
    def create_link(title):
        return "[{0}](#{1})".format(title, MdHeading.get_name_key(title))

    @staticmethod
    def get_name_key(title):
        return title.lower().replace(' ', '_')

