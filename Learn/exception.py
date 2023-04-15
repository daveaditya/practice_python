'''
    sample = int(input("Enter a sample number : "))
    print(sample)
'''

while True:
    try:
        sample = int(input("Enter a sample value : "))
        print(55/sample)
        break
    except ValueError as exc:
        print("Make sure you entered a number.")
    except ZeroDivisionError:
        print("Don't enter Zero.")
    except:
        print("An exception occurred!")
    finally:
        print("Hello World!")

print("Accepted!!!")


