def from_string_to_list(string, container):
    string_elements = string.split()
    for i in range(len(string_elements)):
        if string_elements[i].isdigit():
            container.append(int(string_elements[i]))
    return container
