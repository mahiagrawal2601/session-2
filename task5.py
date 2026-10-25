# incorrect code (example of mixed indentation)
# mixing tabs and spaces can cause an IndentationError

if True:
    print("Hello")
  print("World")

# correct code (use only spaces for indentation)

if True:
    print("Hello")
    print("World")