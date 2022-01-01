import os 

ep_LINK = input("Drag the EOISODE Folder! : ")

first_part = input("First Part :")
last_part = input("Last Part :")

first_part = int(first_part)
last_part = int(last_part) 

os.chdir(r"{}".format(ep_LINK))

startName = []
finishName = []
Origin_Episode = []
EpisodeChecker = []


for s in os.listdir():

    Origin_Episode.append(s)

    Ep_name , EPext = os.path.splitext(s)

    EpisodeChecker.append(Ep_name)
    
    startName.append(Ep_name[:first_part])
    finishName.append(Ep_name[last_part:])

    
sub_Name = input("Drag the SUBTITLES Folder! : ")

First_part = input("First Part :")
Last_part = input("Last Part :")

First_part = int(First_part)
Last_part = int(Last_part)

os.chdir(r"{}".format(sub_Name))

i = 0

for f in os.listdir():
    sub_name , sub_ext = os.path.splitext(f)
    ep_num = sub_name[First_part:Last_part].zfill(2)

    newSub_name = '{}{}{}{}'. format(startName[i], ep_num, finishName[i], sub_ext)
    checkerSub = '{}{}{}'. format(startName[i], ep_num, finishName[i])

    # os.rename(f , newSub_name)

    # print(f , "=>" ,ep_num , "=>" ,newSub_name)

    print(newSub_name , " => " , Origin_Episode[i])

    print("Equalivance is : " , checkerSub == EpisodeChecker[i] )

    i += 1

nextStep = input("Do you want to continue? (y/n): ")

if nextStep == "y" or "Y":
    i = 0

    for t in os.listdir():
        sub_name , sub_ext = os.path.splitext(t)
        ep_num = sub_name[First_part:Last_part].zfill(2)

        newSub_name = '{}{}{}{}'. format(startName[i], ep_num, finishName[i], sub_ext)

        os.rename(t , newSub_name)

        print(t , "=>" ,ep_num , "=>" ,newSub_name)

        i += 1
if nextStep == "n" or "N":
    print("OK, try again and make better settings!")
