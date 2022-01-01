import os

class ep:
    def __init__(self ,ep_File, ep_F, ep_L):
        self.ep_L = ep_L
        self.ep_F = ep_F
        self.ep_File = ep_File
        self.startName = []
        self.finishName = []
        self.Origin_Episode = []
        self.EpisodeChecker = []
    
    def __iter__(self):
        return self

    def epcwd(self):
        return os.chdir(r"{}".format(self.ep_File))

ep_LINK = input("Drag the EOISODE Folder! : ")

first_part = input("First Part :")
last_part = input("Last Part :")

print(ep_LINK)

episodes = ep(ep_LINK , int(first_part), int(last_part))
episodes.epcwd()

for s in os.listdir():

    episodes.Origin_Episode.append(s)

    Ep_name , EPext = os.path.splitext(s)

    episodes.EpisodeChecker.append(Ep_name)
    
    episodes.startName.append(Ep_name[:episodes.ep_F])
    episodes.finishName.append(Ep_name[episodes.ep_L:])


sub_Name = input("Drag the SUBTITLES Folder! : ")

First_part = input("First Part :")
Last_part = input("Last Part :")

subtitles = ep(sub_Name , int(First_part), int(last_part))
subtitles.epcwd()

i = 0

for f in os.listdir():
    sub_name , sub_ext = os.path.splitext(f)
    ep_num = sub_name[subtitles.ep_F:subtitles.ep_L].zfill(2)

    newSub_name = '{}{}{}{}'. format(episodes.startName[i], ep_num, episodes.finishName[i], sub_ext)
    checkerSub = '{}{}{}'. format(episodes.startName[i], ep_num, episodes.finishName[i])

    print(newSub_name , " => " , episodes.Origin_Episode[i])

    print(checkerSub ," => Testing Equivalance.. => " ,  episodes.EpisodeChecker[i] )

    print("Equalivance is : " , checkerSub == episodes.EpisodeChecker[i] )

    i += 1

    if i == len(episodes.EpisodeChecker):
        print("done!")
    else :
        print("Keep digin..")




        