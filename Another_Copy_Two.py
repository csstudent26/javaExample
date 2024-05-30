


import json

from random import choice
import threading
from ursina import *

from itertools import product

random_key = '' # Declare random_key as a global variable
cube_positions = {}  # Dictionary to store the positions of each cube
cube_rotations = {}
cube_faces = {}  # Dictionary to store the faces of each cube
new_faces = {}
faces = {} 

use_animation = False  # Set  boolean variable (for input function)

roth_dict = {'u': ['y', 1, -90],    'e': ['y', 0, -90],    'd': ['y', -1, -90],
            'l': ['x', -1, 90],  'm': ['x', 0, 90],    'r': ['x', 1, 90],
            'f': ['z', -1, 90],   's': ['z', 0, 90],     'b': ['z', 1, 90]
            }

roth_dict2 = {'a': ['y', 1, 90],    'c': ['y', 0, 90],    'k': ['y', -1, 90],
            'g': ['x', -1, -90],  'n': ['x', 0, -90],    'o': ['x', 1, -90],
            'p': ['z', -1, -90],   'q': ['z', 0, -90],     't': ['z', 1, -90]
            }


state_count = 0

store = []
states = []
states2 = []
current_key = ''  # Initialize a global variable to store the current key

pos_1 = (0,1,-1)   
pos_2 = (1,0,-1)   
pos_3 = (0,-1,-1)   
pos_4 = (-1,0,-1)   
pos_5 = (1,1,0)   
pos_6 = (1,0,1)   
pos_7 = (1,-1,0)   
pos_8 = (-1,1,0)   
pos_9 = (-1,0,1)   
pos_10 = (-1,-1,0)   
pos_11 = (0,1,1)   
pos_12 = (0,-1,1)  



cpos_1 = (-1, 1,-1)
cpos_2 = (1,1,-1)
cpos_3 = (-1,1,1)
cpos_4 = (1,1,1)
cpos_5 = (-1, -1,-1)
cpos_6 = (1,-1,-1)
cpos_7 = (-1,-1,1)
cpos_8 = (1,-1,1)


# Method 01
def eltern_kinder_bezihung(asche, sicht):

    
    for w in wurfel:
         w.position , w.rotation, =round( w.world_position,1), w.world_rotation
         w.parent = scene
    
    zentrum.rotation = 0

    for w in wurfel:

      if eval(f'w.position.{asche}') == sicht:
      
   
        w.parent = zentrum 


# Method 02
def save_state():
    # Record the current state and the key that triggered it
    global current_key, state_count
    if current_key in roth_dict or  current_key in roth_dict2:

        current_state = {'key': current_key, 'state': [(w.position, w.rotation) for w in wurfel]}
        states.append(current_state)
        state_count += 1
     #   print(f"Recorded state for key: {current_key}")
        print(f"Total states recorded: {state_count}")


# Method 03
def input(key):

  #  global use_animation
    global current_key

    
    
    if key not in roth_dict and key not in roth_dict2: return

    if key in roth_dict:
                asche, schicht, winkel = roth_dict[key]
    elif key in roth_dict2:
        asche, schicht, winkel = roth_dict2[key]
    
    eltern_kinder_bezihung(asche, schicht)
    shift = held_keys['shift']

    if use_animation:
        eval(f'zentrum.animate_rotation_{asche}({-winkel if shift else winkel}, duration=0.9)')
        current_key = key  # Update the current_key

    else:
        setattr(zentrum, f'rotation_{asche}', -winkel if shift else winkel)
        current_key = key  # Update the current_key

    
   
    # Update the dictionary with the new positions
    for w in wurfel:
        cube_name = w.name
        cube_position = round(w.world_position, 1)
        cube_positions[cube_name] = cube_position
        

    
    # Update the new dictionary with the new rotations
    for w in wurfel:
        cube_name = w.name
        cube_rotations[cube_name] = round(w.world_rotation, 1)  
        cube_rotations[cube_name] = cube_rotations
 
    save_state()
    print(f"Updated current_key: {current_key}")
    print()

    for w in wurfel:
        cube_name = w.name
        cube_faces[cube_name] = w.faces

    
    if key in ['f', 's', 'b']:
        update_face_colors_01(asche,schicht) 

    if key in ['l', 'm', 'r']:
        update_face_colors_02(asche,schicht) 

    if key in ['u', 'e', 'd']:
        update_face_colors_03(asche,schicht) 
        # PART TWO

    if key in ['p', 'q', 't']:
        update_face_colors_04(asche,schicht) 

    if key in ['g', 'n', 'o']:
        update_face_colors_05(asche,schicht) 

    if key in ['a', 'c', 'k']:
        update_face_colors_06(asche,schicht) 

    for w in wurfel:
        cube_name = w.name
        cube_faces[cube_name] = w.faces




    cube_name = 'Cube_20'  # Specify the cube name you want to check
    position = cube_positions.get(cube_name)
  #  if position is not None:
     #   print(f"The position of {cube_name} is {position}.")
  #  else:
       # print(f"Position of {cube_name} not found.")
  #  print(" Here are the states01",states)


