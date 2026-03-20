# Project-17
Generate Hirst-Painting
# Hirst Painting Generator 🎨

A Python program that creates a digital artwork inspired by Damien Hirst's spot paintings using the Turtle graphics library. Generates a 10x10 grid of colorful dots.

## Requirements
```bash
# Built-in libraries (no installation needed)
import turtle
import random
```

## How to Run
```bash
python hirst_painting.py
```

**Note:** Click anywhere on the canvas to close the window after viewing.

## What It Does

This program creates a Hirst-style spot painting by:
1. Setting up a 1000x1000 pixel canvas with gray background
2. Creating a 10x10 grid of colored dots
3. Each dot is 20 pixels in diameter
4. Dots are spaced 50 pixels apart
5. Colors are randomly selected from a predefined palette

## Color Palette

The program uses 10 colors extracted from actual Hirst paintings:
```python
color_list = [
    (253, 251, 247),  # Off-white
    (253, 248, 252),  # Light pink
    (235, 252, 243),  # Mint green
    (198, 13, 32),    # Red
    (248, 236, 25),   # Yellow
    (40, 76, 188),    # Blue
    (244, 247, 253),  # Pale blue
    (39, 216, 69),    # Green
    (238, 227, 5),    # Bright yellow
    (227, 159, 49)    # Orange
]
```

## Technical Details

### Canvas Setup
- **Size**: 1000x1000 pixels
- **Background**: Gray
- **Starting Position**: (-250, -250) - bottom left

### Grid Specifications
- **Rows**: 10
- **Columns**: 10
- **Total Dots**: 100
- **Dot Size**: 20 pixels diameter
- **Spacing**: 50 pixels between dot centers

### Turtle Configuration
```python
turtle.colormode(255)  # Use RGB color mode
mikey.penup()          # Don't draw lines between dots
mikey.hideturtle()     # Hide the turtle cursor
```

## Code Breakdown

### Nested Loop Structure
```python
for row in range(10):              # 10 rows
    for item in range(10):         # 10 dots per row
        # Draw dot
        # Move to next position
    # Move to next row
```

### Drawing Process
1. **Pick random color** from palette
2. **Draw dot** at current position
3. **Move right** 50 pixels
4. **After row completes**, move up 50 pixels and reset to left side
5. **Repeat** until all 100 dots are drawn

## Example Output
```
Gray canvas with 10x10 grid of colored dots:

●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●
●  ●  ●  ●  ●  ●  ●  ●  ●  ●

(Each dot is a random color from the palette)
```

## Customization Options

### Change Grid Size
```python
for row in range(15):      # 15 rows
    for item in range(15):  # 15 columns
```

### Adjust Dot Size
```python
mikey.dot(30, random_color)  # Larger dots
```

### Modify Spacing
```python
mikey.forward(75)  # More space between dots
```

### Change Canvas Size
```python
screen.setup(1500, 1500)  # Bigger canvas
```

### Add Your Own Colors
```python
color_list = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    # Add more RGB tuples...
]
```

### Change Background Color
```python
screen.bgcolor("black")  # Or "white", "beige", etc.
```

## About Damien Hirst Spot Paintings

Damien Hirst's spot paintings are iconic contemporary artworks featuring:
- Grids of colorful circular dots
- Systematic arrangement
- Vibrant color palettes
- Mechanical precision combined with randomness

This program captures the essence of Hirst's spot paintings through code.

## Features

✅ **Random color selection** - Each run creates unique artwork  
✅ **RGB color mode** - Uses precise color values  
✅ **Clean grid layout** - Perfectly aligned dots  
✅ **Scalable design** - Easy to modify grid size and spacing  
✅ **Interactive exit** - Click to close window  
✅ **Hidden turtle** - Clean visual without cursor  

## What I Learned

Building this digital art generator taught me:

- **Turtle graphics** - Using Python's turtle module for drawing
- **RGB color system** - Working with (R, G, B) tuples for precise colors
- **Nested loops** - Creating 2D grids with row and column iteration
- **Coordinate system** - Understanding x, y positioning on canvas
- **Turtle methods** - `penup()`, `goto()`, `dot()`, `hideturtle()`
- **Random selection** - Using `random.choice()` for color variety
- **Grid mathematics** - Calculating positions for evenly-spaced items
- **Canvas configuration** - Setting up drawing environment with Screen
- **Visual programming** - Translating artistic concepts into code

This project demonstrated how code can create visual art and replicate artistic styles programmatically.

## Tips for Best Results

1. **Run in IDLE or terminal** - Some IDEs may not display turtle graphics properly
2. **Wait for completion** - All 100 dots take a few seconds to draw
3. **Try different palettes** - Extract colors from your favorite paintings
4. **Experiment with sizes** - Play with dot sizes and spacing ratios
5. **Save your work** - Take screenshots of unique color combinations

Ready to create your own digital Hirst painting? 🖼️

Enjoy! 🎨
