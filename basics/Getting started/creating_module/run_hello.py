if __name__ == '__main__':
    from hello import say_hello
    say_hello()
# if import run_hello by another module
# say_hello() in this module will not excute
# because if __name__ == '__main__':