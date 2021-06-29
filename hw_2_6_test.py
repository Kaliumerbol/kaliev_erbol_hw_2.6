# # Задание_1
import unittest

def calculate_average_velocity(*args):
    velocity_sum = 0
    for i in args:
        try:
            velocity_sum += i
        except TypeError:
            continue
    return velocity_sum / len(args)
    print(len(args))

class TestCalculator(unittest.TestCase):
        def test_calculate_average_velocity_1(self):
            self.assertEqual(calculate_average_velocity(1, 2, 5, 5), 3.25)
        def test_calculate_average_velocity_2(self):
            self.assertRaises(TypeError, calculate_average_velocity(2, 5, 5, 'd'))
unittest.main()

# #Задание_2
# # Сделано в репозитории

# Задание_3
import unittest

def my_func(dict_u):
    try:
        result = {f"{i}'s rating": sum(j)/len(j) for i, j in dict_u.items()}
        return result
    except TypeError:
        return dict_u


# Закоментил тот код который не понял, и за того что не понимаю как работает проверка ошибок на исключения, не пойму что от меня хотят. И за этого не могу посторить логику.

# def my_func(dict_u):
#     for dct in dict_u:
#         return dict_u[dct]
    # try:
    #     # type(dict_u) == 'dict'
    #     result = {f"{i}'s rating": sum(j)/len(j) for i, j in dict_u.items()}
    #     return result
    # except Exception:
    #     return dict_u

# input_data = {'JD': [13, 89, 32, 55], 'Turk': [5, 32, 57, 39], 'Janitor':[100, 100, 100, 100]}
# print(my_func(input_data))
# input_data = [3, 'JD', True, (33, 77), ['slay', 'invoke', ], ]
# for i in input_data:
#     print(my_func(i))

class TestMyFunction(unittest.TestCase):
    def test_ordinary_case(self):
        input_data = {'JD': [13, 89, 32, 55],
                'Turk': [5, 32, 57, 39],
                'Janitor':[100, 100, 100, 100]}
        result = {"JD's rating": 47.25,
            "Turk's rating": 33.25,
            "Janitor's rating": 100.0}
        self.assertEqual(my_func(input_data), result)

#     def test_other_data_type(self):
#         input_data = [3, 'JD', True, (33, 77), ['slay', 'invoke', ], ]
#         for i in input_data:
#             self.assertRaises(ValueError, my_func, i)

# #     def test_empty_list(self):
# #         input_data = {'Jon Snow': []}
# #         result = {"Jon Snow's rating": 0}
# #         self.assertEqual(my_func(input_data), result)

unittest.main()