import operator


def read_file(filename='jobs.txt'):
    """
    :param filename: Optional parameter if filename would be changed
    :return: Tuple of length of list, and then actual list
    """
    path = f'data/{filename}'
    with open(path) as f:
        read_data = f.read()
    lines = [x for x in read_data.split('\n')]
    length = int(lines[0])
    # Shaving of last item in list as it is an empty line
    list_ = [[int(item) for item in line.split()] for line in lines[1:-1]]

    return length, list_


class Scheduling:
    """
    Your task in this problem is to run the greedy algorithm that schedules
    jobs in decreasing order of the difference (weight - length).

    If two jobs have equal difference (weight - length), you should schedule
    the job with higher weight first.

    You should report the sum of weighted completion times of the resulting
    schedule.
    """

    def __init__(self, list_, schedule_by_ratio=False):
        self.jobs = list_
        self.sorted_jobs = None
        self.completion_times = None
        self.schedule_by_ratio = schedule_by_ratio

    def _schedule(self):
        weighted_list = [[x[0], x[1], x[0] - x[1]] for x in self.jobs]
        self.sorted_jobs = sorted(weighted_list, key=operator.itemgetter(2, 0),
                                  reverse=True)

    def _schedule_by_ratio(self):
        """
        Your task now is to run the greedy algorithm that schedules jobs
        (optimally) in decreasing order of the ratio (weight/length).
        """
        weighted_list = [[x[0], x[1], x[0]/x[1]] for x in self.jobs]
        self.sorted_jobs = sorted(weighted_list, key=operator.itemgetter(2, 0),
                                  reverse=True)

    def get_run_order(self):
        if self.sorted_jobs is None:
            raise Exception('Jobs have not been scheduled')
        return [[x[0], x[1]] for x in self.sorted_jobs]

    def run_jobs(self):
        if self.schedule_by_ratio:
            self._schedule_by_ratio()
        else:
            self._schedule()
        global_completion_time = 0
        completion_times = []

        for job in self.sorted_jobs:
            global_completion_time += job[1]
            completion_times.append(global_completion_time)

        self.completion_times = completion_times

    def get_weighted_completion_time(self):
        if self.completion_times is None:
            raise Exception('Jobs have not been run')

        weighted_completion_time = 0
        for index, item in enumerate(self.sorted_jobs):
            weighted_completion_time += self.completion_times[index]*item[0]

        return weighted_completion_time
