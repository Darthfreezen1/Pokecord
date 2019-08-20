import random

#Plays a slot machine game with up to 5 rows
#rows_selected: how many rows will count for payout. Also how many coins it takes to play!
def play_slots(rows_selected):

    slot_items = ["7", "R", "PIKA", "PSY", ">O<", ":P", "CHERI"]

    payouts = [300, 100, 15, 8, 6, 2]

    text_return = ""

    if rows_selected == 1:
        row = [slot_items[random.randint(0, 6)], slot_items[random.randint(0, 6)], slot_items[random.randint(0, 6)]]
        text_return = f"[ {row[0]} ] [ {row[1]} ] [ {row[2]} ]"
        payout = check_horizontal_row(row)
        if(payout == 0):
            text_return += "\nYou lost!"
        else:
            text_return += f"\nYou won {payout} coins!"
    elif rows_selected == 2:
        row = [slot_items[random.randint(0, 6)], slot_items[random.randint(0, 6)], slot_items[random.randint(0, 6)]]
        row1 = [slot_items[random.randint(0, 6)], slot_items[random.randint(0, 6)], slot_items[random.randint(0, 6)]]
        text_return = f"[ {row[0]} ] [ {row[1]} ] [ {row[2]} ]\n[ {row1[0]} ] [ {row1[1]} ] [ {row1[2]} ]"
        payout = (check_horizontal_row(row)+check_horizontal_row(row1))
        if(payout == 0):
            text_return += "\nYou lost!"
        else:
            text_return += f"\nYou won {payout} coins!"
    elif rows_selected == 3:
        table = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                table[i][j] = slot_items[random.randint(0,6)]
        
        for r in table:
            for c in r:
                text_return+= f"[  {c}  ]"
            text_return+="\n"
        
        payout = check_horizontal_row(table) + check_vertical_rows(table)

        if payout == 0:
            text_return+="\nYou lost!"
        else:
            text_return+=f"\nYou won {payout}!"
               
            
        
    return text_return


def check_horizontal_row(a):
    if a[0] == "7" and a[1] == "7" and a[2] == "7":
        return 300
    elif a[0] == "R" and a[1] == "R" and a[2] == "R":
        return 100
    elif a[0] == "PIKA" and a[1] == "PIKA" and a[2] == "PIKA":
        return 15
    elif a[0] == "PSY" and a[1] == "PSY" and a[2] == "PSY":
        return 15
    elif a[0] == ">O<" and a[1] == ">O<" and a[2] == ">O<":
        return 8
    elif a[0] == ":P" and a[1] == ":P" and a[2] == ":P":
        return 8
    elif a[0] == "CHERI" and a[1] == "CHERI":
        return 6
    elif a[1] == "CHERI" and a[2] == "CHERI":
        return 6
    elif "CHERI" in a:
        return 2
    else:
        return 0

def check_diagonal_row(a):
    #0-8 index
    #[0][1][2]
    #[3][4][5]
    #[6][7][8]

    if a[0] == "7" and a[4] == "7" and a[8] == "7":
        return 300
    elif a[2] == "7" and a[4] == "7" and a[6] == "7":
        return 300
    elif a[0] == "R" and a[4] == "R" and a[8] == "R":
        return 100
    elif a[2] == "R" and a[4] == "R" and a[6] == "R":
        return 100
    elif a[0] == "PIKA" and a[4] == "PIKA" and a[8] == "PIKA":
        return 15
    elif a[2] == "PIKA" and a[4] == "PIKA" and a[6] == "PIKA":
        return 15
    elif a[0] == "PSY" and a[4] == "PSY" and a[8] == "PSY":
        return 15
    elif a[2] == "PSY" and a[4] == "PSY" and a[6] == "PSY":
        return 15
    elif a[0] == ">O<" and a[4] == ">O<" and a[8] == ">O<":
        return 8
    elif a[2] == ">O<" and a[4] == ">O<" and a[6] == ">O<":
        return 8
    elif a[0] == ":P" and a[4] == ":P" and a[8] == ":P":
        return 8
    elif a[2] == ":P" and a[4] == ":P" and a[6] == ":P":
        return 8
    elif a[0] == "CHERI" and a[4] == "CHERI":
        return 6
    elif a[4] == "CHERI" and a[8] == "CHERI":
        return 6
    elif a[6] == "CHERI" and a[4] == "CHERI":
        return 6
    elif a[2] == "CHERI" and a[4] == "CHERI":
        return 6
    elif "CHERI" in a:
        return 2
    else:
        return 0

def check_vertical_rows(a):
    #0-8 index
    #[0][1][2]
    #[3][4][5]
    #[6][7][8]

    if a[0] == "7" and a[3] == "7" and a[6] == "7":
        return 300
    elif a[1] == "7" and a[4] == "7" and a[7] == "7":
        return 300
    elif a[2] == "7" and a[5] == "7" and a[8] == "7":
        return 300
    elif a[0] == "R" and a[3] == "R" and a[6] == "R":
        return 100
    elif a[1] == "R" and a[4] == "R" and a[7] == "R":
        return 100
    elif a[2] == "R" and a[5] == "R" and a[8] == "R":
        return 100
    elif a[0] == "PIKA" and a[3] == "PIKA" and a[6] == "PIKA":
        return 15
    elif a[1] == "PIKA" and a[4] == "PIKA" and a[7] == "PIKA":
        return 15
    elif a[2] == "PIKA" and a[5] == "PIKA" and a[8] == "PIKA":
        return 15
    elif a[0] == "PSY" and a[3] == "PSY" and a[6] == "PSY":
        return 15
    elif a[1] == "PSY" and a[4] == "PSY" and a[7] == "PSY":
        return 15
    elif a[2] == "PSY" and a[5] == "PSY" and a[8] == "PSY":
        return 15
    elif a[0] == ">O<" and a[3] == ">O<" and a[6] == ">O<":
        return 8
    elif a[1] == ">O<" and a[4] == ">O<" and a[7] == ">O<":
        return 8
    elif a[2] == ">O<" and a[5] == ">O<" and a[8] == ">O<":
        return 8
    elif a[0] == ":P" and a[3] == ":P" and a[6] == ":P":
        return 8
    elif a[1] == ":P" and a[4] == ":P" and a[7] == ":P":
        return 8
    elif a[2] == ":P" and a[5] == ":P" and a[8] == ":P":
        return 8
    elif "CHERI" in a:
        return 2
    else:
        return 0


