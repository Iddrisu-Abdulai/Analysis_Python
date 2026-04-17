def main():
    # Display welcome message and basic instruction
    print("Mini Console ")
    print("Type 'help' for commands.")
    print()
    
    # Start an infinite loop to keep the console running
    while True:
        # Get user input, remove extra spaces, and convert to lowercase
        cmd = input("Enter your command: ").strip().lower()
        
        # Exit the console
        if cmd == "exit":
            print("Shutting down console...")
            break
        
        # Display available commands
        elif cmd == "help":
            print("""
Commands:
 help   - show commands
 greet  - enter your name
 calc   - simple calculator
 repeat - repeat your text
 clear  - clear screen (fake)
 exit   - quit
""")
        
        # Greet the user by name
        elif cmd == "greet":
            name = input("Enter your name: ")
            print(f"Welcome, {name}!")
        
        # Simple calculator using user input
        elif cmd == "calc":
            expression = input("Enter calculation (e.g. 5 + 3): ")
            try:
                # Evaluate the mathematical expression
                result = eval(expression)
                print("Result:", result)
            except:
                # Handle invalid input
                print("Invalid calculation.")
        
        # Repeat a message multiple times
        elif cmd == "repeat":
            text = input("Say something: ")
            times = int(input("How many times? "))
            
            # Loop to print the text repeatedly
            for i in range(times):
                print(text)
        
        # Simulate clearing the screen
        elif cmd == "clear":
            print("\n" * 20)
        
        # Handle unknown commands
        else:
            print("Command not found.")


# Ensure the program runs only when executed directly
if __name__ == "__main__":
    main()