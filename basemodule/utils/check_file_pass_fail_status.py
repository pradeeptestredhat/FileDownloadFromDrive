

class TestResult():
    '''
    This is to check if the test case is pass or fail using size and time
    '''

    @staticmethod
    def test_result(size_on_dick, actual_size):
        if size_on_dick == actual_size:
            print("File Downloaded correctly")
            print("*" * 100)
            print("TEST CASE RESULT:-----   PASS")
        else:
            print("TEST CASE RESULT:-----   FAIL")


    @staticmethod
    def test_result_through_file_present(last_time, present_time):
        if last_time<present_time:
            print("File Downloaded correctly")
            print("*" * 100)
            print("TEST CASE RESULT:-----   PASS")
        else:
            print("TEST CASE RESULT:-----   FAIL")

    @staticmethod
    def comp_result(status):
        if status=="YES":
            print("File Downloaded correctly")
            print("*" * 100)
            print("TEST CASE RESULT:-----   PASS")
        else:
            print("TEST CASE RESULT:-----   FAIL")
