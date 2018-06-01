def output(project, tab_files, tab_dir):
    # prints for debug
    print('=====================  ' + project + '  =====================')
    print(tab_files)
    print('')
    print(tab_dir)

    # create new file txt
    new_path = 'results/' + project + '.txt'
    new_output = open(new_path, 'w')
    new_output.write(str(tab_files) + '\n')
    new_output.write('\n')    
    new_output.write(str(tab_dir))
    new_output.close()
