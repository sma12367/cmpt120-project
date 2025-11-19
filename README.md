# CMPT 120 Project: Blackfoot Language Learning App

## Table of Contents
- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Submission 1: Image Processing Module](#submission-1-image-processing-module-due-nov-22)
- [Submission 2: Complete Application](#submission-2-complete-application-due-dec-1)
- [File Organization](#file-organization)
- [Development Tips](#development-tips)
- [FAQ](#faq)
- [Attributions](#attributions)

---

## About the Project

In this project, you will develop an audio-visual Language Learning app for the Indigenous language, **Blackfoot**. This app helps users associate word sounds to objects like apples, child, tipi, etc.

This project is based on collaboration between previous CMPT 120 instructors and Dr. Eldon Yellowhorn in the Indigenous Studies Department, and the Peigan Board of Education in Lethbridge, Alberta. Note: Prof. Vincent was not involved in the original development of this project -- reach out if you want to connect with the original team!

**Working in Pairs**: You may work solo or with one partner. If working with a partner, both members must join the same Canvas group.

---

## Getting Started

### Prerequisites
- Python 3.x
- Pygame library
- NumPy library

### Initial Setup

**1. Test Your Environment**

First, run `test_basics.py` to verify your machine has all required packages:
```bash
python test_basics.py
```
or
```bash
python3 test_basics.py
```

If you encounter errors, see the [FAQ](#faq) section or consult an instructor.

**2. Environment Selection**

When you run the main application, you'll be asked which environment you're using:
- **v** for VS Code
- **r** for Replit
- **i** for IDLE

Most likely you're using VS Code (or maybe IDLE); Replit is a relic from a previous semester but still technically supported.

### Running Your Code

For best results, run your code from the terminal:
```bash
python main.py
```

or 

```bash
python3 main.py
```

This makes it easier to position windows and see Pygame image displays.

---

## Project Structure

```
project/
├── blackfoot.csv          # List of words (apples, bread, burger, etc.)
├── cmpt120image.py        # Provided image helper functions (DO NOT MODIFY)
├── draw.py                # YOUR CODE: Image processing functions
├── main.py                # YOUR CODE: Main application
├── test_basics.py         # Test script for setup verification
├── images/                # PNG files for each word
│   ├── apples.png
│   ├── bread.png
│   └── ...
└── sounds/                # WAV audio files for each word
    ├── apples.wav
    ├── bread.wav
    └── ...
```

---

## Part 1: Image Processing Module

### Overview
Create a module called `draw.py` with 5 image processing functions. Use the provided starter file as your template.

### Required Functions

#### 1. `recolor_image(img, color)`
- **Purpose**: Changes all non-white pixels to the specified color
- **Parameters**:
  - `img`: 2D array of RGB pixels
  - `color`: List of 3 integers [R, G, B], each 0-255
- **Returns**: New image with recolored pixels
- **Important**: White pixels ([255, 255, 255]) remain white

#### 2. `minify(img)`
- **Purpose**: Shrinks the image by half in both dimensions
- **Parameters**:
  - `img`: 2D array of RGB pixels (assumes even dimensions)
- **Returns**: New image at half size
- **Algorithm**: Average each 2x2 block of pixels
  - Example: `result[0][0]` = average of `original[0][0]`, `original[0][1]`, `original[1][0]`, `original[1][1]`

#### 3. `mirror(img)`
- **Purpose**: Flips the image horizontally (left-to-right)
- **Parameters**:
  - `img`: 2D array of RGB pixels
- **Returns**: New mirrored image

#### 4. `draw_item(canvas, item, row, col)`
- **Purpose**: Draws non-white pixels of `item` onto `canvas` at specified position
- **Parameters**:
  - `canvas`: 2D array of RGB pixels (modified in place)
  - `item`: 2D array of RGB pixels to draw
  - `row`: Top row position where item should be placed
  - `col`: Left column position where item should be placed
- **Returns**: None (modifies canvas directly)
- **Important**: Only non-white pixels are drawn; white pixels are transparent

#### 5. `distribute_items(canvas, item, n)`
- **Purpose**: Draws the item `n` times at random locations on canvas
- **Parameters**:
  - `canvas`: 2D array of RGB pixels (modified in place)
  - `item`: 2D array of RGB pixels to draw
  - `n`: Number of times to draw the item
- **Returns**: None (modifies canvas directly)
- **Note**: Overlapping is allowed
- **Hint**: Consider calling `draw_item()` inside this function

### Helper Functions to Use
Use these functions from `cmpt120image.py`:
- `get_image(filename)` - Load an image (e.g., `"images/apples.png"`)
- `get_black_image(width, height)` - Create a black canvas
- `get_white_image(width, height)` - Create a white canvas
- `show_image(pixels)` - Display an image
- `save_image(pixels, filename)` - Save an image

### Testing Your Functions
For functions 4 and 5, create a test canvas:
```python
canvas = cmpt120image.get_white_image(400, 300)  # 400 width x 300 height
```

### What to Submit
- File named `draw.py` containing all 5 functions

---

## Part 2

### Overview
Create a complete Blackfoot Language Learning application with three modes: Learn, Play, and Settings.

### Application Structure

#### Main Menu
The app displays a menu with options:
1. Learn
2. Play
3. Settings
4. Quit

#### Mode 1: Learn
- Displays images and plays audio for words
- User presses Enter to continue to next word
- Default: First 3 words from `blackfoot.csv`
- Number of words can be changed in Settings

**Behavior**:
1. Load the first `n` words from CSV (default n=3)
2. For each word:
   - Display the image randomly on a white canvas (400w x 300h)
   - Play the corresponding audio file
   - Wait for user to press Enter
   - Continue to next word

#### Mode 2: Play (Seek-and-Count Game)
A game where users listen to a word and count how many times it appears in a mixed image.

**Game Flow**:
1. Ask user how many rounds to play
2. For each round:
   - Create a **challenge list** of 3 randomly selected words (from words being learned)
   - Ensure no word repeats in the challenge list (use `random.sample()`)
   - Randomly select one word as the **"spoken word"**
   - For each of the 3 words in the challenge list:
     - Choose random number `n` between 1 and 4 (how many times to display)
     - Choose random color (from hardcoded list or random RGB values)
     - Apply recolor transformation
     - Randomly decide to minify (or not)
     - Randomly decide to mirror (or not)
     - Draw `n` copies with all transformations applied
   - Display the combined canvas
   - Play audio for the spoken word
   - Ask user to count how many of the spoken word they see
   - Inform if answer is correct or incorrect
   - Track and display final score

**Important Notes**:
- All copies of a single word have the same transformations
  - Example: If "apples" is minified and mirrored, all 3 copies of apples are minified and mirrored
- Different words in the challenge list have different random properties
- Total items on canvas: between 3 and 12 (since 3 words × 1-4 copies each)

#### Mode 3: Settings
- Display current number of words being learned (default: 3)
- Allow user to change the number
- Validate: Must be between 3 and the total number of words in `blackfoot.csv`
- Display min/max values to user

### Reading the CSV File
- The `blackfoot.csv` file contains one word per line
- Your code must read this file dynamically (no hardcoding words)
- Use the word names to construct file paths:
  - Images: `"images/" + word + ".png"`
  - Sounds: Use `play_sound(word, ENV)` (no extension needed)

### Playing Audio
Use the provided `play_sound(soundfilename, env)` function:
- `soundfilename`: Word name without extension (e.g., `"apples"`)
- `env`: Environment variable from `init_env()`

**Example**:
```python
ENV = init_env()
play_sound("apples", ENV)
```

### Environment Setup Code
**REQUIRED**: Use the starter code provided in `main.py`:
```python
def init_env():
    print("\nWelcome! Before we start...")
    env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    while env not in "vri":
        print("Environment not recognized, type again.")
        env = input("Are you using VS Code (V), Replit (r) or IDLE (i)? ").lower()
    print("Great! Have fun!\n")
    return env
```

### What to Submit
- draw.py
- main.py

That's it! Don't submit images, sounds, CSV, or cmpt120image.py. No need to zip anything for this one.

---

## File Organization

### Required Directory Structure

Remember, organize like so (these are the defaults, but you might accidentally drag stuff around!)

```
your_project_folder/
├── your_main_file.py
├── draw.py
├── cmpt120image.py
├── blackfoot.csv
├── images/
│   └── [PNG files]
└── sounds/
    └── [WAV files]
```

### Important Path Notes
- Images are in subfolder `images/`, so use: `cmpt120image.get_image("images/xxxx.png")`
- Sounds are in subfolder `sounds/`, but `play_sound()` handles this automatically
- Do NOT include the path when using `play_sound()` - only the filename without extension

### Example Usage
```python
# Loading an image
img = cmpt120image.get_image("images/apples.png")

# Playing a sound
play_sound("apples", ENV)  # Plays sounds/apples.wav
```

---

## Development Tips

### Starting draw.py
1. Begin with `recolor_image()` - it's the most straightforward
2. Test by changing an apple image from black to green/red/blue
3. Write tests for each function before moving to the next
4. Use `test_basics.py` as a reference for testing approaches

### Placeholder Functions
While developing, use placeholder functions:
```python
def my_function():
    print("inside my_function()")
    return 1  # Temporary return value
```

Later, replace with actual implementation.

### Debugging Images
- Use `cmpt120image.show_image()` to visually inspect your results
- Use `cmpt120image.save_image()` to save intermediate results if you'd like
- Compare your output images with expected results

### Testing Strategy
1. Test each `draw.py` function individually
2. Test with different images (child, apples, etc.)
3. Test edge cases (minimum values, maximum values)
4. Test the full application workflow

### Recommended Development Order
1. **Submission 1**: Develop and test all 5 image functions
2. **Submission 2**:
   - First, implement the menu system
   - Then, implement Learn mode (simpler)
   - Then, implement Settings mode
   - Finally, implement Play mode (most complex)
   - Test each mode thoroughly before moving to the next

---

## FAQ

### Setup and Environment

**Q: What if `test_basics.py` fails?**

A: Common solutions:
- Install pygame: `pip install pygame` or `pip3 install pygame`
- Install numpy: `pip install numpy` or `pip3 install numpy`
- Try using a virtual environment
- Check Python version (should be 3.6+)

**Q: How do I install packages locally?**

A:
```bash
pip install pygame numpy
```
or
```bash
pip3 install pygame numpy
```

Consider using a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pygame numpy
```


**Q: The Pygame window appears frozen - is this normal?**

A: Yes, this is expected behavior. The `show_image()` function displays without an event loop. The window will appear frozen but is showing your image correctly.


---

### Part 1: Image Processing

**Q: What does "non-white pixel" mean?**

A: A pixel is white if its RGB values are [255, 255, 255]. Any other RGB value is non-white.

**Q: Do I need to validate input parameters?**

A: No, you can assume:
- Images have even dimensions for `minify()`
- Canvas is large enough for `draw_item()`
- Parameters are valid types

**Q: Should I modify the original image or create a new one?**

A:
- Functions 1-3 (`recolor_image`, `minify`, `mirror`): Create and return a NEW image
- Functions 4-5 (`draw_item`, `distribute_items`): Modify the canvas IN PLACE (no return value)

**Q: How do I create a new image canvas?**

A: Use the provided functions:
```python
new_img = cmpt120image.get_black_image(width, height)
# or
new_img = cmpt120image.get_white_image(width, height)
```

**Q: What does "average a 2x2 block" mean in minify?**

A: Take 4 adjacent pixels in a 2x2 square and average their R, G, and B values separately:
```python
Average R = (pixel1[0] + pixel2[0] + pixel3[0] + pixel4[0]) // 4
Average G = (pixel1[1] + pixel2[1] + pixel3[1] + pixel4[1]) // 4
Average B = (pixel1[2] + pixel2[2] + pixel3[2] + pixel4[2]) // 4
```

**Q: Can I include test code in draw.py?**

A: Yes, you can include tests in draw.py as long as they don't make your code crash when imported! To be safe, comment out.


### Part 2: Complete Application

**Q: How do I read the CSV file?**

A: Use Python's csv module:
```python
import csv

words = []
with open('blackfoot.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        words.append(row[0])
```

**Q: Can I hardcode the word list?**

A: No! You must read from `blackfoot.csv` dynamically. TAs will test with different CSV files.

**Q: How do I ensure 3 different words in the challenge list?**

A: Use `random.sample()`:
```python
challenge_words = random.sample(available_words, 3)
```
This guarantees no duplicates.

**Q: Should all copies of an item have the same transformations?**

A: Yes! If "apples" is randomly chosen to be minified and mirrored, then ALL copies of apples (whether 1, 2, 3, or 4 copies) should be minified and mirrored.

**Q: Can items overlap in Play mode?**

A: Yes, overlapping is allowed and expected since items are placed randomly.

**Q: What if the user enters invalid input in Settings?**

A: Validate and re-prompt:
- Minimum: 3
- Maximum: Number of words in CSV (12 in provided file)
- Must be an integer

**Q: Do I need error handling for missing files?**

A: No, you can assume all image and sound files exist for words in the CSV.

**Q: Should I show the word name during Play mode?**

A: No, only play the audio. The user must identify the word by sound and count visually.

**Q: How is scoring calculated in Play mode?**

A: Track correct answers across all rounds. Display final score at the end (e.g., "You scored 3 out of 5").

---

### Working with Partners

**Q: How do we join a Canvas group?**

A: Follow instructions in the Canvas submission activity. Both partners must join the SAME group.

**Q: Can we split the work?**

A: Yes, but ensure both partners understand all the code. Both names must appear in the header.

**Q: What if my partner isn't contributing?**

A: Contact your instructor as soon as possible. Document your contributions.

**Q: Can we switch from pair to solo (or vice versa)?**

A: Consult with your instructor.

---

### Technical Questions

**Q: What is the image format?**

A: Images are represented as 3D lists:
- `img[row][col]` gives you a pixel at that position
- `img[row][col]` = `[R, G, B]` where R, G, B are integers 0-255

**Q: How do I access a specific pixel?**

A:
```python
pixel = img[row][col]  # Returns [R, G, B]
red_value = img[row][col][0]
green_value = img[row][col][1]
blue_value = img[row][col][2]
```

**Q: How do I modify a pixel?**

A:
```python
img[row][col] = [255, 0, 0]  # Set to red
```

**Q: Why is my image sideways/wrong dimensions?**

A: Remember:
- `len(img)` gives HEIGHT (number of rows)
- `len(img[0])` gives WIDTH (number of columns)
- Access as `img[row][col]`

**Q: How do I generate a random number between 1 and 4?**

A:
```python
import random
n = random.randint(1, 4)  # Inclusive on both ends
```

**Q: How do I randomly choose True or False?**

A:
```python
import random
should_minify = random.choice([True, False])
```

**Q: Why isn't my audio playing?**

A:
- Ensure you selected the correct environment (v/r/i)
- For VS Code/IDLE, pygame.mixer must be installed
- For Replit, use the replit audio library
- Check that the sound file exists in `sounds/` folder

---

### Grading and Submission

**Q: How will my code be tested?**

A: TAs will:
- Use their own copy of cmpt120image.py, images, sounds, and CSV
- Test with potentially different words and files
- Check that your functions work correctly with various inputs
- Test the full application workflow

**Q: Can I use additional libraries?**

A: Use only:
- Standard Python libraries (random, csv, etc.)
- pygame (provided via cmpt120image)
- numpy (provided via cmpt120image)

**Q: Are there partial marks?**

A: Yes, partial marks are awarded based on:
- Correctness of individual functions
- Code quality and organization
- Successful implementation of different modes

**Q: Can I submit early?**

A: Yes! Test thoroughly and submit when ready.

---

### Debugging

**Q: My minify function creates a black image - what's wrong?**

A: Common issue: Make sure you're creating a canvas with correct dimensions (width, height) and not swapping them.

**Q: My mirror function doesn't work - help?**

A: Check your column calculation. The rightmost pixel (col = width-1) should become the leftmost (col = 0).

**Q: Items aren't appearing on my canvas in distribute_items - why?**

A:
- Ensure you're calling `draw_item()` correctly
- Check that the canvas is white, not black (use `get_white_image()`)
- Verify your random position calculation allows the item to fit

**Q: My program crashes when loading images - what's wrong?**

A:
- Check your file paths include `"images/"` prefix
- Ensure the file extension is `.png`
- Verify the images folder exists in the same directory

**Q: The challenge list sometimes has duplicate words - how do I fix it?**

A: Use `random.sample()` instead of multiple `random.choice()` calls.


---

## Attributions

Icons from [The Noun Project](https://thenounproject.com):

- **Child** by Rediffusion
- **Dog** by Creative Mahira
- **Orange** by Alena Artemova
- **Fish** by IronSV
- **Burger** by Ray Design
- **Apple** by Icon Agent
- **Bread** by Vectors Market
- **Coffee** by AFY Studio
- **Door** by angger bayu priswandana
- **Egg** by StoneHub
- **Tipi** by Uriel Sosa
- **Salt** by QuinX

---

**Good luck with your project! If you have questions not covered in this FAQ, please ask during office hours or on the course discussion board.**
