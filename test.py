def WriteData(balance):
    with open("data.txt","w") as f:
        f.write(balance)
        f.close()


WriteData("100")