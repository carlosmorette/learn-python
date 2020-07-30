import json

print("==== Save Tools ====")

arquive = open("tools.json", "r")

newArquiveDict = json.loads(arquive.read())


def createNewTool():
    nameTool = input("Tool name: ")
    descriptionTool = input("Description tool: ")

    links = []
    moreLink = "s"

    while moreLink == "s":
        link = input("Paste a useful link: ")
        moreLink = input("More links [s/n]: ")

    links.append(link)

    return {
      "nameTool": nameTool,
      "descriptionTool": descriptionTool,
      "links": links
    }


newArquiveDict.append(createNewTool())

arquive = open("tools.json", "w")


arquive.write(json.dumps(newArquiveDict))
arquive.close()
print("{0}Saved tool!{0}".format("\033[1;32m"))