# Method 04
def simulate_key_press(simulated_key):
    global current_key

    if simulated_key in roth_dict:
        asche, schicht, winkel = roth_dict[simulated_key]
    elif simulated_key in roth_dict2:
        asche, schicht, winkel = roth_dict2[simulated_key]
    else:
        return  # Key not found in either dictionary
        

   # asche, schicht, winkel = roth_dict[simulated_key]

    eltern_kinder_bezihung(asche, schicht)
    shift = held_keys['shift']
    eval(f'zentrum.animate_rotation_{asche}({-winkel if shift else winkel}, duration=.9)')
    

    current_key = simulated_key  # Update the current_key

   # save_state()
    print(f"Simulated key press: {simulated_key}")
  #  print("Here are the states01", states)
    


 
def reverse_states():


    use_animation = True  # Set  boolean variable (for input function)

    
    if not states:
        print("No states to reverse.")
        return

    # Use the last recorded key for reversal
    last_state = states[-1]
    last_key = last_state['key']

    if last_key is not None:
        for saved_state in reversed(states):
            asche, schicht, winkel = roth_dict[last_key]

            for cube, (position, rotation) in zip(wurfel, saved_state['state']):
                
                eltern_kinder_bezihung(asche, schicht)
                shift = held_keys['shift']
                reversed_rotation = -rotation if shift else rotation
                cube.rotation = reversed_rotation
                                  
                
        print("We are inside reverse state")
    else:
        print("The last key is None. Cannot reverse states.")
        print("Last state:", last_state)


# Load saved states from JSON file
def load_states_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Example usage:
def get_cube_position(cube_name):
    for cube in wurfel:
        if cube.name == cube_name:
            return cube.position
    return None  # Return None if the cube with the given name is not found

def update_face_colors_01(asche, sicht):

    
    for w in wurfel:
        # Get the current face colors of the cube
     if eval(f'w.position.{asche}') == sicht:

        current_face_colors = w.faces
        
        # Define the new face colors according to the 'f' key rule
        new_face_colors = {
            'front': current_face_colors['front'],
            'back': current_face_colors['back'],
            'left': current_face_colors['bottom'],
            'right': current_face_colors['top'],
            'top': current_face_colors['left'],
            'bottom': current_face_colors['right']
        }
        
        # Update the face colors of the cube
        w.faces = new_face_colors


def update_face_colors_02(asche, sicht):
    for w in wurfel:
      if eval(f'w.position.{asche}') == sicht:

        # Get the current face colors of the cube
        current_face_colors = w.faces
        
        # Define the new face colors according to the 'f' key rule
        new_face_colors = {
            'front': current_face_colors['bottom'],
            'back': current_face_colors['top'],
            'left': current_face_colors['left'],
            'right': current_face_colors['right'],
            'top': current_face_colors['front'],
            'bottom': current_face_colors['back']
        }
        
        # Update the face colors of the cube
        w.faces = new_face_colors


