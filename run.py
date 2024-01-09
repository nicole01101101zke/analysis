import os
import subprocess
import re
import openpyxl

def run_parboil(benchmark_row0, benchmark, dataset):
    parboil_directory = "/home/zke/parboil-test/"
    os.chdir(parboil_directory)
    compile_command = f"./parboil run {benchmark} opencl_nvidia {dataset}"
    result = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, text=True)
    output = result.stdout
    match = re.search(r'Kernel\s+:\s+(\d+\.\d+)', output)

    if match:
        extracted_number = float(match.group(1))
        print("Extracted Number:", extracted_number)
    else:
        print("No match found.")
    formatted_number = "{:.10f}".format(extracted_number)
    
    workbook = openpyxl.load_workbook('/home/zke/analysis/data.xlsx')
    sheet = workbook.active
    for row_number, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if row[0] and row[0].startswith(benchmark_row0):
            sheet.cell(row=row_number, column=12, value=formatted_number)
            break
    workbook.save('/home/zke/analysis/data.xlsx')


#run_parboil("parboil_bfs", "bfs", "SF")
run_parboil("parboil_cutcp", "cutcp", "large")
run_parboil("parboil_lbm", "lbm", "long")
run_parboil("parboil_mri-q", "mri-q", "large")
run_parboil("parboil_sgemm", "sgemm", "medium")
#run_parboil("parboil_spmv", "spmv", "large")
run_parboil("parboil_stencil", "stencil", "default")
run_parboil("parboil_tpacf", "tpacf", "large")