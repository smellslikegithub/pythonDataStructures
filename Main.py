from Stack import Stack as stack


def main():
    myStack = stack()
    myStack.push(100)
    myStack.push(200)
    myStack.push(300)
    myStack.push(400)
    myStack.push(500)
    print(myStack.get_stack())
    print(myStack.pop())
    print(myStack.get_stack())
    print(myStack.is_empty())


if __name__ == "__main__":
    main()
