from math import pi, sin, cos
import flet as ft
import flet.canvas as cv

def model(position: ft.Offset = ft.Offset(0, 0), sizeX: float = 200, sizeY: float = 200):
    pointPaint = ft.Paint(
        color = ft.Colors.RED,
        stroke_width=5,
        stroke_cap=ft.StrokeCap.ROUND,
        style=ft.PaintingStyle.STROKE,
    )

    shape = [
        cv.Points(
            points=[
                ft.Offset(position.x - sizeX / 2, position.y - sizeY / 2),
                ft.Offset(position.x + sizeX / 2, position.y - sizeY / 2),
                ft.Offset(position.x - sizeX / 2, position.y - sizeY / 2),
                ft.Offset(position.x + sizeX / 2, position.y + sizeY / 2),
            ],
            paint=pointPaint,
            # point_mode=ft.PointMode.POINTS,
        )
    ]

    return cv.Canvas(
        shapes=shape,
    )


    page.expand = 1
    page.on_keyboard_event=onKey
    page.update()

ft.app(main)