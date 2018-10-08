# Hangman
import random

list_vegi=[]
with open ("dict_vegi_frut.txt", "r", encoding="utf-8") as f:
    list_vegi=f.read().split()

def hangman(word):
    wrong=0
    stages=["",
            "-----------            ",
            "|                  |            ",
            "|                ('_')           ",
            "|               ／|＼         ",
            "|                ／＼         ",
            "|                                "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ！")

    while wrong < len(stages)-1:
        print("\n")
        msg="文字予想してね。"
        char=input(str(len(word))+msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}。".format(word))

random_word=random.choice(list_vegi)
hangman(random_word)
    
