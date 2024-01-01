import os
import subprocess

def compile_cl_files(input_dir):
    
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith(".cl"):
                input_file_path = os.path.join(root, filename)
                # print(input_file_path)
                # relative_path = os.path.relpath(input_file_path, input_dir)
                # print(relative_path)
                output_file_path = input_file_path.replace(".cl", ".ll")

                compile_command = f"clang -c -x cl -emit-llvm -S -cl-std=CL2.0 -Xclang -finclude-default-header {input_file_path} -o {output_file_path}"

                subprocess.run(compile_command, shell=True)

                print(f"Compiled {input_file_path} to {output_file_path}")


#input_directory = "../shoc/src/opencl/level1/"
input_directory = "../rodinia-main/opencl/"

compile_cl_files(input_directory)
