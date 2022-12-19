#This project requires "download". Use this script: "pip3 install download".
from download import download

print("Windows Downloader (Chinese) \nChoose a channel:\n1. Stable\n2. Release Preview\n3. Beta\n4. Dev\n5. Exit")
a = input("Your choice: ")

if a == "1":
    print("Choose a version:\n1. Windows 10\n2. Windows 8.1")
    x = input("Your choice: ")
    if x == "1":
        print("Choose a structure:\n1. 64-bit\n2. 32-bit")
        y = input("Your choice: ")
        if y == "1":
            url = "https://software.download.prss.microsoft.com/sg/Win10_21H2_Chinese(Simplified)_x64.iso?t=e35a08f9-b7a6-400e-9c2a-79bda4e338e2&e=1652928527&h=e0be1a8b641b7545c0dacd6d03f25200acec314b080d837914a56e46f0cef847"
            path = download(url, "Downloads")
        elif y == "2":
            url = "https://software.download.prss.microsoft.com/sg/Win10_21H2_Chinese(Simplified)_x32.iso?t=e35a08f9-b7a6-400e-9c2a-79bda4e338e2&e=1652928527&h=cab37da4b1b95ca7c2262378d9004a7dd9c2c21ae46f3cc2984cc5b4d0826bd7"
            path = download(url, "Downloads")
    elif x == "2":
        print("Choose a structure:\n1. 64-bit\n2. 32-bit")
        y = input("Your choice: ")
        if y == "1":
            url = "https://software.download.prss.microsoft.com/dbazure/Win8.1_Chinese(Simplified)_x64.iso?t=150c7715-296d-4dfd-b3fc-c00ba939126a&e=1652928861&h=0126dd1508c75bf130774cac003e82d697811a96304395a526b9885063c3556c"
            path = download(url, "Downloads")
        elif y == "2":
            url = "https://software.download.prss.microsoft.com/dbazure/Win8.1_Chinese(Simplified)_x32.iso?t=150c7715-296d-4dfd-b3fc-c00ba939126a&e=1652928861&h=ebcc5543ced08bd4f010426adbd7649c50323cdf2a93e9ec09f8ff8dd8b4f482"
            path = download(url, "Downloads")
elif a == "2":
    print("Choose a version:\n1. Windows 10 Insider Preview\n2. Windows Server Insider Preview")
    x = input("Your choice: ")
    if x == "1":
        print("Choose a structure:\n1. 64-bit\n2. 32-bit")
        y = input("Your choice: ")
        if y == "1":
            url = "https://software.download.prss.microsoft.com/pr/Windows10_InsiderPreview_Client_x64_zh-cn_19044.1288.iso?t=c9dbf901-d584-4112-849c-fae318d98f78&e=1652931322&h=1744bb1477ad4f85ab2c4d342ec103cbe8f5a80540d69e2b8a9e46d6bede2350"
            path = download(url, "Downloads")
        elif y == "2":
            url = "https://software.download.prss.microsoft.com/pr/Windows10_InsiderPreview_Client_x32_zh-cn_19044.1288.iso?t=c9dbf901-d584-4112-849c-fae318d98f78&e=1652931322&h=5e3c53d7313de4db6170564e2e7fa74f5a83531d303b3d3f8b5254908da3cfb6"
            path = download(url, "Downloads")
    elif x == "2":
        print("Choose a type:\n1. Windows Server vNext LTSC Previews - Build 25110 Chinese\n2. Microsoft Server Language and Optional Features Preview - Build 25110 English")
        y = input("Your choice: ")
        if y == "1":
            url = "https://software.download.prss.microsoft.com/dbazure/Windows_InsiderPreview_Server_vNext_zh-cn_25110.iso?t=8b583b2a-e4fc-4fa8-ad10-6ccb35809e04&e=1652931414&h=4839c658e1bf70cc960fe650569d2ebd5b3076302b5a914c2cbe8a2db1a57ea8"
            path = download(url, "Downloads")
        elif y == "2":
            url = "https://software.download.prss.microsoft.com/dbazure/Microsoft_Server_InsiderPreview_LangPack_FOD_25110.iso?t=0199a276-f085-4a03-81d6-ab4a5e484d23&e=1652931549&h=e78ac513f5179efa6ebd9eb42c061c0cb39d3ef5a0039a49a9bbb4d9ae359a0c"
            path = download(url, "Downloads")
elif a == "3":
    print("Choose a version:\n1. Windows 11 Insider Preview\n2. Windows 11 on ARM Insider Preview")
    y = input("Your choice: ")
    if y == "1":
        print("Downloading 64-bit Windows...")
        url = "https://software.download.prss.microsoft.com/dbazure/Windows11_InsiderPreview_Client_x64_zh-cn_22621.iso?t=ad1f92e7-f40d-4963-8332-a7dba1c1effb&e=1652931777&h=965942d25a85ca24a98a9fce2398383b5c02b7a26df9549a4f7d48597d4ddd84"
        path = download(url, "Downloads")
    elif y == "2":
        print("Downloading Windows 11 on ARM (en-us) VHDX file...")
        url = "https://software.download.prss.microsoft.com/dbazure/Windows11_InsiderPreview_Client_ARM64_en-us_22598.VHDX?t=c534c3c6-fb37-453d-bf70-96a3f48e8454&e=1652931937&h=9e5a77e4b7057d8ce21d808c5960851d01f59b3cbdff0873ce8a6ab206e26653"
        path = download(url, "Downloads")
elif a == "4":
    print("Downloading Windows 11 Insider Preview (Dev Channel) - Build 22598 (64-bit)...")
    url = "https://software.download.prss.microsoft.com/dbazure/Windows11_InsiderPreview_Client_x64_zh-cn_22598.iso?t=17267db8-88f6-4285-8fa4-c421db9de876&e=1652932083&h=e71d42c197bdcad011fbbee5da366e9842418b54bc9a4a4f90e58073336177f8"
    path = download(url, "Downloads")
elif a == "5":
    exit(0)
