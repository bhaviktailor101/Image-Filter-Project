""" SYSC 1005 A Fall 2014 Lab 4 - Part 3.
"""

from Cimpl import *

#--------------------------------------
# This function was presented in class:

def grayscale(img):
    """
    Convert the specified picture into a grayscale image.
    """

    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)

def negative(img):
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        r = 255 - r
        g = 255 - g
        b = 255 - b
        
        col = create_color(r, g, b)
        set_color(img, x, y, col) 
        
def weighted_grayscale(img):
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        brightness = (r * 0.299) + (g * 0.587) + (b * 0.114)
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)
        
#---------------------------------------------------------------
# A filter that uses three if statements to check every pixel's
# red, green and blue components, individually.

def solarize(img, threshold):
    """
    Solarize the specified image.
    """

    for x, y, col in img:

        # Invert the values of all RGB components less than 128,
        # leaving components with higher values unchanged.

        red, green, blue = col

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)


#--------------------------------------
# A filter that uses an if-else statement.

def black_and_white(img):
    """
    Convert the specified image to a black-and-white (two-tone) image.
    """

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on whether
    # its brightness is in the lower or upper half of this range.

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3
        if brightness < 128:
            set_color(img, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(img, x, y, white)


#--------------------------------------
# A filter that uses an if-elif-else statement.

def black_and_white_and_gray(img):
    """
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, col in img:
        red, green, blue = col
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

def extreme_contrast(img):
    
    for x, y, col in img:
        red, green, blue = col

        if red < 128:
            red = 0
        else:     
            red = 255
        if green < 128:
            green = 0
        else:     
            green = 255        
        if blue < 128:
            blue = 0
        else:     
            blue = 255 
        
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        

def sepia_tint(img):
    grayscale(img)
    for x, y, col in img:
        red, green, blue = col
            
        if red < 63:
            blue = blue * 0.9
            red = red * 1.1
        elif red < 191:
            blue = blue * 0.85
            red = red * 1.15
        else: 
            blue = blue * 0.93
            red = red * 1.08
            
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        
def _adjust_component(amount):
    
        if amount < 64:
            amount = 31
        elif amount < 128:
            amount = 95
        elif amount < 192:
            amount = 159
        else:
            amount = 223
        return amount

def posterize(img):
    for x, y, col in img:
        red, green, blue = col
        red = _adjust_component(red)
        green = _adjust_component(green)
        blue = _adjust_component(blue)
        
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        
def simplify(img):
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    set_red = create_color(255, 0, 0)
    set_green = create_color(0, 255, 0)
    set_blue = create_color(0, 0, 255)
    for x, y, col in img:
        red, green, blue = col
        if red > 200 and blue > 200 and green > 200:
            set_color(img, x, y, black)
        elif red < 50 and blue < 50 and green < 50:
            set_color(img, x, y, white)
        elif red > green and red > blue:
            set_color(img, x, y, set_red)
        elif green > red and green > blue:
            set_color(img, x, y, set_green)
        else:
            set_color(img, x, y, set_blue)
    

def detect_edges(img, threshold):
    # Generate pixels of x and y for img
    

    height = get_height(img)
    width = get_width(img)
    
    for y in range(height - 1):
        for x in range(width):
            
            top_red, top_green, top_blue= get_color(img, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
            avg_top = (top_red + top_green + top_blue)//3
            avg_bottom = (bottom_red + bottom_green + bottom_blue)//3
            
            if abs(avg_top - avg_bottom) > threshold:
                black = create_color(0, 0, 0)
                set_color(img, x, y, black)
            else:
                white = create_color(255, 255, 255)
                set_color(img, x, y, white)
            
def detect_edges_better(img, threshold):
    # Generate pixels of x and y for img
    

    height = get_height(img)
    width = get_width(img)
    
    for y in range(height - 1):
        for x in range(width - 1):
            
            top_red, top_green, top_blue= get_color(img, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
            right_red, right_green, right_blue = get_color(img, x + 1, y)
            avg_top = (top_red + top_green + top_blue)//3
            avg_bottom = (bottom_red + bottom_green + bottom_blue)//3
            avg_right = (right_red + right_green + right_blue)//3
            
            if abs(avg_top - avg_bottom) or abs(avg_top - avg_right) > threshold:
                black = create_color(0, 0, 0)
                set_color(img, x, y, black)
            else:
                white = create_color(255, 255, 255)
                set_color(img, x, y, white)


def blur(source):
    """
    Return a new image that is a blurred copy of the image bound to source.
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Notice the arguments passed to range(). We don't want to modify the
    # pixels at the image's edges.

    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):
            
            sum_red = 0
            sum_blue = 0
            sum_green = 0
            
            for b in range(y - 1, y + 2):
                for a in range(x - 1, x+2):
                    red, green, blue = get_color(source, a, b)
                
                    sum_red += red
                    sum_green += green
                    sum_blue += blue
                

            # Average the red components of the five pixels
            new_red = sum_red//9

            # Average the green components of the five pixels
            new_green = sum_green//9

            # Average the blue components of the five pixels
            new_blue = sum_blue//9

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target

def flip(img):
    height = get_height(img)
    width = get_width(img)
    for y in range(0, height):
        for x in range(0, width//2):
            pixel_one = get_color(img, x, y)
            pixel_two = get_color(img, width-x-1, y)
            set_color(img, x, y, pixel_two)
            set_color(img, width-x-1, y, pixel_one)
            
        