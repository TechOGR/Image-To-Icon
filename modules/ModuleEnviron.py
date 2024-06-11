from subprocess import run

def createEnviron():
    run(
        [
            "cmd",
            "/c",
            "setx",
            "IMGICON",
            "nothing"
        ],
        shell=True
    )

def setCurrentEnviron():
    run(
        [
            "cmd",
            "/c",
            "setx",
            "IMGICON",
            "nothing"
        ],
        shell=True
    )

def getValueEnviron():
    
    subProcess = run(
        [
            "cmd.exe",
            "/c","echo",
            "%IMGICON%"
        ],
        shell=True,
        capture_output=True
    )

    output = subProcess.stdout.decode("utf-8")[:-2]
    
    return output

def checkingValue():
    
    valueEnviron = getValueEnviron()
    
    if len(valueEnviron) == "nothing":
        run(
            [
                "msg",
                "*",
                """No se ha establecido ninguna opción\n
                Puede hacerlo desde el menú de Settings"""
            ],
            shell=True
        )
    elif valueEnviron == "Current":
        ...
    else:
        print(valueEnviron)

checkingValue()