def update_face_colors_03(asche, sicht):
    for w in wurfel:
      if eval(f'w.position.{asche}') == sicht:

        # Get the current face colors of the cube
        current_face_colors = w.faces
        
        # Define the new face colors according to the 'f' key rule
        new_face_colors = {
            'front': current_face_colors['left'],
            'back': current_face_colors['right'],
            'left': current_face_colors['back'],
            'right': current_face_colors['front'],
            'top': current_face_colors['top'],
            'bottom': current_face_colors['bottom']
        }
        
        # Update the face colors of the cube
        w.faces = new_face_colors


def update_face_colors_04(asche, sicht):
    # For faces p, q, t
    # Update for 'Z' Anti Clockwise
    global faces


    for w in wurfel:
        # Get the current face colors of the cube
     if eval(f'w.position.{asche}') == sicht:

        current_face_colors = w.faces
        
        # Define the new face colors according to the 'Z clockwise' key rule
        new_face_colors = {
            'front': current_face_colors['front'],
            'back': current_face_colors['back'],
            'left': current_face_colors['top'],
            'right': current_face_colors['bottom'],
            'top': current_face_colors['right'],
            'bottom': current_face_colors['left']
        }
        
        # Update the face colors of the cube
        w.faces = new_face_colors

def update_face_colors_05(asche, sicht):
    # For Keys, q,n, o
    #Update for 'X' Anti Clockwise
    global faces


    for w in wurfel:
        # Get the current face colors of the cube
     if eval(f'w.position.{asche}') == sicht:

        current_face_colors = w.faces
        
        # Define the new face colors according to the 'Z clockwise' key rule
        new_face_colors = {
            'front': current_face_colors['top'],
            'back': current_face_colors['bottom'],
            'left': current_face_colors['left'],
            'right': current_face_colors['right'],
            'top': current_face_colors['back'],
            'bottom': current_face_colors['front']
        }
        
        # Update the face colors of the cube
        w.faces = new_face_colors


def update_face_colors_06(asche, sicht):

    # For faces a,c,k
    # Y anti clockwise
    global faces


    for w in wurfel:
        # Get the current face colors of the cube
     if eval(f'w.position.{asche}') == sicht:

        current_face_colors = w.faces
        
        # Define the new face colors according to the 'Y  Anti clockwise' key rule
        new_face_colors = {
            'front': current_face_colors['right'],
            'back': current_face_colors['left'],
            'left': current_face_colors['front'],
            'right': current_face_colors['back'],
            'top': current_face_colors['top'],
            'bottom': current_face_colors['bottom']
        }
        
        # Update the face colors of the cube
        w.faces = new_face_colors











def general_movement():
   # result = get_cube_position("Cube_15")
    result = cube_positions.get("Cube_15")

    if result == pos_1:
        print("The Cube_15 is already in the correct position.")
    elif result == pos_2:
        for key in ['p']:
            invoke(input, key)
    elif result == pos_3:
        for key in ['f', 'f']:
            invoke(input, key)
    elif result == pos_4:
        for key in ['f']:
            invoke(input, key)
    elif result == pos_5:
        for key in ['a']:
            invoke(input, key)
    elif result == pos_6:
        for key in ['t', 'a', 'a']:
            invoke(input, key)
    elif result == pos_7:
        for key in ['r', 'p']:
            invoke(input, key)
    elif result == pos_8:
        for key in ['u']:
            invoke(input, key)
    elif result == pos_9:
        for key in ['g', 'u']:
            invoke(input, key)
    elif result == pos_10:
        for key in ['d', 'p', 'p']:
            invoke(input, key)
    elif result == pos_11:
        for key in ['u', 'u']:
            invoke(input, key)
    elif result == pos_12:
        for key in ['d', 'd', 'f', 'f']:
            invoke(input, key)

    else :
        print("Could not Find Cube")

    cube_name = "Cube_15"
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
        else:
            print(f"The top face color of {cube_name} is not 'white'. Rotating the cube...")
            for key in ['f', 'c', 'f']:
                invoke(input, key)
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.") 

    # Set the flag to True indicating general_movement is done



