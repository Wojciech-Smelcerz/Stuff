# IMPORT
import tkinter
from tkinter import ttk

# CLASSES
# camera dialog
class CameraDialog:
    # __init__
    def __init__(self, icon: str, x: float, y: float, zoom: float):
        # variables
        self.x, self.y, self.zoom = tkinter.DoubleVar(value=x), tkinter.DoubleVar(value=y), tkinter.DoubleVar(value=zoom)
        # TKINTER
        # window
        self.__window = tkinter.Toplevel()
        self.__window.title(string='Mandelbrot'), self.__window.geometry(newGeometry='242x140'), self.__window.resizable(width=False, height=False)
        self.__window.iconbitmap(bitmap=icon), self.__window.protocol('WM_DELETE_WINDOW', lambda: None)
        # frame - values
        self.__frame_values = ttk.Frame(master=self.__window, width=240, height=80)
        self.__frame_values.grid(column=0, row=0, pady=10)
        self.__frame_values.grid_propagate(flag=False)
        # label - x
        ttk.Label(master=self.__frame_values, width=6, text='X:').grid(column=0, row=0, padx=7.5, pady=2.5)
        # label - y
        ttk.Label(master=self.__frame_values, width=6, text='Y:').grid(column=0, row=1, pady=2.5)
        # label - zoom
        ttk.Label(master=self.__frame_values, width=6, text='Zoom:').grid(column=0, row=2, pady=2.5)
        # entry - x
        self.__entry_x = ttk.Entry(master=self.__frame_values, width=28, textvariable=self.x)
        self.__entry_x.grid(column=1, row=0)
        # entry - y
        self.__entry_y = ttk.Entry(master=self.__frame_values, width=28, textvariable=self.y)
        self.__entry_y.grid(column=1, row=1)
        # entry - zoom
        self.__entry_zoom = ttk.Entry(master=self.__frame_values, width=28, textvariable=self.zoom)
        self.__entry_zoom.grid(column=1, row=2)
        # frame - buttons
        self.__frame_buttons = ttk.Frame(master=self.__window, width=240, height=40)
        self.__frame_buttons.grid(column=0, row=1)
        self.__frame_buttons.grid_propagate(flag=False)
        # button - ok
        self.__button_ok = ttk.Button(master=self.__frame_buttons, width=16, text='Ok', command=self.__ok)
        self.__button_ok.grid(column=0, row=0, padx=10, pady=2.5)
        # button - cancel
        self.__button_cancel = ttk.Button(master=self.__frame_buttons, width=16, text='Cancel', command=self.__cancel)
        self.__button_cancel.grid(column=1, row=0)
        self.__window.wait_window()
    # ok
    def __ok(self):
        self.__window.destroy()
    # cancel
    def __cancel(self):
        self.x = self.y = self.zoom = None
        self.__window.destroy()

# FUNCTIONS
# askcamera
def askcamera(icon: str, x: float, y: float, zoom: float) -> tuple[float, float, float]:
    widget = CameraDialog(icon=icon, x=x, y=y, zoom=zoom)
    if None not in (widget.x, widget.y, widget.zoom):
        try:
            return (float(widget.x.get()), float(widget.y.get()), float(widget.zoom.get()))
        except:
            return None
    return None