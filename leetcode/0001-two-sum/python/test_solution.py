from solution import Solution


class TestTwoSum:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1: nums = [2,7,11,15], target = 9
        Expected output: [0,1]
        """
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)

        assert sorted(result) == [0, 1]
        assert nums[result[0]] + nums[result[1]] == target

    def test_example_2(self):
        """
        Example 2: nums = [3,2,4], target = 6
        Expected output: [1,2]
        """
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)

        assert sorted(result) == [1, 2]
        assert nums[result[0]] + nums[result[1]] == target

    def test_example_3(self):
        """
        Example 3: nums = [3,3], target = 6
        Expected output: [0,1]
        """
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)

        assert sorted(result) == [0, 1]
        assert nums[result[0]] + nums[result[1]] == target
