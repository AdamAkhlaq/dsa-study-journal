from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_case_1_positive_palindrome(self):
        """Test case 1: x = 121, expected output = True"""
        result = self.solution.isPalindrome(121)
        assert result

    def test_case_2_negative_number(self):
        """Test case 2: x = -121, expected output = False"""
        result = self.solution.isPalindrome(-121)
        assert not result

    def test_case_3_not_palindrome(self):
        """Test case 3: x = 10, expected output = False"""
        result = self.solution.isPalindrome(10)
        assert not result
