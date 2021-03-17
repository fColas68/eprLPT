import pwa

def main():
    print("How many files max to retreive from Parallel Workload Archive ? ")
    maxFiles = int(input("0 for all : "))
    pwa.pwaFileImport(True, True, maxFiles)
    
if __name__ == "__main__":
    main()

    
    
