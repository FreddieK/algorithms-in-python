

class TwoSum:
    # Assuming sorted array, because lazy...

    @staticmethod
    def _find(value, t, list_):
        sought_value = t - value
        if sought_value == value:
            return False

        sublist = list_
        while len(sublist) > 1:
            mid_point_index = len(sublist)//2
            mid_point = sublist[mid_point_index]
            if mid_point == sought_value:
                return True
            elif mid_point < sought_value:
                sublist = sublist[mid_point_index:]
            elif mid_point > sought_value:
                sublist = sublist[:mid_point_index]

        if sublist[0] == sought_value:
            return True
        return False

    @staticmethod
    def search(t, list_):
        for value in list_:
            if TwoSum._find(value, t, list_):
                return True
        return False

    @staticmethod
    def search_list(search_list, list_):
        return_list = []
        for value in search_list:
            return_list.append(TwoSum.search(value, list_))
        return return_list


class TwoSumHash:
    # In order to speed up performance, utilize Python built-in hashing to get
    # O(n) performance instead of O(nlog(n))

    @staticmethod
    def _find(value, t, set_):
        sought_value = t - value
        if sought_value == value:
            return False
        return sought_value in set_

    @staticmethod
    def search(t, list_):
        for value in list_:
            if TwoSumHash._find(value, t, list_):
                return True
        return False

    @staticmethod
    def search_list(search_list, list_):
        return_list = []
        for value in search_list:
            print(value)
            return_list.append(TwoSumHash.search(value, list_))
        return return_list
