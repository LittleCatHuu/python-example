#coding = utf-8
# 定义函数
# def temp_convert(var):
#    try:
#       return int(var)
#    except ValueError as Argument:
#       print ("The argument does not contain numbers\n", Argument)

# # Call above function here.
# temp_convert("xyz")


def functionName( level ):
    if level <1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level

try:
    l=functionName(-10)
    print ("level=",l)
except Exception as e:
    print ("error in level argument",e.args[0])