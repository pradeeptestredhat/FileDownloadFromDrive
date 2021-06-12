
class TimeDiff():

    @staticmethod
    def check_time_diff(last_time, present_time):
        '''
        This is to check whether last-time is lesser than present itme or not
        :param last_time:
        :param present_time:
        :return:  True/False boolean
        '''
        if last_time < present_time:
            return True
        else:
            return False
