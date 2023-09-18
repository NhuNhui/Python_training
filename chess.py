# Import các thư viện cần thiết
import chess
import chess.svg

# Hàm để hiển thị bàn cờ với SVG
def display_board(board):
    print(chess.svg.board(board=board))

# Hàm để chơi trò chơi
def play_game():
    # Tạo một bàn cờ mới
    board = chess.Board()

    # Vòng lặp chính của trò chơi
    while not board.is_game_over():
        # Hiển thị bàn cờ
        display_board(board)

        # Lấy lượt đi của người dùng
        move = input("Nhập lượt đi của bạn (ví dụ: e2e4): ")

        # Kiểm tra xem lượt đi có hợp lệ không
        if move in [move.uci() for move in board.legal_moves]:
            # Áp dụng lượt đi vào bàn cờ
            board.push_uci(move)
        else:
            print("Lượt đi không hợp lệ! Hãy thử lại.")

    # Hiển thị bàn cờ cuối cùng
    display_board(board)

# Gọi hàm chơi trò chơi
play_game()
