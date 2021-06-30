class HandlePlayerInput:        
    def player_input_main_method(self):
        # Get, Parse, and Confirm players desired movement. 
        player_confirmation = False
        
        while player_confirmation != True:
            player_move = self.get_player_piece_move()
            player_move_dict = self.parse_player_move(player_move)
            player_confirmation = self.get_player_confirmation(player_move_dict)
        
        return player_move_dict
        
    def get_player_piece_move(self):
        # Get the chese piece movement that the player would like to make
        print("If you would like to forfit you must type 'I yield'")
        player_move = input("What move would you like to make: ")
        return player_move
    
    def parse_player_move(self, player_move):
        # Receive move as entered by the user. Split up the input to determine
        # what the user is trying to do. Return a dictionary of move details 
        move_dict = { "move_type" : "",
                      "move_piece": "",
                      "from": "", 
                      "to": "", 
                      "promotion_to": "",
                      "confirm_string": ""}
        
        piece_dict = { "K": "king", "Q": "queen", "B": "bishop", 
                       "N": "knight", "R": "rook", "P": "pawn" }
        
        move_elements = [element.upper().strip() for element in player_move.split("-")]
        
        # Handle Forfit
        if move_elements[0] == "I YIELD": 
            move_dict["move_type"] = "forfeit"
            move_dict["confirm_string"] = "forfeit the game"
            return move_dict
        
        # Handle Castling
        if (move_elements[0] == "O" or move_elements[0] == "0"):
            if len(move_elements) == 2:
                rook_side = "kingside"
            else: 
                rook_side = "queenside"
                
            move_dict["move_type"] = "castle"
            move_dict["move_piece"] = rook_side + "-rook and the king"
            move_dict["confirm_string"] = f"castle {rook_side} rook and the king"
            return move_dict
        
        move_dict["move_type"] = "move"
        move_dict["move_piece"] = piece_dict[move_elements[1]]
        move_dict["from"] = move_elements[0]
        move_dict["to"] = move_elements[2]
        move_dict["confirm_string"] = f"move {move_dict['move_piece']} at {move_elements[0]} to {move_elements[2]}"
        
        # Handle Promotion
        if (len(move_elements) > 3): 
            move_dict["move_type"] = "promote"
            move_dict["promotion_to"] = piece_dict[move_elements[-1]]
            move_dict["confirm_string"] = (f"promote {move_dict['move_piece']} at {move_elements[0]} "+
                                           f"to {move_dict['promotion_to']} at {move_elements[2]}")

        return move_dict
    
    def get_player_confirmation(self, move_dict): 
        confirmation_message = f"To confirm you would like to {move_dict['confirm_string']}? "
        print(confirmation_message, "Type 'y' or 'yes' to confirm or anything else to enter a new move: ")
        player_confirmation = input(confirmation_message).lower()
        if player_confirmation == 'y' or player_confirmation == 'yes': 
            return True
        else: 
            return False