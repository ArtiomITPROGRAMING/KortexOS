import curses
import traceback

with open("/usr/local/bin/kortex-keyboard") as f:
    code = f.read()

# Let's inspect what happens in draw_keyboard
try:
    exec(code, globals())
except Exception as e:
    with open("/tmp/kb_err.log", "w") as f:
        f.write(traceback.format_exc())
    print("Caught:", e)
