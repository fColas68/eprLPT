import urllib.request
import os
import pathlib
import gzip

import setup as s

# ##################################################################
# pwaFileImport
# ##################################################################
def pwaFileImport(webRetrieve=False, unzipfiles=True, maxFiles = 5):
    """
    Import files froms website https://www.cs.huji.ac.il
    Logs (of real life) of set of job times.
    Retrieve file catalog : address setted in constant s.URL_CATALOG_PWA
    reads this file which contains the url addresses of the time files
    and each file is retreived in the folder FOLDER_ZIPPEDLOG,
    to be unzipped in the folder FOLDER_PWA
    input
        :param webRetrieve: True : retreive files from website.
        :param unzipfiles : True : unzip files from zippedLog folder to PWA folder
        :param maxFiles   : number of files to retreive from website.
                            use 0 to retreive all files
    """
    tabFiles = []

    #-------------------------------
    # log directory
    # s.folder creates requested directories if not exists
    # curDir = os.path.abspath(os.curdir)
    #-------------------------------
    zipDir = s.folder(s.FOLDER_ZIPPEDLOG)
    logDir = s.folder(s.FOLDER_PWA)
    
    #-------------------------------
    # Web resource web --> zipDir
    #-------------------------------
    if webRetrieve:
        # read distant file
        fichierNom = s.URL_CATALOG_PWA # url of files log catalog 
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
# ##################################################################
# unzipGZ
# ##################################################################
def unzipGZ(fileNameGZ, fromDir, destDir):
    """
    Unzip the file named fromDir+fileNameGZ
    in the folder destDir. 
    """
    #
    fromFile = fromDir+s.sepDir()+fileNameGZ
    destFile = destDir+s.sepDir()+fileNameGZ.rstrip(".gz")
    #
    print("Unzipping file %s in %s" % (fromFile, destDir))
    #
    src = gzip.GzipFile(fromFile, 'rb')
    sRead = src.read()
    src.close()
    d = open(destFile, 'wb')
    d.write(sRead)
    d.close()
    print("Unzipped.")

# ##################################################################
# pwaFileRead
# ##################################################################
def pwaFileRead(fileName):
    """
    Reads the log file according to the predefined format,
    to create an instance (set of times)
    called from matrix.py
    """
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
# ##################################################################
# pwaFileChoice():
# ##################################################################
def pwaFileChoice():
    """
    finds the files contained in the "FOLDER_PWA" directory,
    and proposes to choose them, or not (for test instance creation).
    Returns the list of selected files as a list files[]
    """
    files = []
    logDir = s.folder(s.FOLDER_PWA)
    content = os.listdir(logDir)
    for item in content:
        r = int(input("Use this file %s ? (1 yes 0 no) : " % (item)))
        if r == 1:
            files.append(logDir+s.sepDir()+item)
        # END IF
    # END FOR
    print(files)
    return files

##FOR TEST THIS SCRIPT
##pwaFileImport(True, True)
##logTimes = pwaFileRead(logFolder()+"/NASA-iPSC-1993-3.1-cln.swf")
##print(logTimes)
##pwaFileChoice()


