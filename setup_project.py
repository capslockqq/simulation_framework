import argparse
import os
from subprocess import call

def copy_file_to(source, dest):
    call('cp ' + source + ' ' + dest, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Setting up project')
    parser.add_argument('-prj_name', help='Name of project', required=True)
    args = vars(parser.parse_args())
    call('cd ..' + ' && ' + 'mkdir ' + args['prj_name'] + ' && ' +'cd ' + args['prj_name'] + ' && ' +'mkdir application_code && ' +'mkdir simulation && ' +'mkdir target && cd simulation && mkdir ' + args['prj_name'] + '_model', shell=True)
    
    dest = "../" + args['prj_name'] + '/application_code/'
    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/application_code_template.cpp'
    copy_file_to(source, dest)

    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/application_code_template.hpp'
    copy_file_to(source, dest)

    dest = "../" + args['prj_name'] + '/application_code/CMakeLists.txt'
    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/CMakeLists_application_code.txt'
    copy_file_to(source, dest)

    dest = "../" + args['prj_name'] + '/simulation/CMakeLists.txt'
    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/CMakeLists_simulation_program.txt'
    copy_file_to(source, dest)

    dest = "../" + args['prj_name'] + '/simulation/' + args['prj_name'] + '_model/CMakeLists.txt'
    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/CMakeLists_simulation_model.txt'
    copy_file_to(source, dest)

    dest = "../" + args['prj_name'] + '/target/CMakeLists.txt'
    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/CMakeLists_target.txt'
    copy_file_to(source, dest)

    dest = "../" + args['prj_name'] + '/target/CMakeLists.txt'
    source = os.path.dirname(os.path.abspath(__file__)) + '/build_files_for_project_setup/CMakeLists_target.txt'
    copy_file_to(source, dest)

    