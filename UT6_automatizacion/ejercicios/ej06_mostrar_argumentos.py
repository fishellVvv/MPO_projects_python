import sys

def show_args():
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

try:
    show_args()
except Exception as e:
    print(e)
