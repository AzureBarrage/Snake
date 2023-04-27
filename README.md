Snake Game:

  This is a simple implementation of the classic Snake Game using Python and the Pygame library. In this game, the player controls a snake which grows in length as it eats food. The goal is to eat as much food as possible without the snake colliding with itself or the screen boundaries.

Dependencies:

  Python 3.x, 
  Pygame


How to Run:
  Ensure that you have Python 3.x installed on your computer.
  Install the Pygame library using pip:
  pip install pygame
  Run the Snake Game by executing the Python script:
  python snake_game.py
  
  
Controls:

  Arrow keys: Change the snake's direction
  R key = Restart the game after losing
  Q key = Quit the game
  
Features:

  The snake grows in length as it eats food
  Food is randomly generated on the game screen
  The game detects collisions with itself and screen boundaries
  A message is displayed when the player loses, with the option to restart or quit the game
  
Code Structure:

  draw_objects(): 
    Draws the snake and food on the game screen
    
move_snake(): 
  Updates the snake's position based on its current direction
  
check_collision(): 
  Checks if the snake's head has collided with its body or screen boundaries
  
generate_food():
  Generates new food at a random position on the screen
  
eat_food(): 
  Checks if the snake's head has collided with the food, and increases the snake's length if it has
  
display_message():
  Displays a message on the game screen
  
reset_game():
  Resets the game state, including the snake's position and direction
  
game_loop(): 
  Main game loop handling user input and game logic
  
  
The main loop at the end of the script repeatedly calls game_loop() to restart the game when necessary
