import os
import subprocess
import time
import xlwt

codeOutputs = []
students = []
runTime = []
correctOutputBool = []
language = []
inputFiles = []
inputFiles = []
breakTime = 1.5  # secounds
owd = os.getcwd()
dirFiles = []
os.chdir("codes")


def getFiles():
    dir = os.listdir()
    for x in dir:
        if x.endswith('.c'):
            students.append(x[:-2])
            language.append('C')
            c(x)
        if x.endswith('.py'):
            students.append(x[:-3])
            language.append('Python')
            python(x)
        if x.endswith('.cpp'):
            students.append(x[:-4])
            language.append('C++')
            cpp(x)
        if x.endswith('.java'):
            students.append(x[:-5])
            language.append('Java')
            java(x)


def c(dir):
    print('Compiling ' + dir[:-2] + '... ')
    os.system('g++ ' + dir + ' -o' + dir[:-2])
    try:

        tStart = time.time()
        codeOutputs.append(subprocess.check_output(('./' + dir[:-2]), timeout=breakTime))
        tEnd = time.time()
        tFinsh = tEnd - tStart
        runTime.append(tFinsh)
    except subprocess.TimeoutExpired:
        codeOutputs.append('TLE')
        runTime.append('TLE')
    except:
        codeOutputs.append('Didn\'t compile')
        runTime.append('Didn\'t compile')


def python(dir):
    print('Compiling ' + dir[:-3] + '... ')
    try:
        tStart = time.time()
        codeOutputs.append(subprocess.check_output(('python ' + dir), timeout=breakTime))
        tEnd = time.time()
        tFinsh = tEnd - tStart
        runTime.append(tFinsh)
    except subprocess.TimeoutExpired:
        codeOutputs.append('TLE')
        runTime.append('TLE')
    except:
        codeOutputs.append('Didn\'t compile')
        runTime.append('Didn\'t compile')


def cpp(dir):
    print('Compiling ' + dir[:-4] + '... ')
    os.system('g++ ' + dir + ' -o' + dir[:-4])
    try:
        tStart = time.time()
        codeOutputs.append(subprocess.check_output(('./' + dir[:-4]), timeout=breakTime))
        tEnd = time.time()
        tFinsh = tEnd - tStart
        runTime.append(tFinsh)
    except subprocess.TimeoutExpired:
        print('TLE')
        codeOutputs.append('TLE')
        runTime.append('TLE')
    except:
        print('Didn\t Compile')
        codeOutputs.append('Didn\'t compile')
        runTime.append('Didn\'t compile')


def java(dir):
    print('Compiling ' + dir[:-5] + '... ')
    os.system('javac ' + dir)
    try:
        tStart = time.time()
        codeOutputs.append(subprocess.check_output(('java ' + dir[:-5]), timeout=breakTime))
        tEnd = time.time()
        tFinsh = tEnd - tStart
        runTime.append(tFinsh)
    except subprocess.TimeoutExpired:
        codeOutputs.append('TLE')
        runTime.append('TLE')
    except:
        codeOutputs.append('Didn\'t compile')
        runTime.append('Didn\'t compile')


def correctOutput():
    for x in codeOutputs:
        if x == b'132043019\r\n' or x == b'132043019':
            correctOutputBool.append(True)
        else:
            correctOutputBool.append(False)


def workbook():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test1')
    for x in range(len(students)):
        ws.write(x + 1, 0, students[x])
    for x in range(len(codeOutputs)):
        ws.write(x + 1, 1, str(codeOutputs[x]))
    for x in range(len(runTime)):
        ws.write(x + 1, 2, runTime[x])
    for x in range(len(language)):
        ws.write(x + 1, 3, language[x])
    for x in range(len(correctOutputBool)):
        ws.write(x + 1, 4, correctOutputBool[x])
    ws.write(0, 0, 'Student Name', xlwt.easyxf('font: bold 1'))
    ws.write(0, 1, 'Code Output', xlwt.easyxf('font: bold 1'))
    ws.write(0, 2, 'Code Runtime', xlwt.easyxf('font: bold 1'))
    ws.write(0, 4, 'Correct Output', xlwt.easyxf('font: bold 1'))
    ws.write(0, 3, 'Language', xlwt.easyxf('font:bold 1'))
    os.chdir(owd)
    try:
        wb.save("examplew.xls")
    except:
        wb.save("example2.xls")
        print("Workbook Was not able to be Created")


def final():
    getFiles()
    correctOutput()
    workbook()


final()
print(codeOutputs)
