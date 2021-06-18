def str_filter(list):
    new_list = []
    for v in list:
        try:
            int(v)
            new_list.append(int(v))
        except ValueError:
            continue
    return new_list


subj = {}
with open('tasksix.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        tmp_list = [lecture, practice, lab]
        new_list = str_filter(tmp_list)
        subj[subject] = sum(new_list)
    print(f'Общее кол-во часов по предметам: {subj}')
