import platform


def get_platform_info():
    print("\nSYSTEM INFORMATION")
    print("{:<20}{:>5}".format('system:', platform.system()))
    print("{:<20}{:>5}".format('node:', platform.node()))
    print("{:<20}{:>5}".format('version:', platform.version()))
    print("{:<20}{:>5}".format('processor:', platform.processor()))
    print("{:<20}{:>5}".format("python compiler:", platform.python_compiler()))
