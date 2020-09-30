from ..compiler.compiler import run as run_f

import threading


class AppThread(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename

    def run(self):
        run_f(self.filename)


def run(filename, stdout="snow.stdout", stderr="snow.stderr"):
    old_out = ""
    old_err = ""
    app = AppThread(filename)
    app.start()
    while app.is_alive():
        with open(stdout, "w"):
            pass
        with open(stderr, "w"):
            pass
        with open(stdout, "r") as out:
            f_out = out.read()
            if f_out != old_out:
                print(f_out)
                old_out = f_out
        with open(stderr, "r") as err:
            f_err = err.read()
            if f_err != old_err:
                print(f_err)
                old_err = f_err
