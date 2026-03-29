from ..utils import _border, _content_border, _horizontal_spacing, _vertical_spacing

def header(
        message="Encabezado",
        border_divider="=",
        border_divider_length=64,
        content_divider="-",
        content_divider_length=21,
        vertical_divider_spacing=0,
        horizontal_divider_spacing=0,
        top_border=True,
        bottom_border=True
) -> None :
    """ Función para imprimir un encabezado elegante por consola """
    if top_border:
        _border(border_divider,border_divider_length)

    _vertical_spacing(vertical_divider_spacing)

    print(
        _content_border(content_divider, content_divider_length),
        _horizontal_spacing(horizontal_divider_spacing),
        message,
        _horizontal_spacing(horizontal_divider_spacing),
        _content_border(content_divider, content_divider_length)
    )

    _vertical_spacing(vertical_divider_spacing)

    if bottom_border:
        _border(border_divider, border_divider_length)