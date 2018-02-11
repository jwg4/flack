import os
import subprocess
import time


def start_gunicorn():
    args = ["gunicorn", "wsgi.app"]
    p = subprocess.Popen(args=args, cwd="flack")
    time.sleep(5)
    p.kill()


if __name__ == '__main__':
    server_name = os.environ['SERVER']

    if server_name == 'gunicorn':
        start_gunicorn()
