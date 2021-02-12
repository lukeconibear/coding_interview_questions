class Solution:
    def class_photos(self, red_shirt_heights, blue_shirt_heights): # time O(nlgn), space O(1)
        red_shirt_heights.sort(reverse=True) # tallest person first
        blue_shirt_heights.sort(reverse=True) # tallest person first
        back_row_colour = 'BLUE' if blue_shirt_heights[0] > red_shirt_heights[0] else 'RED'
        for index in range(len(blue_shirt_heights)):
            if back_row_colour == 'BLUE':
                if blue_shirt_heights[index] <= red_shirt_heights[index]:
                    return False
            else:
                if red_shirt_heights[index] <= blue_shirt_heights[index]:
                    return False

        return True
