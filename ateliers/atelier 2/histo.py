from recherche import a_repetitions
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen


def listDupsUnique(listNums):
	return list(unique_everseen(duplicates(listNums)))



def injective(X,Y):
    if not a_repetitions(Y) and not a_repetitions(X):
        return True
    else:
        T = list(unique_everseen(duplicates(X)))
        U = list(unique_everseen(duplicates(Y)))
        

