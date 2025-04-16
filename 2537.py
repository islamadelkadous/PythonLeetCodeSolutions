from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Initialize a counter to track the count of each number
        num_counter = Counter()
        # Initialize the result and current sum and the starting index
        result = current_sum = start_index = 0
      
        # Iterate over the list of numbers
        for num in nums:
            # Update the current sum with the number of times we have seen the current number
            current_sum += num_counter[num]
            # Increment the count of the current number in the counter
            num_counter[num] += 1
          
            # If the current sum exceeds the limit, adjust the window from the left
            while current_sum - num_counter[nums[start_index]] + 1 >= k:
                # Decrease the count of the starting number
                num_counter[nums[start_index]] -= 1
                # Deduct the excess from the current sum
                current_sum -= num_counter[nums[start_index]]
                # Move the starting index to the right
                start_index += 1
          
            # If the current sum meets the requirement, count the subarrays
            if current_sum >= k:
                result += start_index + 1
              
        # Return the total count of "good" subarrays
        return result
