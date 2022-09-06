def est_bissextile(an:int):
    if(an%4==0 and an%100!=0 or an%400==0):
        return True
    else:
        return False


def test_biss(tab:list):
    for i in tab:
        print(est_bissextile(i))


#tab = [2003,2009,2004,1997,2000]
#test_biss(tab)
#print(est_bissextile(2000))

