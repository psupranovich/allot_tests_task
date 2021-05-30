def task_two(your_list: list) -> str:
    new_list = []
    try:
        for i in your_list:
            if i not in new_list:
                new_list.append(i)
            else:
                return i
    except:
        return 'Error: Input must be a list or a string!'


'''some tests'''
print(task_two('kolo'))
print(task_two(['a', 'v', 3, 'k', 4, 'd', 3, 'd']))
print(task_two(1234))
