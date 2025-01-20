import flet as ft
import flet.canvas as cv

import time
from enum import Flag, auto


def main(page: ft.Page):
    class TILT(Flag):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

    class PREFERRED_USER_HAND(Flag):
        LEFT = auto()
        RIGHT = auto()

#
# 2D movement (Pan)
#   w/i: Up
#   a/j: Left
#   d/l: Right
#   s/k: Down
    LEFT_HANDED_KEYS  = ["w", "s", "a", "d"]
    RIGHT_HANDED_KEYS  = ["i", "k", "j", "l"]
#
# 3D movement in combination with keys above
#   <Ctrl>: Tilt
#   <Shift>: Scale
#
    size=750 # Drawing area x and y
    keySet = RIGHT_HANDED_KEYS

    def onPanUpdate(e: ft.DragUpdateEvent):
        print("P", e.delta_x, e.delta_y)
        drawArea.top = max(0, drawArea.top + e.delta_y)
        drawArea.left = max(0, drawArea.left + e.delta_x)
        e.control.update()

    def onDragUpdate(e: ft.DragUpdateEvent):
        print("D", e.delta_x, e.delta_y)
        drawArea.top = max(0, drawArea.top + e.delta_y)
        drawArea.left = max(0, drawArea.left + e.delta_x)
        e.control.update()

    # def onHover(e: ft.HoverEvent):
    #     print("H", e.global_x, e.global_y)

    def onKey(e: ft.KeyboardEvent):
        if not e.ctrl and e.key.lower() == keySet[0]:
            # Pan(direction=PAN.UP)
            print("Pan up")
        elif not e.ctrl and e.key.lower() ==  keySet[1]:
            # Pan(direction=PAN.DOWN)
            print("Pan down")
        elif not e.ctrl and e.key.lower() ==  keySet[2]:
            # Pan(direction=PAN.LEFT)
            print("Pan left")
        elif not e.ctrl and e.key.lower() ==  keySet[3]:
            # Pan(direction=PAN.RIGHT)
            print("Pan right")
        if e.ctrl and e.key.lower() ==  keySet[0]:
            # Pan(direction=TILT.UP)
            print("Tilt up")
        elif e.ctrl and e.key.lower() ==  keySet[1]:
            # Pan(direction=TILT.DOWN)
            print("Tilt down")
        elif e.ctrl and e.key.lower() ==  keySet[2]:
            # Pan(direction=TILT.LEFT)
            print("Tilt left")
        elif e.ctrl and e.key.lower() ==  keySet[3]:
            # Pan(direction=TILT.RIGHT)
            print("Tilt right")

        page.update()

    def closeHintDialog(e):
        page.close(hint)

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        on_pan_update=onPanUpdate,
        on_horizontal_drag_update=onDragUpdate,
        on_vertical_drag_update=onDragUpdate,
        # on_hover=onHover,
    )

    drawArea = ft.Container(
        gd,
        bgcolor=ft.Colors.BLUE,
        width=float("inf"),
        height=float("inf"),
        left=0,
        top=0
    )
    paint = ft.Paint(
        color = ft.Colors.RED,
        stroke_width=5,
        stroke_cap = ft.StrokeCap.ROUND,
        style=ft.PaintingStyle.STROKE
    )

    hint = ft.AlertDialog(
        modal=True,
        title=ft.Text("Hint for keyboard usage"),
        content=ft.Text(
            "_Keys_\n" +
            "a\tTilt backward\tm\tTilt forward\n" +
            "j\tTurn left\tl\tTurn right\n" +
            "<Ctrl>i\t Pan up\t<Ctrl>m\tPan down\n",
            style=ft.TextStyle(
                size=12,
                weight=ft.FontWeight.NORMAL
            )
        ),
        actions=[
            ft.TextButton("Close", on_click=closeHintDialog)
        ],
    )

    shape = [
        cv.Path(
            [
                cv.Path.MoveTo(-size / 2, -size / 2),
                cv.Path.LineTo(size / 2, -size / 2),
                cv.Path.LineTo(size / 2, size / 2),
                cv.Path.LineTo(-size / 2, size / 2),
                cv.Path.Close(),
            ],
            paint=paint,
        )
    ]

    threeDBody = cv.Canvas(
        shapes=shape,
    )

    page.window.width = size * 1.2
    page.window.height = size * 1.2

    page.add(ft.Stack(
        [threeDBody],
    ),

    )
    page.expand = 1
    page.on_keyboard_event=onKey
    page.update()

ft.app(main)
