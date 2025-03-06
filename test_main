import unittest, time
from main import fetchProcessIndices

class TestMain(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment"""
        pass

    def test_empty_input(self):
        """Test if the function doesnt crash when given an empty input."""
        self.assertEqual(fetchProcessIndices([]), [], f"The output should be an empty array.")

    def test_single_process(self):
        """Only one process should always survive."""
        self.assertEqual(fetchProcessIndices([10]), [1], f"The output should be [1].")

    def test_two_processes_different_robots(self):
        """The process with more robots should win."""
        self.assertEqual(fetchProcessIndices([3, 7]), [2], f"The output should be [2].")
        self.assertEqual(fetchProcessIndices([7, 3]), [1], f"The output should be [1].")

    def test_two_processes_same_robots(self):
        """Either process could win, both should be in the result."""
        self.assertEqual(fetchProcessIndices([5, 5]), [1, 2], f"The output should be [1,2].")

    def test_multiple_processes_unique_winner(self):
        """Test with multiple possible survivors"""
        self.assertEqual(fetchProcessIndices([1, 3, 2, 10, 4]), [2,3,4,5], f"The output should be [2,3,4,5].")

    def test_large_numbers(self):
        """Test if the function can handle large numbers."""
        self.assertEqual(fetchProcessIndices([10**9, 10**9, 10**9, 10**9, 10**9]), [1, 2, 3, 4, 5], f"The output should be [1,2,3,4,5].")

    def test_ascending_order(self):
        """Test with increasing robot counts."""
        self.assertEqual(fetchProcessIndices([1, 2, 3, 4, 5, 6]), [2,3,4,5,6], f"The output should be [2,3,4,5,6].")

    def test_large_input_size(self):
        """Test if the function runs in under 10 seconds with max constraints."""
        n = 2 * 10**5
        robots = [1] * n  # All processes start with the same number of robots

        start_time = time.time()
        result = fetchProcessIndices(robots)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.4f} seconds")

        self.assertLess(execution_time, 10, f"Function took too long: {execution_time:.4f} seconds")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)