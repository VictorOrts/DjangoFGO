from dearpygui import simple, core
import os

def button_callback(sender, data):
    print("Save Clicked")
def open_file():
    os.system("start /wait cmd /c python fatego.py")    
def save_callback(sender, data):
    os.system("start /wait cmd /c scrcpy\scrcpy.exe")    

with simple.window("Main", x_pos=75, y_pos=400, show=True, no_resize=True, autosize=True):
    with simple.menu_bar("mb"):
        with simple.menu("Settings"):
            core.add_menu_item("List Files", callback=lambda: open_file())
            core.add_menu_item("Ignore Settings", callback=lambda: simple.show_item("Ignore Options"))

    core.add_input_text("Root", default_value="C:\\Users\\Victor\\Desktop\\FGO\\ScriptsFGO")
    core.add_same_line()
    core.add_button("Initialize", callback=save_callback)

    with simple.node_editor("Editor"):
        with simple.node(name="Node 1", x_pos=10, y_pos=10):
            with simple.node_attribute(name="A",output=True):
                core.add_input_float(name="F1", width=150)
        with simple.node(name="Node 2", x_pos=30, y_pos=10):
            with simple.node_attribute(name="B1"):
                core.add_text("Function")
                core.add_button("CLICKED",callback=button_callback)
                print("node2")
            with simple.node_attribute(name="B2",output=True):
                core.add_input_float(name="F2", width=150)
        with simple.node(name="Node 3", x_pos=30, y_pos=10):
            with simple.node_attribute(name="C1"):
                core.add_text("Function")
            with simple.node_attribute(name="C2",output=True):
                core.add_input_float(name="C3", width=150)
        
core.set_style_color_button_position(255)
core.start_dearpygui(primary_window="Main")
