import random
import string
import unittest
import my_list


def random_alphanumeric(size=4):
    if random.randint(0, 1):
        return ''.join(
            random.choices(string.ascii_letters + string.digits, k=size))
    else:
        return random.randint(-2**10, 2**10)


def get_random_list(size=4):
    return [random_alphanumeric() for _ in range(size)]


class ListSampleTest(unittest.TestCase):

    def setUp(self):
        print("Init new test set.")
        self.head = get_random_list(size=1)
        self.data_set = []
        for number in range(2**4):
            self.data_set.append(
                get_random_list(size=number))

    def test_tail_init(self):
        # Тестирование классического конструктора (head, [tail])
        # Проходим по инвертированным данным и
        for data in self.data_set:
            sample = None
            for item in reversed(data):
                sample = my_list.List(item, sample)
            sample = my_list.List(self.head[0], sample)
            if not sample:
                sample = []
            self.assertEqual(
                self.head + list(data), list(sample))

    def test_iter(self):
        # Проходим по стартовому набору и проверяем
        # корректность итератора
        print("Testing iterator.")
        for data in self.data_set:
            sample = my_list.List(self.head[0]) + data
            self.assertEqual(
                self.head + data, list(sample))

    def test_reversed(self):
        print("Testing reverse iterator.")
        for data in self.data_set:
            sample = my_list.List(self.head[0]) + data
            self.assertEqual(
                list(reversed(data)) + self.head, list(reversed(sample)))

    def test_append(self):
        # Каждый список из тестового набора
        # добавим в новый объект List и сравним содержимое
        # c исходными данными
        print("Testing append.")
        for data in self.data_set:
            sample = my_list.List(self.head[0])
            for item in data:
                sample.append(item)
            self.assertEqual(
                self.head + data, list(sample))

    def test_add(self):
        # Для каждого набора тестовых данных
        # проверим корректность выполнения операции +
        # для случаев: obj + [...] и obj + obj,
        # где type(obj) ~ List
        print("Testing add op.")
        for data in self.data_set:
            sample = my_list.List(self.head[0])
            new_sample = sample + data
            self.assertEqual(
                self.head + data, list(new_sample))
            data_list = my_list.List(self.head[0]) + data
            new_sample = sample + data_list
            self.assertEqual(
                self.head + self.head + data, list(new_sample))


if __name__ == '__main__':
    unittest.main()
