class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # -----------------------------------------
        # STEP 1: Find the search range
        # -----------------------------------------

        # The capacity cannot be smaller than the
        # heaviest single package.
        left = max(weights)

        # The capacity cannot need to be larger than
        # the total weight of all packages.
        # With this capacity, everything can go in 1 day.
        right = sum(weights)

        # -----------------------------------------
        # STEP 2: Binary Search on the capacity
        # -----------------------------------------

        while left < right:

            # Try this capacity
            capacity = left + (right - left) // 2

            # -----------------------------------------
            # STEP 3: Check how many days are needed
            # with this capacity
            # -----------------------------------------

            days_used = 1
            current_weight = 0

            # Process packages in their given order
            for weight in weights:

                # If adding this package would make
                # the ship too heavy, start a new day.
                if current_weight + weight > capacity:

                    days_used += 1

                    # Start the new day with no weight
                    current_weight = 0

                # Put the current package on the ship
                current_weight += weight

            # -----------------------------------------
            # STEP 4: Decide which side to search
            # -----------------------------------------

            if days_used <= days:

                # This capacity works.
                # But we want the MINIMUM capacity,
                # so try smaller values.
                right = capacity

            else:

                # This capacity is too small.
                # We need more capacity.
                left = capacity + 1

        # When left == right, we have found
        # the minimum capacity that works.
        return left