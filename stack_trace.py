def function_a():
    print("Function A started")
    function_b()
    print("function A ended")

def function_b():
    print("Function b started")
    function_c()
    print("function b ended")

def function_c():
    print("Function c started")
    # Intentional Error
    result = 10 / 0
    print/("Function C ended")

# call the intital function
function_a()