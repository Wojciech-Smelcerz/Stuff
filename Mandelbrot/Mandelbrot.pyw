# IMPORT
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from assets.scripts import algorithms, dialogs

# FUNCTIONS
# update
def update():
    # update images
    global IMAGE, IMAGE_TK
    IMAGE = IMAGE.resize(size=(RESOLUTION.get(), RESOLUTION.get()))
    algorithms.plot(image=IMAGE, position=(X, Y), zoom=ZOOM, iterations=ITERATIONS.get())
    IMAGE_TK = ImageTk.PhotoImage(image=IMAGE.resize(size=(400, 400)))
    # update widgets
    label_image_image.configure(image=IMAGE_TK)
    label_options_image_resolution.configure(text=f'Resolution: {RESOLUTION.get()}')
    label_options_mandelbrot_iterations.configure(text=f'Iterations: {ITERATIONS.get()}')
    label_options_camera_x.configure(text=f'X: {X}')
    label_options_camera_y.configure(text=f'Y: {Y}')
    label_options_camera_zoom.configure(text=f'Zoom: {ZOOM}')
# transform
def transform(event: tk.Event):
    global X, Y, ZOOM
    # zoom in
    if event.delta > 0:
        ZOOM *= 2
        X += (event.x/400-0.5)/ZOOM
        Y += (event.y/400-0.5)/ZOOM
    # zoom out
    else:
        ZOOM /= 2
        X -= (event.x/400-0.5)/ZOOM/2
        Y -= (event.y/400-0.5)/ZOOM/2
    update()
# reset camera values
def camera_reset():
    global X, Y, ZOOM
    X, Y = -1, 0
    ZOOM = 0.25
    update()
# copy camera values
def camera_copy():
    window.clipboard_clear()
    window.clipboard_append(string=f'X: {X}, Y: {Y}, Zoom: {ZOOM}')
# set camera values
def camera_set():
    global X, Y, ZOOM
    data = dialogs.askcamera(icon='assets/images/icon.ico', x=X, y=Y, zoom=ZOOM)
    if data is not None:
        if data[2] != 0:
            try:
                X, Y, ZOOM = data
                update()
            except:
                messagebox.showerror(title='Mandelbrot', message="Invalid input!")
        else:
            messagebox.showerror(title='Mandelbrot', message="Cannot zoom to zero!")
# save image
def file_save():
    file_path = filedialog.asksaveasfilename(title='Mandelbrot')
    if file_path:
        try:
            IMAGE.save(fp=file_path)
        except ValueError:
            messagebox.showerror(title='Mandelbrot', message='Unknown file extension!')

# TKINTER
# window
window = tk.Tk()
window.title(string='Mandelbrot'), window.geometry(newGeometry='690x460'), window.resizable(width=False, height=False)
window.iconbitmap(bitmap='assets/images/icon.ico')
# variables
RESOLUTION = tk.IntVar(master=window, value=50)
ITERATIONS = tk.IntVar(master=window, value=50)
# labelframe - options
labelframe_options = ttk.Labelframe(master=window, width=240, height=440, text='Options')
labelframe_options.grid(column=0, row=0, padx=10, pady=10)
labelframe_options.grid_propagate(flag=False)
# labelframe - image options
labelframe_options_image = ttk.Labelframe(master=labelframe_options, width=220, height=50, text='Image')
labelframe_options_image.grid(column=0, row=0, padx=7.5, pady=2.5)
labelframe_options_image.grid_propagate(flag=False)
# label - image resolution
label_options_image_resolution = ttk.Label(master=labelframe_options_image, width=14)
label_options_image_resolution.grid(column=0, row=0, padx=7.5, pady=2.5)
# scale - image resolution
scale_options_image_resolution = ttk.Scale(master=labelframe_options_image, length=100, from_=1, to=400, variable=RESOLUTION, command=(lambda v: update()))
scale_options_image_resolution.grid(column=1, row=0)
# labelframe - mandelbrot options
labelframe_options_mandelbrot = ttk.Labelframe(master=labelframe_options, width=220, height=50, text='Mandelbrot')
labelframe_options_mandelbrot.grid(column=0, row=1, pady=2.5)
labelframe_options_mandelbrot.grid_propagate(flag=False)
# label - mandelbrot iterations
label_options_mandelbrot_iterations = ttk.Label(master=labelframe_options_mandelbrot, width=14)
label_options_mandelbrot_iterations.grid(column=0, row=0, padx=7.5, pady=2.5)
# scale - mandelbrot iterations
scale_options_mandelbrot_iterations = ttk.Scale(master=labelframe_options_mandelbrot, length=100, from_=1, to=400, variable=ITERATIONS, command=(lambda v: update()))
scale_options_mandelbrot_iterations.grid(column=1, row=0)
# labelframe - camera options
labelframe_options_camera = ttk.Labelframe(master=labelframe_options, width=220, height=100, text='Camera')
labelframe_options_camera.grid(column=0, row=2, pady=2.5)
labelframe_options_camera.grid_propagate(flag=False)
# label - camera position x
label_options_camera_x = ttk.Label(master=labelframe_options_camera, width=24)
label_options_camera_x.grid(column=0, row=0, padx=7.5, pady=2.5)
# label - camera position y
label_options_camera_y = ttk.Label(master=labelframe_options_camera, width=24)
label_options_camera_y.grid(column=0, row=1, pady=2.5)
# label - camera zoom
label_options_camera_zoom = ttk.Label(master=labelframe_options_camera, width=24)
label_options_camera_zoom.grid(column=0, row=2, pady=2.5)
# button - camera copy
button_options_camera_copy = ttk.Button(master=labelframe_options_camera, width=6, text='Copy', command=camera_copy)
button_options_camera_copy.grid(column=1, row=0)
# button - camera reset
button_options_camera_reset = ttk.Button(master=labelframe_options_camera, width=6, text='Reset', command=camera_reset)
button_options_camera_reset.grid(column=1, row=1)
# button - camera set
button_options_camera_set = ttk.Button(master=labelframe_options_camera, width=6, text='Set', command=camera_set)
button_options_camera_set.grid(column=1, row=2)
# labelframe - file options
labelframe_options_file = ttk.Labelframe(master=labelframe_options, width=220, height=50, text='File')
labelframe_options_file.grid(column=0, row=3, pady=2.5)
labelframe_options_file.pack_propagate(flag=False)
# button - save file
button_options_file_save = ttk.Button(master=labelframe_options_file, width=34, text='Save image', command=file_save)
button_options_file_save.pack(padx=7.5, pady=0)
# labelframe - image
labelframe_image = ttk.Labelframe(master=window, width=420, height=440, text='Image')
labelframe_image.grid(column=1, row=0)
labelframe_image.pack_propagate(flag=False)
# label - image
label_image_image = ttk.Label(master=labelframe_image, width=0)
label_image_image.pack(fill='y', expand=True)
label_image_image.bind(sequence='<MouseWheel>', func=transform)

# PILLOW
# image
IMAGE = Image.new(mode='RGB', size=(RESOLUTION.get(), RESOLUTION.get()))
# STARTUP
camera_reset()
update()
window.mainloop()
