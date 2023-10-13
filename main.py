# Создайте класс Playlist, представляющий плейлист с песнями.
# Переопределите метод __str__, чтобы он выводил список песен
# в читаемом виде, и метод __len__, чтобы можно было узнать
# количество песен в плейлисте.

class Playlist:

    def __init__(self, list_name , author):
        self.list_name = list_name
        self.author = author

    def __len__(self):
        return len(self.list_name)

    def __str__(self):
        print(f'Автор: {self.author}')
        for song in self.list_name:
            print(f'Песня: {song}')
        return ''

list_song = ['Young and Beautiful', 'Radio', 'Summertime Sadness',
             'Born to Die', 'West Coast']

lana_del_rey = Playlist(list_song,'Лана Дель Рей')
print(lana_del_rey)
print(len(lana_del_rey))

# 2)Создайте класс, который будет представлять собой неизменяемый объект,
# и переопределите методы __hash__ и __eq__, чтобы можно было использовать
# его в множествах и как ключи в словарях.
print()
print('*' * 50)
print()



class Hash:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


tom1 = Hash('Tom')
tom2 = Hash('Tom')

print(hash(tom1))
print(hash(tom2))
print(tom1 == tom2)
my_dict = {tom1:'tom1', tom2:'tom2'}
print(my_dict)
print(len(my_dict))
my_set = set([tom1, tom2])
print(my_set)