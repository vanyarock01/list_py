import random
import string
import unittest
import my_list


def random_alphanumeric(size=4):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))


def get_random_list(size=4):
    return [random.randint(-2**10, 2**10) for _ in range(size)]


class ListAverageTest(unittest.TestCase):

    def setUp(self):
        print("Init new test set.")
        self.data_set = []
        for number in range(2**4):
            self.data_set.append(
                get_random_list(size=number))

    def test_iter(self):
        print("Testing iterator.")
        for data in self.data_set:
            sample = my_list.List() + data
            self.assertEqual(
                data, list(sample))

    def test_append(self):
        # Каждый список из тестового набора
        # добавим в новый объект List и сравним содержимое
        # c исходными данными
        print("Testing append.")
        for data in self.data_set:
            sample = my_list.List()
            for item in data:
                sample.append(item)
            self.assertEqual(
                data, list(sample))

    def test_copy(self):
        # Cоздадим копии объекта sample несколько раз
        # и посмотрим, изменяется ли при изменении
        # копии новых элеменетов исходный объект
        # Так же проверим цельность первоначального списка
        print("Testing copy.")
        for data in self.data_set:
            sample = my_list.List()
            sample += data
            self.assertEqual(
                data, list(sample))
            for i in range(1, 2**5):
                new_data = random.choice(self.data_set)
                new_sample = sample.copy()
                self.assertEqual(
                    data, list(new_sample))
                new_sample += new_data
                self.assertEqual(
                    data + new_data, list(new_sample))
                self.assertEqual(
                    data, list(sample))

    def test_add(self):
        # Для каждого набора тестовых данных
        # проверим корректность выполнения операции +
        # для случаев: obj + [...] и obj + obj,
        # где type(obj) ~ List
        print("Testing add op.")
        for data in self.data_set:
            sample = my_list.List()
            new_sample = sample + data
            self.assertEqual(
                data, list(new_sample))
            data_list = my_list.List() + data
            new_sample = sample + data_list
            self.assertEqual(
                data, list(new_sample))


if __name__ == '__main__':
    unittest.main()