def general_movement_2():
  #  result = get_cube_position("Cube_17")
    result = cube_positions.get("Cube_17")



    if result == pos_11:
        print("The Cube_17 is already in the correct position.")
    elif result == pos_2:
        for key in ['r','r','t']:
            invoke(input, key)
    elif result == pos_1:
        for key in ['u','u']:
            invoke(input, key)
    elif result == pos_3:
        for key in ['d', 'd','t','t']:
            invoke(input, key)
    elif result == pos_4:
        for key in ['l','l','b']:
            invoke(input, key)
    elif result == pos_5:
        for key in ['r','t']:
            invoke(input, key)
    elif result == pos_6:
        for key in ['t']:
            invoke(input, key)
    elif result == pos_7:
        for key in ['o', 't']:
            invoke(input, key)
    elif result == pos_8:
        for key in ['l','b']:
            invoke(input, key)
    elif result == pos_9:
        for key in ['b']:
            invoke(input, key)
    elif result == pos_10:
        for key in ['k', 't','t']:
            invoke(input, key)
    elif result == pos_11:
        print("Cube_17 already in Position")
            
    elif result == pos_12:
        for key in [ 't', 't']:
            invoke(input, key)

    else:
        print(" Cube Not Found ") 


    cube_name = "Cube_17"
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
        else:
            print(f"The top face color of {cube_name} is not 'white'. Rotating the cube...")
            for key in ['t', 'c', 't']:
                invoke(input, key)
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.") 


def general_movement_3():
   # result = get_cube_position("Cube_25")
    result = cube_positions.get("Cube_25")

    if result == pos_5:
        print("The Cube_25 is already in the correct position.")
    elif result == pos_1:
        for key in ['u']:
            invoke(input, key)
    elif result == pos_2:
        for key in ['r']:
            invoke(input, key)
    elif result == pos_3:
        for key in ['d', 'r','r']:
            invoke(input, key)
    elif result == pos_4:
        for key in ['p','d','r','r']:
            invoke(input, key)
           
    elif result == pos_6:
        for key in ['o']:
            invoke(input, key)
    elif result == pos_7:
        for key in ['o', 'o']:
            invoke(input, key)
    elif result == pos_8:
        for key in ['l','l','d','d','r','r']:
            invoke(input, key)
    elif result == pos_9:
        for key in ['g','d','d','r','r']:
            invoke(input, key)
    elif result == pos_10:
        for key in ['d', 'd','r','r']:
            invoke(input, key) 
    elif result == pos_11:
        for key in ['b', 'o']:
            invoke(input, key)
    elif result == pos_12:
        for key in ['t', 'o']:
            invoke(input, key)

    else:
        print("The Cube was not Found")

    cube_name = "Cube_25"
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
        else:
            print(f"The top face color of {cube_name} is not 'white'. Rotating the cube...")
            for key in ['r', 'c', 'r']:
                invoke(input, key)
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.") 
  
    
def general_movement_4():
   # result = get_cube_position("Cube_7")
    result = cube_positions.get("Cube_7")

    if result == pos_8:
        print("The Cube_7 is already in the correct position.")
    elif result == pos_1:
        for key in ['a']:
            invoke(input, key)
    elif result == pos_2:
        for key in ['c','l']:
            invoke(input, key)
    elif result == pos_3:
        for key in ['k', 'l','l']:
            invoke(input, key)
    elif result == pos_4:
        for key in ['l']:
            invoke(input, key)
    elif result == pos_5:
        print(f"The Cube is in Pos_5 {pos_5}")
        for key in ['q',]:
            invoke(input, key)
    elif result == pos_6:
        for key in ['c','c','l']:
            invoke(input, key)
    elif result == pos_7:
        for key in ['k', 'k','l','l']:
            invoke(input, key)
    
    elif result == pos_9:
        for key in ['g']:
            invoke(input, key)
    elif result == pos_10:
        for key in ['g', 'g']:
            invoke(input, key)
    elif result == pos_11:
        for key in ['t', 'g']:
            invoke(input, key)
            
    elif result == pos_12:
        for key in [ 'b', 'g']:
            invoke(input, key)
    
    else:
        print(" Cube 7 Not Found") 

    cube_name = "Cube_7"
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
        else:
            print(f"The top face color of {cube_name} is not 'white'. Rotating the cube...")
            for key in ['l', 'e', 'l']:
                invoke(input, key)
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.") 



