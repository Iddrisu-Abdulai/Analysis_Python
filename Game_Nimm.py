
import random
import ai




def main():
    print("Welcome to Nimm!")
    
    stones = 20
    max_take = 3
    
    # Choose winning rule
    mode = input("Should take the last stone WIN or LOSE? (win/lose): ").lower()
    
    # Choose AI type
    ai_mode = input("Play against Smart or Random AI? (smart/random): ").lower()
    smart_ai = ai_mode == "smart"
    
    # Choose first player
    turn = input("Who goes first? (player/computer): ").lower()
    
    while stones > 0:
        print(f"\nStones remaining: {stones}")
        
        if turn == "player":
            # Player move
            move = int(input(f"Take 1 to {min(max_take, stones)} stones: "))
            
            # Validate move
            while move < 1 or move > min(max_take, stones):
                move = int(input("Invalid. Try again: "))
            
            stones -= move
            
            # Check game end
            if stones == 0:
                if mode == "win":
                    print("You win!")
                else:
                    print("You lose!")
                break
            
            # Divisible by 3 rule
            if stones % 3 != 0:
                turn = "computer"
            else:
                print("Bonus turn! You go again.")
        
        else:
            # Computer move
            move = get_computer_move(stones, max_take, smart_ai)
            print(f"Computer takes {move}")
            stones -= move
            
            # Check game end
            if stones == 0:
                if mode == "win":
                    print("Computer wins!")
                else:
                    print("Computer loses! You win!")
                break
            
            # Divisible by 3 rule
            if stones % 3 != 0:
                turn = "player"
            else:
                print("Computer gets another turn!")


print("The Ancient Game of Nimm")  # Delete this line and write your code here! :)



def get_computer_move(stones, max_take, smart=True):
    # Smart AI: try to leave a multiple of (max_take + 1)
    if smart:
        target = (max_take + 1)
        move = stones % target
        if move == 0:
            return random.randint(1, min(max_take, stones))
        return move if move <= stones else 1
    else:
        # Random (dummy AI)
        return random.randint(1, min(max_take, stones))


if __name__ == '__main__':
    main()