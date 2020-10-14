import test1

print("top-level in test2.py")

test1.func()

if __name__ == "__main__":
    print("test2.py is being run directly")
else:
    print("test2.py is being imported into another module")
    
    
    