def corner_1(): 
    result = cube_positions.get("Cube_6")

    if result == cpos_1:
        print("The Cube_6 is already in the correct position.")
    
    
    elif result == cpos_2:
        print("The Cube_6 is in cpos_2.")

        for key in ['f','k','p','k','s','l','q']:
            invoke(input, key)

    elif result == cpos_3:
        print("The Cube_6 is in cpos_3.")

        for key in ['t','d','d','g','k','l']:
            invoke(input, key)


    elif result == cpos_4:
        print("The Cube_6 is in cpos_4.")

        for key in ['b','k','t','g','k','l']:
            invoke(input, key) 

    elif result == cpos_5:
        print("The Cube_6 is in cpos_5.")

        for key in ['d','g','k','l']:
            invoke(input, key) 

    elif result == cpos_6:
        print("The Cube_6 is in cpos_5.")

        for key in ['g','k','l']:
            invoke(input, key)

    elif result == cpos_7:
        print("The Cube_6 is in cpos_7.")

        for key in ['d','d','g','k','l']:
            invoke(input, key)

    elif result == cpos_8:
        print("The Cube_6 is in cpos_7.")

        for key in ['k','g','k','l']:
            invoke(input, key)


    cube_name = "Cube_6"  # Adjust the name as per your actual cube name
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
            
        else:
            if top_face_color == "orange":
                print(f"The top face color of {cube_name} is 'orange'. Rotating the cube with keys [l, l, d, l, l, l, d, l]...")
                for key in ['l','c', 'l', 'd', 'l', 'l', 'l', 'd', 'l','l','e','g']:
                    invoke(input, key)
            elif top_face_color == "green":
                print(f"The top face color of {cube_name} is 'green'. Rotating the cube with keys [l, l, d, l]...")
                for key in ['l','c', 'l', 'd', 'l','l','e','g']:
                    invoke(input, key)
            else:
                print(f"The top face color of {cube_name} is {top_face_color}. No rotation needed for this color.")
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.")


def corner_2(): 
    result = cube_positions.get("Cube_24")

    if result == cpos_2:
        print("The Cube_24 is already in the correct position.")
    elif result == cpos_1:
        print("The Cube_24 is in cpos_1.")

        for key in ['t','d','b','o','d','r']:
            invoke(input, key) 

    
    elif result == cpos_3:
        print("The Cube_24 is in cpos_3.")

        for key in ['t','d','b','o','d','r']:
            invoke(input, key) 

    elif result == cpos_4:
        print("The Cube_24 is in cpos_4.")

        for key in ['b','k','t','k','o','d','r']:
            invoke(input, key) 

    elif result == cpos_5:
        print("The Cube_24 is in cpos_5.")

        for key in ['o','d','r']:
            invoke(input, key) 

    elif result == cpos_6:
        print("The Cube_24 is in cpos_6.")

        for key in ['k','o','d','r']:
            invoke(input, key)


    elif result == cpos_7:
        print("The Cube_24 is in cpos_7.")

        for key in ['d','o','d','r']:
            invoke(input, key)

    elif result == cpos_8:
        print("The Cube_24 is in cpos_8.")

        for key in ['k','k','o','d','r']:
            invoke(input, key)





    cube_name = "Cube_24"  # Adjust the name as per your actual cube name
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
            
        else:
            if top_face_color == "green":
                print(f"The top face color of {cube_name} is 'green'. Rotating the cube with keys [l, l, d, l, l, l, d, l]...")
                for key in ['f','k','p','d','f','k','p']:
                    invoke(input, key)
            elif top_face_color == "red":
                print(f"The top face color of {cube_name} is 'green'. Rotating the cube with keys [l, l, d, l]...")
                for key in ['f','k', 'p', 'd', 'f','k','p','f','k', 'p', 'd', 'f','k','p']:
                    invoke(input, key)
            else:
                print(f"The top face color of {cube_name} is {top_face_color}. No rotation needed for this color.")
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.")

