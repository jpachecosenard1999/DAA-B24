def galeShappley(mens: list, mpreferences: list, wpreferences: list, womens: list):
    man_fiance = [None for _ in womens] #pareja actual del hombre
    woman_fiance = [None for _ in mens] #pareja actual de la mujer
    number_of_trials = [0 for _ in womens] #proposiciones echas por los hombres
    singles = mens.copy() #todos los hombres están solteros al inicio
    pairs = {} #parejas finales
    while singles:
        man = singles.pop()
        mpref = mpreferences[man]
        woman = mpref[number_of_trials[mens.index(man)]] #siguiente mujer en la lista de preferencias
        number_of_trials[mens.index(man)] +=1
        if woman_fiance[womens.index(woman)] is None: #si la mujer está soltera
            woman_fiance[womens.index(woman)] = man
            man_fiance[mens.index(man)] = woman
            pairs[man] = woman
        else: #sino está soltera revisar sus preferencias
            actual_man =  woman_fiance[womens.index(woman)]
            wpref = wpreferences[woman]
            if wpref[man] < wpref[actual_man]: #Gordo tenemos que hablar
                woman_fiance[womens.index(woman)] = man
                man_fiance[mens.index(man)] = woman
                singles.append(actual_man)
                pairs[man] = woman
            else: #rechaza al hombre
                singles.append(man)
    
    return pairs


mens = ["Angel", "Bruno", "Carlos"]
womens = ["Ana", "Beatriz", "Celia"]
mpreferences = {"Angel": {0: "Ana", 1: "Beatriz", 2: "Celia"}, "Bruno": {0: "Beatriz", 1: "Ana", 2: "Celia"}, "Carlos": {0: "Ana", 1: "Beatriz", 2: "Celia"}}
wpreferences = {"Ana": {"Bruno": 0, "Angel": 1, "Carlos": 2}, "Beatriz": {"Angel": 0, "Bruno": 1, "Carlos": 2}, "Celia": {"Angel": 0, "Bruno": 1, "Carlos": 2}}

pairs = galeShappley(mens, mpreferences, wpreferences, womens)

print(pairs)

