# Your header

import cmpt120image
import random # Import random for distribute_items

cmpt120image.init()

# Note: delete all `return False` lines as you complete each function!

def recolor_image(img, color):
  """
  Changes all non-white pixels to the specified color.
  White pixels [255, 255, 255] remain white.
  """
  height = len(img)
  width = len(img[0])
  new_img = []

  for row in range(height):
    new_row = []
    for col in range(width):
      pixel = img[row][col]
      # Check if pixel is white
      if pixel == [255, 255, 255]:
        new_row.append(pixel)
      else:
        # Replace with the new color
        new_row.append(color)
    new_img.append(new_row)
    
  return new_img

def minify(img):
  """
  Shrinks the image by half in both dimensions by averaging 2x2 blocks.
  """
  height = len(img)
  width = len(img[0])
  new_height = height // 2
  new_width = width // 2
  new_img = []

  for row in range(new_height):
    new_row = []
    for col in range(new_width):
      # Get the 4 pixels from the 2x2 block
      p1 = img[row*2][col*2]
      p2 = img[row*2][col*2+1]
      p3 = img[row*2+1][col*2]
      p4 = img[row*2+1][col*2+1]

      # Calculate average for R, G, and B
      avg_r = (p1[0] + p2[0] + p3[0] + p4[0]) // 4
      avg_g = (p1[1] + p2[1] + p3[1] + p4[1]) // 4
      avg_b = (p1[2] + p2[2] + p3[2] + p4[2]) // 4

      new_row.append([avg_r, avg_g, avg_b])
    new_img.append(new_row)
  
  return new_img
  
def mirror(img):
  """
  Flips the image horizontally (left-to-right).
  """
  height = len(img)
  width = len(img[0])
  new_img = []

  for row in range(height):
    # Copy pixel from the opposite side
    # Using slicing [::-1] is an efficient way to reverse a list in Python
    new_row = img[row][::-1]
    new_img.append(new_row)

  return new_img
  
def draw_item(canvas, item, row, col):
  """
  Draws non-white pixels of item onto canvas at specified position.
  Modifies canvas in-place.
  """
  item_height = len(item)
  item_width = len(item[0])
  canvas_height = len(canvas)
  canvas_width = len(canvas[0])

  for r in range(item_height):
    for c in range(item_width):
      pixel = item[r][c]
      # Only draw non-white pixels
      if pixel != [255, 255, 255]:
        # Calculate target position
        target_row = row + r
        target_col = col + c
        
        # Ensure
