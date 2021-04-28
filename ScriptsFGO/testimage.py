from dearpygui.core import *

def do_something(sender, data):
    log_info('This did something', logger='MyLog')

def call_async_function(sender, data):
    do_something()

add_button('MyButton', callback=call_async_function)
add_logger('MyLog')

start_dearpygui()