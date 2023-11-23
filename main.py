import tkinter as tk

chessboard = [
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-']
]

def draw_chessboard():
    board_size = min(root.winfo_width(), root.winfo_height())
    square_size = board_size / 8

    for row in range(8):
        for col in range(8):
            x0, y0 = col * square_size, row * square_size
            x1, y1 = x0 + square_size, y0 + square_size
            color_index = (row + col) % 2
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[color_index])

            piece = chessboard[row][col]
            if piece != '-':
                piece_image = get_piece_image(piece)
                canvas.create_image((x0 + x1) / 2, (y0 + y1) / 2, image=piece_image)

def get_piece_image(piece):
    return tk.PhotoImage(file={"whitebishop"}.png)
    pass

def on_window_resize(event):
    canvas.delete("all")
    draw_chessboard()

root = tk.Tk()
root.title("Chess Game")

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

root.bind("<Configure>", on_window_resize)

colors = ["white", "lightgrey"]

draw_chessboard()

root.mainloop()
