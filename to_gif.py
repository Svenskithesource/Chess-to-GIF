import chess.pgn, chess, argparse, io, PIL.Image, os


def get_coordinates(square, x_positions, y_positions):
    x = [i * 150 for i, n in enumerate(x_positions) if square in n][0]

    y = [i * 150 for i, n in enumerate(y_positions) if square in n][0]

    return int(x), int(y)


def get_piece_images():
    pieces = os.listdir("pieces")
    images = {}
    for piece in pieces:
        images[piece] = PIL.Image.open("./pieces/" + piece).convert("RGBA")
    return images


def get_image(board: chess.Board):
    images = get_piece_images()
    new_board = PIL.Image.new("RGBA", (1200, 1200))
    board_img = PIL.Image.open("board.png")
    new_board.paste(board_img)
    x_positions = [
        [y for y in range(x, 65, 8)] for x in range(1, 9)
    ]  # this took a long time to figure out and it still isn't as efficient as I'd like
    y_positions = [x for x in range(1, 65)]
    y_positions = [y_positions[i : i + 8] for i in range(0, len(y_positions), 8)]
    for i, square in enumerate(chess.SQUARES):
        piece = board.piece_at(square)
        if piece == "none" or not piece:
            continue

        piece = (
            f"b{str(piece).lower()}.png"
            if str(piece).isupper()
            else f"w{str(piece).lower()}.png"
        )  # Get the correct filename
        x, y = get_coordinates(i + 1, x_positions, y_positions)
        new_board.paste(images[piece], (x, y), images[piece])

    return new_board


def main():
    pgn = open("game.pgn")

    game = chess.pgn.read_game(pgn)
    board = game.board()
    gif = get_image(board)
    board_images = []
    for move in game.mainline_moves():
        board.push(move)
        board_images.append(get_image(board))
    gif.save("game.gif", save_all=True, append_images=board_images, duration=1000)


if __name__ == "__main__":
    main()
