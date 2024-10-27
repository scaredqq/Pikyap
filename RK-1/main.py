class SyntaxStructure:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ProgrammingLanguage:
    def __init__(self, id, name, syntax_structure_id):
        self.id = id
        self.name = name
        self.syntax_structure_id = syntax_structure_id

class LanguageStructureMapping:
    def __init__(self, language_id, structure_id):
        self.language_id = language_id
        self.structure_id = structure_id


# Синтаксические конструкции
structures = [
    SyntaxStructure(1, "Условный оператор"),
    SyntaxStructure(2, "Цикл"),
    SyntaxStructure(3, "Функция"),
]

# Языки программирования
languages = [
    ProgrammingLanguage(1, "Python", 1),
    ProgrammingLanguage(2, "Python", 2),
    ProgrammingLanguage(3, "Java", 3),
    ProgrammingLanguage(4, "C++", 1),
    ProgrammingLanguage(5, "JavaScript", 2),
]

# Связи между языками и синтаксическими конструкциями
mappings = [
    LanguageStructureMapping(1, 1),
    LanguageStructureMapping(1, 2),
    LanguageStructureMapping(2, 3),
    LanguageStructureMapping(3, 1),
    LanguageStructureMapping(4, 1),
    LanguageStructureMapping(5, 2),
]

# Запрос 1: Выводим языки, которые используют синтаксическую конструкцию с названием, заканчивающимся на "ый"
def get_languages_by_structure_suffix(structures, languages):
    suffix = "ый"
    return [
        (language.name, structure.name)
        for language in languages
        for structure in structures
        if structure.id == language.syntax_structure_id and structure.name.endswith(suffix)
    ]

# Запрос 2: Выводим среднюю зарплату (в данном случае количество языков) по синтаксическим конструкциям
def average_languages_per_structure(structures, languages):
    structure_count = {structure.id: 0 for structure in structures}
    
    for language in languages:
        structure_count[language.syntax_structure_id] += 1

    return sorted(
        [(structure.name, count) for structure, count in zip(structures, structure_count.values())],
        key=lambda x: x[1]
    )

# Запрос 3: Языки, которые имеют синтаксическую конструкцию, название которой начинается на "У"
def get_languages_by_structure_prefix(structures, languages):
    prefix = "У"
    return [
        (language.name, structure.name)
        for language in languages
        for structure in structures
        if structure.id == language.syntax_structure_id and structure.name.startswith(prefix)
    ]

# Запрос 1
print("Языки с конструкциями, заканчивающимися на 'ый':")
for lang, struct in get_languages_by_structure_suffix(structures, languages):
    print(f"Язык: {lang}, Конструкция: {struct}")

# Запрос 2
print("\nСреднее количество языков по синтаксическим конструкциям (отсортировано):")
for struct, count in average_languages_per_structure(structures, languages):
    print(f"Конструкция: {struct}, Количество языков: {count}")

# Запрос 3
print("\nЯзыки с конструкциями, начинающимися на 'У':")
for lang, struct in get_languages_by_structure_prefix(structures, languages):
    print(f"Язык: {lang}, Конструкция: {struct}")
