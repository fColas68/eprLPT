import urllib.request
import os
import pathlib
import gzip

def zipFolder():
    return "./gz"  # curDir+"/gz"

def logFolder():
    return "./log" # curDir+"/log"

def pwaFileImport(webRetrieve=False, unzipfiles=True, maxFiles = 5):
    tabFiles = []
    
    #-------------------------------
    # script's directory
    # Create requested directories
    #curDir = os.path.abspath(os.curdir) 
    #-------------------------------
    zipDir = zipFolder()
    logDir = logFolder()
    
    if not os.path.exists(zipDir):
        os.makedirs(zipDir)
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    
    #-------------------------------
    # Web resource web --> zipDir
    #-------------------------------
    if webRetrieve:
        # read distant file
        fichierNom = "https://www.cs.huji.ac.il/labs/parallel/workload/logs-list"
        req = urllib.request.Request(url=fichierNom) 
        fichierId = urllib.request.urlopen(req)

        # put the list on a list tabFiles
        contentsLine = fichierId.readline().decode('utf-8')
        while contentsLine:
            tabFiles.append(contentsLine.rstrip("\n")) # erase \n caracter from the string 
            contentsLine = fichierId.readline().decode('utf-8')

        # close the file
        fichierId.close()
        
        # now i have my list of pwa gz logs
        n=0
        for file in tabFiles:
            n+=1
            if (n > maxFiles or maxFiles==0):
                break
            fileInfo = pathlib.Path(file)
            # destFile = os.path.join(zipDir, fileInfo.name)
            destFile = zipDir+"/"+fileInfo.name
            urllib.request.urlretrieve(file, destFile)
            print("file ========> "+destFile+" retrieved.")

            if unzipfiles == True:
                unzipGZ(fileInfo.name, zipDir, logDir)
                    
def unzipGZ(fileNameGZ, fromDir, destDir):
    #
    fromFile = fromDir+"/"+fileNameGZ
    destFile = destDir+"/"+fileNameGZ.rstrip(".gz")
    #
    print("Unzipping file %s in %s" % (fromFile, destDir))
    #
    src = gzip.GzipFile(fromFile, 'rb')
    s = src.read()
    src.close()
    d = open(destFile, 'wb')
    d.write(s)
    d.close()
    print("Unzipped.")


def pwaFileRead(fileName):
    with open(fileName, 'r') as f:
        text = f.read()
    # END WITH    
    times = []
    for line in text.split('\n'):
        line = line.strip()
        if not(line) or line[0] == ";":
            continue
        # END IF
        jobId, submitTime, waitTime, runTime, nbProc, avgCPUtime, mem, reqProc, reqTime, reqMem, status, uId, gId, appId, queueId, partitionId, precedingJob, timefromPrecedingJob = [float(x) for x in line.split()]
        if runTime != 0:
            # times += [runTime]
            times.append(runTime)
        # END IF
    # END FOR
    return times

def pwaFileChoice():
    files = []
    logDir = logFolder()
    content = os.listdir(logDir)
    for item in content:
        r = int(input("Use this file %s ? (1 yes 0 no) : " % (item)))
        if r == 1:
            files.append(logDir+"/"+item)
        # END IF
    # END FOR
    print(files)
    return files

#pwaFileImport(True, True)
# haha = pwaFileRead(logFolder()+"/NASA-iPSC-1993-3.1-cln.swf")
# print(haha)
# pwaFileChoice()


