from chess.gameboard.game_board import GameBoard
from chess.gameboard.analyze_board import AnalyzeBoard
# piece imports
from chess.pieces.pawn import Pawn
from chess.pieces.knight import Knight
from chess.pieces.bishop import Bishop
from chess.pieces.queen import Queen 
from chess.pieces.king import King

class Game: 
    def __init__(self):
        # initlize the starting conditions of a chess game. 
        self.inital_pieces = self.get_inital_pieces()

        # Create a GameBoard using the newly created inital_pieces array
        self.game_board = GameBoard(self.inital_pieces)
        self.current_player = "red" 

        # create an HandlePlayerInput instance. This will be used to get, and verify user input.
        input_handler = HandlePlayerInput(self.players_turn) 
    
        # create an AnalyzeBoard instance. Used to monitor 'check' and 'checkmate'  
        analyze = AnalyzeBoard()
        self.current_player_in_check = analyze.is_color_king_in_check(self.current_player, self.game_board)
        self.current_player_in_checkmate = analyze.is_color_king_in_checkmate(self.current_player, self.game_board)

        # Call the main loop of the game.
        self.game_loop()
        
        
    def game_loop(self): 
        # Outline Game Flow
        # 1. Create a while loop. The while loop will continue to run provided that the self.current_player isn't in checkmate.
        # 2. Display the board to the user. 
        # 3. Call an execute player turn function. 
        #     - Needs to Get input from the user. 
        #     - Determine the of the move is valid:
        #         - Can the indicated piece move to the requested position? 
        #         - Will moving the requested piece put self.current_player into check? 
        #     - If the move is valid update the following game variables. 
        #         - update the pieces array of the game board to reflect the move. 
        #         - update self.current_player
        #         - update self.current_player_in_check
        #         - update self.current_player_in_checkmate
        #     - If the move isn't valid request a different move from the user
        # 4. Repeate player turn until current_player is in checkmate
        # 5. call Game over function. Display a message to the winner. 

    



    def get_inital_pieces(self):
        init_royal_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        col_count = 0    # Used to instantiate each piece with starting position
        
        blue_royals, blue_pawns, red_royals, red_pawns = [], [], [], []
        empty_squares = [[EmptySpace() for _ in range(8)] for _ in range(4)]
        
        for piece in init_royal_row:
            letter_col = "ABCDEFGH"[col_count]
            blue_royals.append(piece("blue", f"{letter_col}8"))
            red_royals.append(piece("red", f"{letter_col}1"))
            
            blue_pawns.append(Pawn("blue", f"{letter_col}7"))
            red_pawns.append(Pawn("red", f"{letter_col}2"))
            col_count += 1
        
        return ([blue_royals] + [blue_pawns] +
                empty_squares  +
                [red_pawns] + [red_royals])