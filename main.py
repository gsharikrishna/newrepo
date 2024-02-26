import turtle

def move_forward():
    turtle.forward(50)

def move_backward():
    turtle.backward(50)

def turn_left():
    turtle.left(90)

def turn_right():
    turtle.right(90)

def main():
    turtle.speed(1)  # Set the turtle speed (1 = slowest, 10 = fastest)

    while True:
        command = input("Enter command (f for forward, b for backward, l for left, r for right, q to quit): ")

        if command == 'f':
            move_forward()
        elif command == 'b':
            move_backward()
        elif command == 'l':
            turn_left()
        elif command == 'r':
            turn_right()
        elif command == 'q':
            break
        else:
            print("Invalid command! Please try again.")

    turtle.done()

if __name__ == "__main__":
    main()
