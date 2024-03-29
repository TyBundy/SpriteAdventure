from classes.globals import Globals
# Checks if a point collides with a rect
def collides_rect(rect=[0, 0, 0, 0], point=[0, 0]):
    return rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]

# Checks if the player collided with a platform/object, returns the collision direction and the platform type
def collides_platform(player, platform):
    player_left, player_right = player.x, player.x + player.width
    player_top, player_bottom = player.y + player.height, player.y

    platform_left, platform_right = platform.x, platform.x + platform.width
    platform_top, platform_bottom = platform.y + platform.height, platform.y

    # Checks if the player and platform are colliding
    if player_left < platform_right and player_right > platform_left and player_top > platform_bottom and player_bottom < platform_top:
        collision = [0, 0]
        
        # Adjust for the current framerate as oppposed to the set framerate
        delta = 1
        if Globals.current_framerate != 0:
            delta = Globals.FPS / Globals.current_framerate

        old_player_left, old_player_right = player_left - player.velocity[0] * delta, player_right - player.velocity[0] * delta
        old_player_top, old_player_bottom = player_top - player.velocity[1] * delta, player_bottom - player.velocity[1] * delta

        # Calculate which direction happened in
        if old_player_right < platform_left and player_right >= platform_left:
            collision[0] = -1
        
        elif old_player_left >= platform_right and player_left < platform_right:
            collision[0] = 1
        
        elif old_player_bottom >= platform_top and player_bottom < platform_top:
            collision[1] = -1
        
        elif old_player_top <= platform_bottom and player_top > platform_bottom:
            collision[1] = 1

        return collision, platform.type

    return (0, "None")
    