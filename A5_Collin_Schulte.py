#define base structure
def MAIN():
    HOLE = int(input("Enter the number of the hole: "))
    PAR = int(input("Enter the par value for the hole: "))
    STROKE = float(input("Enter the number of strokes it took to finish the hole: "))
    print("on hole number",HOLE ,"a par",PAR ,"you shot",STROKE2PAR(STROKE,PAR) ,STROKESLANG(STROKE)) 
#find stroke to par value
def STROKE2PAR(STROKE,PAR):
    A = "If you see this something went wrong with Stroke2Par"
    if STROKE - PAR == -5:
        A = "Ostrich"
    elif STROKE - PAR == -4:
        A = "Condor"
    elif STROKE - PAR == -3:
        A = "Albatross"
    elif STROKE - PAR == -2:
        A = "Eagle"
    elif STROKE - PAR == -1:
        A = "Birdie"
    elif STROKE - PAR == 0:
        A = "par"
    elif STROKE - PAR == 1:
        A = "Bogey"
    elif STROKE - PAR == 2:
        A = "Double Bogey"
    elif STROKE - PAR == 3:
        A = "Triple Bogey"
    elif STROKE - PAR == 4:
        A = "4 over par"
    elif STROKE - PAR == 5:
        A = "5 over par"
    elif STROKE - par > 5:
        A = "way to many "
    elif STROKE - par < -5:
        A = "so low"
    else:
        A = "."
    return A
#find slang fitting to stroke
def STROKESLANG(STROKE):
    B = "If you see this something went wrong with StrokeSlang"
    if STROKE == 1:
        B = "a Hole in one"
    if STROKE == 4:
        B = "a Sailboat"
    if STROKE == 8:
        B = "a Snowman"
    if STROKE == 10:
        B = "Bo Derek"
    else:
        B = "."
    return B



MAIN()
