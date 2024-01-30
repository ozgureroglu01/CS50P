def main():
    userInput = input("File name: ").strip().lower()
    fileFormat = userInput[-4:]
    print(extensions(fileFormat))

def extensions(fileFormat):
    match fileFormat:
        case ".gif":
            return "image/gif"
        case "jpeg" |".jpg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"



main()
