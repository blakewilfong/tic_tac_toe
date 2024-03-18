class TicTacToe:
    def __init__(self):
        self.game_on = True

    def generate_board(self):
        game_board = [f"\033[4m {self.variable_dict["var1"]} | {self.variable_dict["var2"]} | {self.variable_dict["var3"]} \033[0m",
                      f"\033[4m {self.variable_dict["var4"]} | {self.variable_dict["var5"]} | {self.variable_dict["var6"]} \033[0m",
                      f" {self.variable_dict["var7"]} | {self.variable_dict["var8"]} | {self.variable_dict["var9"]} "]
        for line in game_board:
            print(line)

    def invalid_choice_checker(self, choice):
        legal_choices = []
        for key in self.variable_dict:
            legal_choices.append(self.variable_dict[key])
        if choice not in legal_choices or choice == "X" or choice == "O":
            print("Illegal selection")
            return True
        else:
            return False

    def x_choice(self):
        new_x_val = input("Player 1, where would you like to place your X?")
        if tictactoe.invalid_choice_checker(new_x_val):
            tictactoe.x_choice()
        else:
            for key in self.variable_dict:
                if self.variable_dict[key] == new_x_val:
                    self.variable_dict[key] = "X"

    def o_choice(self):
        new_o_val = input("Player 2, where would you like to place your O?")
        if tictactoe.invalid_choice_checker(new_o_val):
            tictactoe.o_choice()
        else:
            for key in self.variable_dict:
                if self.variable_dict[key] == new_o_val:
                    self.variable_dict[key] = "O"

    def determine_winner(self):
        if self.variable_dict["var1"] == "X" and self.variable_dict["var2"] == "X" and self.variable_dict["var3"] == "X" \
            or self.variable_dict["var4"] == "X" and self.variable_dict["var5"] == "X" and self.variable_dict["var6"] == "X" \
            or self.variable_dict["var7"] == "X" and self.variable_dict["var8"] == "X" and self.variable_dict["var9"] == "X" \
            or self.variable_dict["var1"] == "X" and self.variable_dict["var4"] == "X" and self.variable_dict["var7"] == "X" \
            or self.variable_dict["var2"] == "X" and self.variable_dict["var5"] == "X" and self.variable_dict["var8"] == "X" \
            or self.variable_dict["var3"] == "X" and self.variable_dict["var6"] == "X" and self.variable_dict["var9"] == "X" \
            or self.variable_dict["var1"] == "X" and self.variable_dict["var5"] == "X" and self.variable_dict["var9"] == "X" \
            or self.variable_dict["var3"] == "X" and self.variable_dict["var5"] == "X" and self.variable_dict["var7"] == "X":
            print("Tic Tac Toe! Player 1 wins!")
            return True

        if self.variable_dict["var1"] == "O" and self.variable_dict["var2"] == "O" and self.variable_dict["var3"] == "O" \
            or self.variable_dict["var4"] == "O" and self.variable_dict["var5"] == "O" and self.variable_dict["var6"] == "O" \
            or self.variable_dict["var7"] == "O" and self.variable_dict["var8"] == "O" and self.variable_dict["var9"] == "O" \
            or self.variable_dict["var1"] == "O" and self.variable_dict["var4"] == "O" and self.variable_dict["var7"] == "O" \
            or self.variable_dict["var2"] == "O" and self.variable_dict["var5"] == "O" and self.variable_dict["var8"] == "O" \
            or self.variable_dict["var3"] == "O" and self.variable_dict["var6"] == "O" and self.variable_dict["var9"] == "O" \
            or self.variable_dict["var1"] == "O" and self.variable_dict["var5"] == "O" and self.variable_dict["var9"] == "O" \
            or self.variable_dict["var3"] == "O" and self.variable_dict["var5"] == "O" and self.variable_dict["var7"] == "O":
            print("Tic Tac Toe! Player 2 wins!")
            return True
        else:
            pass

    def reset_dictionary(self):
        self.variable_dict = {
            "var1": str(1),
            "var2": str(2),
            "var3": str(3),
            "var4": str(4),
            "var5": str(5),
            "var6": str(6),
            "var7": str(7),
            "var8": str(8),
            "var9": str(9),
        }

    def dictionary_checker(self):
        checker_list = []
        for key in self.variable_dict:
            if self.variable_dict[key] == "X" or self.variable_dict[key] == "O":
                pass
            else:
                checker_list.append("1")
        if not checker_list:
            return True
        else:
            pass


tictactoe = TicTacToe()

print("Welcome to Tic Tac Toe!")


def game():
    tictactoe.reset_dictionary()
    while tictactoe.game_on:
        tictactoe.generate_board()
        tictactoe.x_choice()
        if tictactoe.dictionary_checker():
            continue_game = input("Game has ended in a tie. Play again? y or n")
            if continue_game == "y":
                game()
            else:
                print("Thanks for playing.")
                tictactoe.game_on = False
                break
        if tictactoe.determine_winner():
            continue_game = input("Play again? y or n")
            if continue_game == "y":
                game()
            else:
                print("Thanks for playing.")
                tictactoe.game_on = False
                break
        tictactoe.generate_board()
        tictactoe.o_choice()
        if tictactoe.dictionary_checker():
            continue_game = input("Game has ended in a tie. Play again? y or n")
            if continue_game == "y":
                game()
            else:
                print("Thanks for playing.")
                tictactoe.game_on = False
                break
        tictactoe.determine_winner()
        if tictactoe.determine_winner():
            continue_game = input("Play again? y or n")
            if continue_game == "y":
                game()
            else:
                print("Thanks for playing.")
                tictactoe.game_on = False
                break


game()
