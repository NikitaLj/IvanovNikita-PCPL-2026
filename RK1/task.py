from operator import itemgetter


class Lib:
    def __init__(self, id, name, downloads, lang_id):
        self.id = id
        self.name = name
        self.downloads = downloads
        self.lang_id = lang_id


class Lang:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibLang:
    def __init__(self, lang_id, lib_id):
        self.lang_id = lang_id
        self.lib_id = lib_id


langs = [
    Lang(1, 'Python'),
    Lang(2, 'Java'),
    Lang(3, 'Ассемблер'),
    Lang(4, 'Ада'),
    Lang(5, 'JavaScript'),
]

libs = [
    Lib(1, 'NumPy', 300, 1),
    Lib(2, 'Protocol Buffers', 120, 1),
    Lib(3, 'Spring', 250, 2),
    Lib(4, 'Irvine32', 15, 3),
    Lib(5, 'GNAT Components', 8, 4),
]

libs_langs = [
    LibLang(1, 1),
    LibLang(1, 2),
    LibLang(2, 2),
    LibLang(2, 3),
    LibLang(3, 4),
    LibLang(4, 5),
    LibLang(5, 2),
]


def main():
    one_to_many = [(lib.name, lib.downloads, lang.name)
                   for lang in langs
                   for lib in libs
                   if lib.lang_id == lang.id]

    temp = [(lang.name, link.lang_id, link.lib_id)
            for lang in langs
            for link in libs_langs
            if lang.id == link.lang_id]

    many_to_many = [(lib.name, lib.downloads, lang_name)
                    for lang_name, lang_id, lib_id in temp
                    for lib in libs if lib.id == lib_id]

    print('Задание Г1')
    res_1 = {}
    for lang in langs:
        if lang.name.startswith('А'):
            lang_libs = list(filter(lambda row: row[2] == lang.name, one_to_many))
            names = [name for name, _, _ in lang_libs]
            res_1[lang.name] = names
    print(res_1)

    print('\nЗадание Г2')
    unsorted = []
    for lang in langs:
        lang_libs = list(filter(lambda row: row[2] == lang.name, one_to_many))
        if len(lang_libs) > 0:
            downloads = [d for _, d, _ in lang_libs]
            unsorted.append((lang.name, max(downloads)))
    res_2 = sorted(unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Г3')
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == '__main__':
    main()