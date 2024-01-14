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

def run_polybench(benchmark_row0, path, run_command):
    parboil_directory = "/home/zke/PolyBench-ACC/OpenCL/"
    os.chdir(parboil_directory)
    compile_command = f"cd {path} && {run_command}"
    result = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, text=True)
    output = result.stdout
    pattern1 = r"GPU Time in seconds:\s*([\d.]+)"
    pattern2 = r"CPU Time in seconds:\s*([\d.]+)"
    match1 = re.search(pattern1, output)
    match2 = re.search(pattern2, output)

    if match1:
        extracted_number1 = float(match1.group(1))
        print("Extracted Number1:", extracted_number1)
        formatted_number1 = "{:.10f}".format(extracted_number1)
        workbook = openpyxl.load_workbook('/home/zke/analysis/data.xlsx')
        sheet = workbook.active
        for row_number, row in enumerate(sheet.iter_rows(values_only=True), start=1):
            if row[0] and row[0].startswith(benchmark_row0):
                sheet.cell(row=row_number, column=12, value=formatted_number1)
                break
        workbook.save('/home/zke/analysis/data.xlsx')
    else:
        print("No match1 found.")

    if match2:
        extracted_number2 = float(match2.group(1))
        print("Extracted Number2:", extracted_number2)
        formatted_number2 = "{:.10f}".format(extracted_number2)
        workbook = openpyxl.load_workbook('/home/zke/analysis/data.xlsx')
        sheet = workbook.active
        for row_number, row in enumerate(sheet.iter_rows(values_only=True), start=1):
            if row[0] and row[0].startswith(benchmark_row0):
                sheet.cell(row=row_number, column=11, value=formatted_number2)
                break
        workbook.save('/home/zke/analysis/data.xlsx')
    else:
        print("No match2 found.")
    


# #run_parboil("parboil_bfs", "bfs", "SF")
# run_parboil("parboil_cutcp", "cutcp", "large")
# run_parboil("parboil_lbm", "lbm", "long")
# run_parboil("parboil_mri-q", "mri-q", "large")
# run_parboil("parboil_sgemm", "sgemm", "medium")
# #run_parboil("parboil_spmv", "spmv", "large")
# run_parboil("parboil_stencil", "stencil", "default")
# run_parboil("parboil_tpacf", "tpacf", "large")

run_polybench("polybench_correlation", "datamining/correlation", "./correlation.exe")
run_polybench("polybench_covariance", "datamining/covariance", "./covariance.exe")
run_polybench("polybench_2mm", "linear-algebra/kernels/2mm", "./2mm.exe")
run_polybench("polybench_3mm", "linear-algebra/kernels/3mm", "./3mm.exe")
run_polybench("polybench_atax", "linear-algebra/kernels/atax", "./atax.exe")
run_polybench("polybench_bicg", "linear-algebra/kernels/bicg", "./bicg.exe")
run_polybench("polybench_doitgen", "linear-algebra/kernels/doitgen", "./doitgen.exe")
run_polybench("polybench_gemm", "linear-algebra/kernels/gemm", "./gemm.exe")
run_polybench("polybench_gemver", "linear-algebra/kernels/gemver", "./gemver.exe")
run_polybench("polybench_gesummv", "linear-algebra/kernels/gesummv", "./gesummv.exe")
run_polybench("polybench_mvt", "linear-algebra/kernels/mvt", "./mvt.exe")
run_polybench("polybench_syr2k", "linear-algebra/kernels/syr2k", "./syr2k.exe")
run_polybench("polybench_syrk", "linear-algebra/kernels/syrk", "./syrk.exe")
run_polybench("polybench_gramschmidt", "linear-algebra/solvers/gramschmidt", "./gramschmidt.exe")
run_polybench("polybench_lu", "linear-algebra/solvers/lu", "./lu.exe")
run_polybench("polybench_adi", "stencils/adi", "./adi.exe")
run_polybench("polybench_convolution-2d", "stencils/convolution-2d", "./2DConvolution.exe")
run_polybench("polybench_convolution-3d", "stencils/convolution-3d", "./3DConvolution.exe")
run_polybench("polybench_fdtd-2d", "stencils/fdtd-2d", "./fdtd2d.exe")
run_polybench("polybench_jacobi-1d-imper", "stencils/jacobi-1d-imper", "./jacobi1D.exe")
run_polybench("polybench_jacobi-2d-imper", "stencils/jacobi-2d-imper", "./jacobi2D.exe")

