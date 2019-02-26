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
        print("Init new test set")
        self.data_set = []
        for number in range(1, 2**4):
            self.data_set.append(
                get_random_list(size=number))

    def test_append(self):
        # Каждый список из тестового набора
        # добавим в новый объект List и сравним содержимое
        # c исходными данными
        print("Testing append.")
        for data in self.data_set:
            head = get_random_list(size=1)
            sample = my_list.List(head[0])
            for item in data:
                sample.append(item)
            self.assertEqual(
                head + data, list(sample))

    def test_copy(self):
        # Cоздадим копии объекта sample несколько раз
        # и посмотрим, изменяется ли при изменении
        # копии новых элеменетов исходный объект
        # Так же проверим цельность первоначального списка
        print("Testing copy.")
        for data in self.data_set:
            head = get_random_list(size=1)
            sample = my_list.List(head[0])
            for item in data:
                sample.append(item)
            self.assertEqual(
                head + data, list(sample))
            for i in range(1, 2**5):
                new_data = random.choice(self.data_set)
                new_sample = sample.copy()
                self.assertEqual(
                    head + data, list(new_sample))
                for item in new_data:
                    new_sample.append(item)
                self.assertEqual(
                    head + data + new_data, list(new_sample))
                self.assertEqual(
                    head + data, list(sample))


if __name__ == '__main__':
    unittest.main()
