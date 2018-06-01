def normalize_lines(response_list):
    # Normalize Lines - return (int)
    lines = [s for s in response_list if "line" in s]
    lines = [int(s) for s in str(lines).split() if s.isdigit()]
    try:
        lines = int(lines[0])
    except IndexError:
        lines = 0
    return lines


def convert_to_bytes(size, size_type):
    # Convert KB or MB for Bytes
    if size_type == "KB":
        return int(float(size) * 1000)
    elif size_type == "MB":
        return int(float(size) * 1000000)


def normalize_size(response_list):
    # Normalize Size - return bytes (int)
    response_list = str(response_list)

    if "Bytes" in response_list:
        size = response_list.split("Bytes")[0].split(" ")[-2]
        size = int(size)
    elif "KB" in response_list:
        size = response_list.split("KB")[0].split(" ")[-2]
        size = convert_to_bytes(size, "KB")
    elif "MB" in response_list:
        size = response_list.split("MB")[0].split(" ")[-2]
        size = convert_to_bytes(size, "MB")
    else:
        size = 0
    return size


def normalize_extension(dir_file):
    from pathlib import Path
    ext = Path(dir_file).suffix
    if ext == "":
        ext = "<others>"
    return ext
