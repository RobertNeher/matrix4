import flet as ft
import flet.canvas as cv

import time
from enum import Flag, auto
from math import pi, cos, sin

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
#   <key>: Roll
#   <Ctrl><key>: Yaw
#   <Shift><key>: Translate
#
    size=750
    deltaX = deltaY = deltaZ = pi / 24
    rotationX = rotationY = rotationZ = 0

    keySet = RIGHT_HANDED_KEYS

    def onRotate(e: ft.DragUpdateEvent):
        print("R", e.delta_x, e.delta_y)
        drawArea.top = max(0, drawArea.top + e.delta_y)
        drawArea.left = max(0, drawArea.left + e.delta_x)
        e.control.update()

    # def onHover(e: ft.HoverEvent):
    #     print("H", e.global_x, e.global_y)

    def onKey(e: ft.KeyboardEvent):
        if not e.ctrl and e.key.lower() == keySet[0]:
            # Rotate around y-axis counter clockwise
            print("Rotate y left")
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
        on_pan_update=onRotate,
        on_horizontal_drag_update=onRotate,
        on_vertical_drag_update=onRotate,
        # on_hover=onHover,
    )

    drawArea = ft.Container(
        gd,
        bgcolor=ft.colors.BLUE,
        width=float("inf"),
        height=float("inf"),
        left=0,
        top=0
    )
    paint1 = ft.Paint(
        color = ft.colors.RED,
        stroke_width=5,
        stroke_cap = ft.StrokeCap.ROUND,
        style=ft.PaintingStyle.STROKE
    )
    paint2 = ft.Paint(
        color = ft.colors.BLUE_100,
        stroke_width=5,
        stroke_cap = ft.StrokeCap.ROUND,
        style=ft.PaintingStyle.FILL,
        # blend_mode=ft.BlendMode.COLOR_BURN,
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
        cv.Rect(
            x = size / 2,
            y = size / 2,
            width = size / 2,
            height = size / 2,
            border_radius=5,
            paint=paint1,
        ),
        cv.Oval(
            x = size / 2,
            y = size / 2,
            width = size / 2 * 0.9,
            height = size / 2 * 0.9,
            paint = paint2,
        ),
    ]

    threeDBody = cv.Canvas(
        shapes=shape,
    )

    page.window.alignment=ft.alignment.center
    page.window.width = size * 1.2
    page.window.height = size * 1.2

    page.add(ft.Stack(
        [threeDBody],
        alignment=ft.alignment.center
    ),

    )
    page.expand = 1
    page.on_keyboard_event=onKey
    page.update()

ft.app(main)
