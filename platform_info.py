import platform


def get_platform_info(output_file):
    print("\nSYSTEM INFORMATION", file=output_file)
    print("{:<20}{:>5}".format('system:', platform.system()), file=output_file)
    print("{:<20}{:>5}".format('node:', platform.node()), file=output_file)
    print("{:<20}{:>5}".format('version:', platform.version()), file=output_file)
    print("{:<20}{:>5}".format('processor:', platform.processor()), file=output_file)
    print("{:<20}{:>5}".format("python compiler:", platform.python_compiler()), file=output_file)
