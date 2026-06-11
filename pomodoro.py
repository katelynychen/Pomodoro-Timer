#list of session durations in minutes
sessions = [25, 5, 25, 5]

def countdown():
    """
    Display a 3-2-1 countdown on the LED screen before each session.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    #show a 3-2-1 countdown on screen before each session round starts 
    basic.show_number(3)
    basic.pause(1000)
    basic.show_number(2)
    basic.pause(1000)
    basic.show_number(1)
    basic.pause(1000)
    basic.clear_screen()

def show_progress(time_left, total_time):
    """
    Light up the LED grid as a progress bar based on time remaining.

    Parameters
    ----------
    time_left : int
        Seconds remaining in the current session.
    total_time : int
        Total seconds in the current session.

    Returns
    -------
    None
    """
    #calculate how many of the 25 LEDs should be lit based on the time that is remaining 
    leds_on = (time_left * 25) // total_time

    #loop through all 25 LEDs and turn them on or off. Plot is (column, row). 
    # % because it resets back to 0 every 5 steps, // because it only increases every 5 steps 
    for i in range(25):
        if i < leds_on:
            led.plot(i % 5, i // 5)
        else:
            led.unplot(i % 5, i // 5)

def session_finished():
    """
    Display a smiley face on the LED screen when a session ends.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # show a :) when pulled --> 4 smiles total. 
    basic.show_icon(IconNames.HAPPY)
    basic.pause(2000)

#Loop through each session in the list 
for i in range(len(sessions)):
    countdown()
    minutes = sessions[i]
    time_left = minutes * 600
    
    
    # count down every minute and update the LED progress bar based off of it 
    while time_left > 0:
        show_progress(time_left, minutes * 60)
        basic.pause(60000)
        time_left -= 60
    session_finished()

import unittest

# Recreated the logic from the micro:bit code in plain Python so it can be tested without needing a micro:bit

def get_leds_on(time_left, total_time):
    """Calculate how many LEDs should be lit given the time remaining."""
    return (time_left * 25) // total_time

def get_time_left(minutes):
    """Convert minutes to seconds."""
    return minutes * 60

def is_session_over(time_left):
    """Return True if the session timer has run out."""
    return time_left <= 0

def get_next_session(current_index, sessions):
    """Return the next session index, or None if all sessions are done."""
    next_index = current_index + 1
    if next_index < len(sessions):
        return next_index
    return None
