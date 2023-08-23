def write_file(file_name, file_content):
    with open(file_name + ".txt", "w", encoding="utf-8") as f:
        f.write(file_content)

def append_to_file(file_name, append_content):
    with open(file_name + ".txt", "a", encoding="utf-8") as f:
        f.write(append_content)

def read_file(file_name):
    with open(file_name + ".txt", "r", encoding="utf-8") as f:
        content = f.read()
    return content

write_file(file_name="example_file", file_content="This is some content.")
append_to_file(file_name="example_file", append_content="\nThis is appended content.")
content = read_file(file_name="example_file")
print(content)
