import unittest
import Task


class TaskTest(unittest.TestCase):
    def test_create_task(self):
        """Объект Task должен инициализироваться только с именем"""
        try:
            task = Task.Task("Новая задача")
        except:
            self.fail("Не удалось инициализировать объект Task")

    def test_cost_point_set(self):
        """Стоимость выполнения можно переназначить"""
        new_cost_point = 30
        task = Task.Task("Новая задача")
        task.set_cost_point(new_cost_point)
        self.assertEqual(new_cost_point, task.get_cost_point())