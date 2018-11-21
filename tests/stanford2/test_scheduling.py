import unittest
from algorithms.stanford2.scheduling import *


class TestScheduling(unittest.TestCase):

    def test_can_read_file(self):
        length, list_ = read_file()
        self.assertEqual(length, 10000)
        self.assertEqual(len(list_), 10000)
        self.assertEqual(list_[0], [8, 50])

    def test_schedules_according_to_weighted_priority(self):
        list_ = [
            [5, 5],
            [3, 1],
            [10, 5]
        ]
        jobs = Scheduling(list_)
        jobs._schedule()
        run_order = jobs.get_run_order()
        self.assertEqual(run_order, [[10, 5],
                                     [3, 1],
                                     [5, 5]])

    def test_schedules_according_to_priority_when_tied(self):
        list_ = [
            [1, 2],
            [2, 3],
            [3, 4]
        ]
        jobs = Scheduling(list_)
        jobs._schedule()
        run_order = jobs.get_run_order()
        self.assertEqual(run_order, [[3, 4],
                                     [2, 3],
                                     [1, 2]])

    def test_running_jobs(self):
        list_ = [
            [1, 2],
            [2, 3],
            [3, 4]
        ]
        jobs = Scheduling(list_)
        jobs.run_jobs()
        weighted_completion_time = jobs.get_weighted_completion_time()
        self.assertEqual(weighted_completion_time, 4*3 + 7*2 + 9*1)

        list_ = [
            [5, 5],
            [3, 1],
            [10, 5]
        ]
        jobs = Scheduling(list_)
        jobs.run_jobs()
        weighted_completion_time = jobs.get_weighted_completion_time()
        self.assertEqual(weighted_completion_time,  5*10 + 6*3 + 11*5)

    @unittest.skip
    def test_with_full_data(self):
        length, list_ = read_file()
        jobs = Scheduling(list_)
        jobs.run_jobs()
        total_completion_time = jobs.get_weighted_completion_time()
        print(total_completion_time)

    def test_schedules_according_to_weighted_priority_by_ratio(self):
        list_ = [
            [5, 5],
            [3, 1],
            [10, 5]
        ]
        jobs = Scheduling(list_)
        jobs._schedule_by_ratio()
        run_order = jobs.get_run_order()
        self.assertEqual(run_order, [[3, 1],
                                     [10, 5],
                                     [5, 5]])

    def test_running_jobs_by_ratio(self):
        list_ = [
            [5, 5],
            [3, 1],
            [10, 5]
        ]
        jobs = Scheduling(list_, schedule_by_ratio=True)
        jobs.run_jobs()
        weighted_completion_time = jobs.get_weighted_completion_time()
        self.assertEqual(weighted_completion_time, 3*1 + 10*6 + 5*11)

    @unittest.skip
    def test_with_full_data(self):
        length, list_ = read_file()
        jobs = Scheduling(list_, schedule_by_ratio=True)
        jobs.run_jobs()
        total_completion_time = jobs.get_weighted_completion_time()
        print(total_completion_time)