import sys
import time
import threading
import functools

frames = ['|', '/', '—', '\\', '|', '/', '—', '\\']
ball_frames = ['[     ]', '[o    ]', '[oo   ]', '[ooo  ]', '[oooo ]', '[ooooo]', '[ oooo]', '[  ooo]', '[   oo]', '[    o]']
bar_frames = ['[=   ]', '[==  ]', '[=== ]', '[ ===]', '[  ==]', '[   =]']
ast_frames = ['[*    ]', '[**   ]', '[***  ]', '[**** ]', '[*****]', '[ ****]', '[  ***]', '[   **]', '[    *]']

stop_spin = False
color = '\033[38;5;122m'
color_reset = '\033[0m'

def spinner(text, frames, speed):
    global stop_spin
    sys.stdout.write(f'{text} ')
    sys.stdout.flush()

    while not stop_spin:
        for frame in frames:
            sys.stdout.write(f'\033[{len(text) + 3}G')
            sys.stdout.write(f'{color}\b{frame}{color_reset}')
            sys.stdout.flush()
            time.sleep(speed)
    sys.stdout.write('\r')

def runspin(text = "Loading...", frames = frames, speed = 0.2):
    def _runspin(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            global stop_spin
            stop_spin = False
            loading_thread = threading.Thread(target = spinner, args = (text, frames, speed))
            loading_thread.start()

            a = func(*args, **kwargs)

            stop_spin = True
            loading_thread.join()

            sys.stdout.write('\033[2K\r')
            sys.stdout.write(text)
            sys.stdout.write(f'{color} Done!{color_reset}')
            sys.stdout.write('\n')

            return a
        return _wrapper
    return _runspin

if __name__ == '__main__':
    @runspin()
    def justwait():
        time.sleep(5)
    justwait()
