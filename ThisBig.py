"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can cl canvas.create_rectangle(ick the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    # Makes our rectangle centered at (CENTER_X, CENTER_Y)!
    # Since we draw starting at the left-most x and top-most y,
    # we need to take however big our square is (THIS_BIG)
    # and put half of it to the left and above the center, and the other
    # half to the right and below the center.
    
   
    size = THIS_BIG
    left_x = CENTER_X - size / 2 # Put half of the square to the left of CENTER_X
    top_y = CENTER_Y - size / 2  # Put half of the square above CENTER_Y
    right_x = CENTER_X + size / 2  # Put half of the square to the right of CENTER_X
    bottom_y = CENTER_Y + size / 2    # Put half of the square below CENTER_Y
    
 
    
    # Draw the square
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    
	

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()