def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]

    total_boxes = 0
    diff = 0
    size = height * length * width
    for element in args[3::]:
        if element == 'Finish':
            break
        total_boxes += element

    if size > total_boxes:
        diff = size - total_boxes
        return f'There is free space in the box. You could put {diff} more cubes.'
    else:
        diff = total_boxes - size
        return f'No more free space! You have {diff} more cubes.'


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
