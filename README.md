# Chess-to-GIF
Turn any PGN chess game into a gif.

Inspired by https://chess.com/gifs

## How to use
Install the requirements with: `pip install -r requirements.txt`

Use `python to_gif.py -h` to get the help menu.

## Examples
`python to_gif.py -f game.pgn`

`python to_gif.py -f game.pgn -o queens_gambit.gif` saves the gif as queens_gambit.gif

`python to_gif.py -f game.pgn -o bongcloud.gif -d 2` makes the delay between each move 2 seconds.
