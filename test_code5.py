def read_file_noncompliant(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()


read_file_noncompliant('C:\Data-Science\CS90\Project\CSCI90-Project\.gitignore')