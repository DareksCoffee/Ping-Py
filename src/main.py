# Simple Ping Pong game script, made using Pygame
# The project is free to use

# MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import pygame # Importing the Library "Pygame" for more infos https://www.pygame.org/
from pingpong import ping_pong # Importing "pingpong.py" that includes the ping_pong function

pygame.init() # Initialize Pygame

## Setting up the window ##
title = pygame.display.set_caption("Ping Py") # Setting the title of the window

screen_width = 1280 # The width of the window
screen_height = 720 # The height of the window

screen = pygame.display.set_mode((screen_width, screen_height)) 
############################

clock = pygame.time.Clock() # Create a Clock object

ping_pong(screen, clock, screen_width, screen_height) # Call the ping_pong function with the initialized screen and clock