def corner_3(): 
    result = cube_positions.get("Cube_8")

    if result == cpos_3:
        print("The Cube_8 is already in the correct position.")
    elif result == cpos_1:
        print("The Cube_8 is in cpos_1.")
        for key in ['p','k','f','d','t','k','b']:
                    invoke(input, key)
                    
    elif result == cpos_2:
        print("The Cube_8 is in cpos_2.")
        for key in ['o','k','r','t','k','b']:
                    invoke(input, key)
                    

    elif result == cpos_4:
        print("The Cube_8 is in cpos_4.")
        for key in ['b','k','t','k','t','k','b']:
                    invoke(input, key)
                    
    
                    
    elif result == cpos_5:
        print("The Cube_8 is in cpos_5.")
        for key in ['t','k','b']:
                    invoke(input, key)
                    
    
    elif result == cpos_6:
        print("The Cube_8 is in cpos_6.")
        for key in ['k','t','k','b']:
                    invoke(input, key)
     

    elif result == cpos_7:
        print("The Cube_8 is in cpos_7.")
        for key in ['d','t','k','b']:
                    invoke(input, key)
     
    elif result == cpos_8:
        print("The Cube_8 is in cpos_8.")
        for key in ['d','d','t','k','b']:
                    invoke(input, key) 

    cube_name = "Cube_8"  # Adjust the name as per your actual cube name
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
            
        else:
            if top_face_color == "blue":
                print(f"The top face color of {cube_name} is 'blue'. Rotating the cube with keys [l, l, d, l, l, l, d, l]...")
                for key in ['l','k','g','d','l','k','g']:
                    invoke(input, key)
            elif top_face_color == "orange":
                print(f"The top face color of {cube_name} is 'orange'. Rotating the cube with keys [l, l, d, l]...")
                for key in ['l','k', 'g', 'd', 'l','k','g','l','k', 'g', 'd', 'l','k','g']:
                    invoke(input, key)
            else:
                print(f"The top face color of {cube_name} is {top_face_color}. No rotation needed for this color.")
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.")


def corner_4(): 
    result = cube_positions.get("Cube_26")

    if result == cpos_4:
        print("The Cube_26 is already in the correct position.")

    elif result == cpos_1:
        print("The Cube_8 is in cpos_1.")
        for key in ['g','k','l','k','r','k','o']:
                    invoke(input, key)
             
    elif result == cpos_2:
        print("The Cube_8 is in cpos_2.")
        for key in ['o','k','r','d','b','d','t']:
                    invoke(input, key)
             

    elif result == cpos_3:
        print("The Cube_8 is in cpos_3.")
        for key in ['t','d','b','d','b','d','t']:
                    invoke(input, key)
             

    elif result == cpos_5:
        print("The Cube_8 is in cpos_5.")
        for key in ['d','b','d','t']:
                    invoke(input, key)

    elif result == cpos_6:
        print("The Cube_8 is in cpos_6.")
        for key in ['b','d','t']:
                    invoke(input, key)
             

    elif result == cpos_7:
        print("The Cube_8 is in cpos_7.")
        for key in ['d','b','k','k','t']:
                    invoke(input, key)
             
    elif result == cpos_8:
        print("The Cube_8 is in cpos_8.")
        for key in ['k','b','d','t']:
                    invoke(input, key)
             
    cube_name = "Cube_26"  # Adjust the name as per your actual cube name
    face_colors = cube_faces.get(cube_name)

    if face_colors:
        top_face_color = face_colors.get('top')
        if top_face_color == "white":
            print(f"The top face color of {cube_name} is 'white'.")
            
        else:
            if top_face_color == "red":
                print(f"The top face color of {cube_name} is 'blue'. Rotating the cube with keys [l, l, d, l, l, l, d, l]...")
                for key in ['r','k','o','d','r','k','o']:
                    invoke(input, key)
            elif top_face_color == "blue":
                print(f"The top face color of {cube_name} is 'orange'. Rotating the cube with keys [l, l, d, l]...")
                for key in ['r','k', 'o', 'd', 'r','k','o','r','k', 'o', 'd', 'r','k','o']:
                    invoke(input, key)
            else:
                print(f"The top face color of {cube_name} is {top_face_color}. No rotation needed for this color.")
    else:
        print(f"Cube {cube_name} not found or face colors not initialized.")


