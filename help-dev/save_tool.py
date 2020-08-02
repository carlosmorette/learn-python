import json

path = "tools.json"  # path to json

print("==== Save Tools ====")
with open(path) as tools_json:
    arquive = json.load(tools_json)

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

    arquive.append(createNewTool())

    with open(path, "w") as newArquive:
        newArquive.write(json.dumps(arquive))
        print("{0}Saved tool!{0}".format("\033[1;32m"))
