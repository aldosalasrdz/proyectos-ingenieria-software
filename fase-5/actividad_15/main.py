from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)


@app.route("/")
def search():
    word = request.args.get("word", "").lower()

    if os.path.basename(os.getcwd()) == "actividad_15":
        root_directory = os.path.abspath("../..")
    else:
        root_directory = os.path.abspath("./")

    # Se lee el diccionario
    with open(os.path.join(root_directory, "dictionary.txt"), "r") as Dic:
        DicLines = Dic.readlines()
        Dic.close()

    # Se lee el posting
    with open(os.path.join(root_directory, "newPosting.txt"), "r") as Pos:
        PosLines = Pos.readlines()
        Pos.close()

    # Se lee el documents
    with open(os.path.join(root_directory, "Documents.txt"), "r") as Doc:
        DocLines = Doc.readlines()
        Doc.close()

    files = []
    for line in DicLines:
        rowWord = line.split(";")[0]
        if word == rowWord:
            rowRep = int(line.split(";")[1])
            rowPos = int(line.split(";")[2])

            for i in range(rowPos, (rowPos + rowRep)):
                fileId = int(PosLines[i].split()[0]) - 1
                # FileRep = el peso del token
                fileRep = str(PosLines[i].split()[1])
                file = DocLines[fileId].split()[1]

                file_path = os.path.join("templates", file)

                files.append((file, file_path, fileRep))

            files.sort(key=lambda a: a[2], reverse=True)
            files = files[:10]

            break

    return render_template("index.html", word=word, files=files, sa="sa")


@app.route("/files/<path:filename>")
def view_file(filename):
    return send_file(filename)


if __name__ == "__main__":
    app.run(debug=True)
