# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import funcy
# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [ ]
# Submenu list of [Prompt, Action]
# Works similarly to main_menu

data_menu = [
  
    ["Swap", "python_menu_challenges/swap.py"],
    ["Keypad", "python_menu_challenges/keypad.py"],
    ["InfoDB lists/loops (not working on menu)", "python_menu_challenges/infoDB.py"],
]

math_menu = [
    ["Fibonacci", "python_menu_challenges/fibonacci.py"],
    ["Factorial (not working on menu)", "python_menu_challenges/factorial.py"],
    ["Math function (not working on menu)", "python_menu_challenges/math.py"],
    ["Palindrome (not working on menu)", "python_menu_challenges/palindrome.py"],

]

drawing_menu = [
    
    ["Tree", "python_menu_challenges/tree.py"],
    ["Animation", "python_menu_challenges/animation.py"],
    

]


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nplease pick one\n{border}"
# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "function menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Data", data])
    menu_list.append(["Math", math])
    menu_list.append(["Drawings", draw])
    buildMenu(title, menu_list)
# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def data():
    title = "function submenu" + banner
    buildMenu(title, data_menu)

def math():
    title = "Function Submenu" + banner
    buildMenu(title, math_menu)

def draw():
    title = "Function Submenu" + banner
    buildMenu(title, drawing_menu)
  
def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])
    # get user choice
    choice = input("input:")
    
    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
      
        
          
        if choice == 0:
            # stop
            print("you have left the program! thank you!")
            exit()
            return
            
        try:
            # try as function
            action = prompts.get(choice)[1]
            
            action()
            
            
        except TypeError:
            try:  # try as playground style
                
                exec(open(action).read())
                
                
     
                #python_menu_challenges/ship.ship()
                
          
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    buildMenu(banner, options)  # recursion, start menu over again
if __name__ == "__main__":
    menu()

#test
