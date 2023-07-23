def print_file_contents(fpath):
    """Opens a file, decodes it and prints (some of) its contents"""
    try:
        with open(fpath, "rb") as myfile:
            data = myfile.read()
            data = data.decode()
            if len(data) <= 100:
                print(data)
            else: 
                print(data[1000])
    # except blocks below
    except FileNotFoundError:
        print(f"ERROR: {fpath} cannot be found")
    except UnicodeDecodeError:
        print(f"ERROR: {fpath} is not UTF-8 encoded")
    except PermissionError:
        print(f"ERROR: Insufficient permission to open {fpath}")
    except Exception as err:
        print(f"ERROR: {err}")


print_file_contents("testfile4.txt")