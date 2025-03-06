from typing import List

def fetchProcessIndices(robots: List[int]) -> List[int]:
    num_robots = len(robots)

    # Dealing with empty list
    if robots == []:
        return []

    # Dealing with a list with only one element
    elif num_robots == 1:
        return [1]
    
    else:
        # Creating a list with the robots sorted in descending order + their index in i+1 (count, index)
        sorted_robots = []
        for i in range(num_robots):
            sorted_robots.append((robots[i], i+1))
        sorted_robots.sort(reverse=True)

        # Helper variables
        survivors = []
        strongest = sorted_robots[0][0]
        total_robots = 0

        # Looping through the sorted robots list
        counter = 0
        for idx, (count, index) in enumerate(sorted_robots):
            
            # if a given element is bigger than the strongest, it is a survivor.
            if count >= strongest:
                survivors.append(index)
                counter += 1
                continue

            # This loop compares the elements from itself to the smaller.    
            broke_out = False
            for i in range(counter, num_robots):

                # preventing self-comparison
                if i == idx:
                    continue

                # Losing the comparison
                if count < sorted_robots[i][0]:
                    continue
                
                # Comparison 
                if count >= sorted_robots[i][0]:
                    total_robots += count
                    if total_robots >= strongest:
                        survivors.append(index)
                        counter += 1
                        broke_out = True
                        break
            
            # If the element didnt broke the previous loop, we compare it with the remaining elements (the ones that were previously bigger than itself)
            if not broke_out:
                for i in range(counter -1, -1, -1):

                    # preventing self-comparison
                    if i == idx:
                        continue

                    # Losing the comparison
                    if count < sorted_robots[i][0]:
                        continue
                    
                    # Comparison
                    if count >= sorted_robots[i][0]:
                        total_robots += count
                        if total_robots >= strongest:
                            survivors.append(index)
                            counter += 1
                            break

        # sort and return the survivors.
        output = sorted(survivors)
        return output

if __name__ == "__main__":
    pass