app = Ursina()
window.borderless = False
window.size = (800,800)
window.position = (200,200)
EditorCamera()




zentrum = Entity() 




wurfel = []

#for pos in product((-1,0,1),repeat = 3):
for i, pos in enumerate(product((-1, 0, 1), repeat=3)):

    position = (pos[0], pos[1] , pos[2])
    cube_name = f"Cube_{i}"
    faces = {
        'front': "green",
        'back' : "blue",
        'left':  "orange",
        'right': "red",
        'top':   "white",
        'bottom': "yellow",
    }

    cube_faces[cube_name] = faces

    wurfel.append(Entity(model = "Teil_46_model.obj",texture = "Teil_46_texture.png", position = pos, scale = 0.5,name= cube_name, faces=cube_faces[cube_name]))

  
    cube_positions[cube_name] = position

#print(" Here are the states02",states)

def on_button_click():
    global current_key

    list_1 = ['u', 'e', 'd', 'l', 'm', 'r', 'f', 's', 'b']
    list_2 = ['a', 'c', 'k', 'g', 'n', 'o', 'p', 'q', 't']

    if states:
        pressed_keys = [saved_state.get('key') for saved_state in states if saved_state.get('key') is not None]

        # Create a copy of the list before reversing it
        reversed_keys = pressed_keys.copy()[::-1]

        for i, element in enumerate(reversed_keys):
            if element in list_1:
                # Find the equivalent key from list_2
                index_in_list_1 = list_1.index(element)
                equivalent_key = list_2[index_in_list_1]

                # Update the element with the equivalent from list_2
                reversed_keys[i] = equivalent_key

            invoke(simulate_key_press, reversed_keys[i], delay=i * 2)
            

    else:
        print("No previous state recorded.")



def on_button_click_2():
    
    general_movement()

    general_movement_2()

    general_movement_3()
    general_movement_4()

    corner_1()
    corner_2()
    corner_3()
    corner_4()

    





def on_button_click_3():
    random_choices = []

   # list_1 = ['u', 'e', 'd', 'l', 'm', 'r', 'f', 's', 'b']

    list_1 = ['u',  'd', 'l', 'r', 'f',  'b']
    


    for _ in range(10):
        random_key = choice(list_1)
        invoke(input, random_key)

# Create a smaller button
button = Button(
    text='Solve',
    color=color.azure,
    highlight_color=color.cyan,
    scale=(0.175, 0.05),  # Adjust the scale to make it smaller
    position=(-0.25, 0.4),  # Adjust the position as needed
    on_click=on_button_click,
)

# Additional buttons
button2 = Button(
    text='New Game',
    color=color.red,
    highlight_color=color.orange,
    scale=(0.175, 0.05),
    position=(-0.35, 0.3),
    on_click=on_button_click_2,
)

button3 = Button(
    text='Random',
    color=color.white,  # Set color to white
    text_color=color.black,  # Set text color to black
    highlight_color=color.gray,
    
    scale=(0.175, 0.05),
    position=(-0.35, 0.15),
    on_click=on_button_click_3,
)
print("here is the type of cube_positions:", type(cube_positions))
print("The length of cubr_positions is:",len(cube_positions))
#print(cube_positions)







print("--------------------------------------------------------")    



app.run()