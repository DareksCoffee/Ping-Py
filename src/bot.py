def move_opposite_paddle(opposite_paddle_y, ball_y, speed, dt):
    """
    A simple bot script that smoothly follows the ball y position.
    Parameters :
    - opposite_paddle_y (float) :  Current y-coordinate of the opposite square.
    - ball_y (float) ; Current y-coordinate of the ball.
    - speed (float): Speed of the opposite square.
    - dt (float): Time elapsed since the last frame.

    Returns : 
    - float: New y-coordinate of the opposite square.
    """
    # Calculate the direction to move
    direction = 1 if ball_y > opposite_paddle_y else -1

    # Calculate the distance between the ball and opposite square
    distance = abs(ball_y - opposite_paddle_y)

    adjusted_speed = min(speed, distance)

    # Update the opposite_square_y based on the direction, adjusted_speed, and dt
    new_opposite_square_y = opposite_paddle_y + direction * adjusted_speed * dt

    return new_opposite_square_y