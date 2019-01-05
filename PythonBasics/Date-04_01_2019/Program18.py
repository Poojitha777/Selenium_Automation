def start(move):
    def run():
        print("started", move.__name__)
        move()
        print("END", move.__name__)
        run.__name__=move.__name__
    return run

@start
def department():
    print("Number of departments")

department()
print(department.__name__)