# Implémentation des dates et calendriers
# Implémentation des tests (voir main en fin de fichier)



from typing import ChainMap, Dict, List, Tuple, NoReturn


#varibale global
mois_dict = {1:'janvier',2:'fevrier',3:'mars',4:'avril',5:'mai',6:'juin',7:'juillet',8:'aout',9:'september',10:'october', 11:'november',12:'december'}


# =============================================================================
def est_bissextile(annee: int) -> bool :
    """
    retourne vrai si l'année est bissextile

    >>> est_bissextile(2020)
    True
    >>> est_bissextile(2021)
    False
    >>> est_bissextile(2022)
    False
    >>> est_bissextile(1900)
    False
    >>> est_bissextile(2000)
    True
    """ 
    modulo4 = annee%4
    modulo100 = annee%100
    modulo400 = annee%400
    #les conditions pour lesquelles une année bissetile
    if modulo4 == 0 and modulo100!= 0 or modulo400 ==0:
        return True
    else:
        return False 


    
# =============================================================================
def cree_date(j: int, m: int, a: int) -> Dict :
    """
    Crée une date à partir des entiers la décrivant.
    Si l'un des paramètres n'est pas un entier, la fonction retournera None

    >>> cree_date(15,12,2020)
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> cree_date(1.5,12,2020)

    """
    if type(j) == int and type(m) == int and type(a) == int:
        return {'jour' : j ,'mois': m, 'annee': a}






    
# =============================================================================
def copie_date(date: Dict) -> Dict :
    """
    copie la date passée en paramètre

    Args:
        date (dict) : date 

    >>> copie_date({'jour': 1, 'mois': 2, 'annee': 3})
    {'jour': 1, 'mois': 2, 'annee': 3}
    >>> copie_date({'jour': 2, 'mois': 6, 'annee': 2022})
    {'jour': 2, 'mois': 6, 'annee': 2022}
    >>> copie_date({'jour': 19, 'mois': 12, 'annee': 1950})
    {'jour': 19, 'mois': 12, 'annee': 1950}
    """
    return cree_date(date['jour'],date['mois'],date['annee'])



    
# =============================================================================
def compare(d1: Dict, d2: Dict) -> int :
    """
    Permet de classer deux dates.
    Retourne
    -1 si la date d1 < d2
    +1 si la date d1 > d2
    0 si les dates sont identiques
    on considère que les dates sont croissantes 
    dans l'ordre chronologique

    Args:
        d1 (dict) : Une date
        d2 (dict) : deuxième date

    >>> date1 = cree_date(25,12,2021)
    >>> date2 = cree_date(31,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    """
    if d1['annee'] > d2['annee']:
        return +1
    elif d1['annee'] < d2['annee']:
        return -1
    elif d1['mois'] > d2['mois']:
        return +1
    elif d1['mois'] < d2['mois']:
        return -1
    elif d1['jour'] > d2['jour']:
        return +1
    elif d1['jour'] < d2['jour']:
        return -1
    #comme on a tester tout les possibilité il reste que l'égalité entre l'année le mois et le jour donc pas besoin de le faire
    return 0


# =============================================================================
def valide_simple(d: Dict) -> bool :
    """   
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - si le premier (le jour) est un entier compris entre 1 et 31
    - si le second (le mois) est un entier compris entre 1 et 12
    Args:
        d(dict) : date
    
    Returns
        bool
    >>> date = cree_date(1, 2, 0)
    >>> valide_simple(date)
    True
    >>> date = cree_date(1.5, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(0, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(20, 8, 2021)
    >>> valide_simple(date)
    True
    """
    if d == None:
        return False


    if d['jour'] <= 31 and d['jour'] >=1  and  d['mois'] <= 12 and d['mois'] >= 1:
        return True 
    else:
        return False
    


# =============================================================================
def valide_complet(d: Dict) -> bool :
    """ 
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - la validation simple est vraie
    - si la date représente une date réelle

    Args:
        d(dict) : date
    
    Returns
        bool

    >>> date = cree_date(15, 1, 2022)
    >>> valide_complet(date)
    True
    >>> date = cree_date(32, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(-1, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(31, 6, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(29, 2, 2020)
    >>> valide_complet(date)
    True
    >>> date = cree_date(29, 2, 2022)
    >>> valide_complet(date)
    False
    """
    if valide_simple(d):
        #tout les mois de 30 jours
        if d['mois'] == 4 or d['mois'] == 6 or d['mois'] == 9 or d['mois'] == 11:
            if d['jour']<=30 and d['jour'] >= 1:
                return True
            else:
                return False
        #tout les mois de 31 jours
        if d['mois'] == 1 or d['mois'] == 3 or d['mois'] == 5 or d['mois'] == 7 or d['mois'] == 8 or d['mois'] == 10 or d['mois'] == 12:
            if d['jour']<=31 and d['jour'] >= 1:
                return True
            else:
                return False
        #verif de l'année bissextile
        if est_bissextile(d['annee']):
            #le mois de fevrier
            if d['mois'] == 2:
                #si l'anne bissextille et qu'on est en février il doit avoir entre 1 à 29 jours
                if d['jour'] <= 29 and d['jour'] >= 1:
                    return True
                else:
                    return False
        if not est_bissextile(d['annee']):
            if d['mois'] == 2:
                #si l'anne n'est pas bissextille et qu'on est en février il doit avoir entre 1 à 29 jours
                if d['jour'] <= 28 and d['jour'] >= 1:
                    return True
                else:
                    return False
            
    return False        

# =============================================================================




# =============================================================================
def ajoute_calendrier(calendrier: List, date: Dict, description: str ) -> NoReturn :
    """ajoute un élément à la liste du calendrier.

    Args:
        calendrier (List): date avec les evenement
        date (Dict): date des evenement
        description (str): l'evenement du jour

    Returns:
        NoReturn
        
    >>> ajoute_calendrier([],{'jour': 1, 'mois': 1, 'annee': 2022}, 'Jour de l an')
    
    """
    if valide_complet(date):
        
        evenement = "Le {}/{}/{} : {}".format(date['jour'],date['mois'],date['annee'], description)
        calendrier.append(evenement)
        


    
# =============================================================================
def affiche_calendrier(calendrier: List) -> NoReturn :
    """affiche le calendrier sous forme de liste.

    Args:
        calendrier (List): date d'evenement

    Returns:
        NoReturn
    
    """
    for i in range (len(calendrier)):
        print(calendrier[i])


# ============================================================================= 
def calcule_jour(date : dict) -> str:
    """Donne le jour de la semaine de la date

    Args:
        date (dict): une date

    Returns:
        str: jour de la semaine

    >>> date = cree_date(2,6,2003)
    >>> calcule_jour(date)
    'lundi'
    >>> date = cree_date(8,12,2021)
    >>> calcule_jour(date)
    'mercredi'
    >>> date = cree_date(13,3,2004)
    >>> calcule_jour(date)
    'samedi'
    """
    #dico des jours
    jour = {0:'dimanche', 1 : 'lundi', 2 :'mardi', 3: 'mercredi', 4: 'jeudi', 5:'vendredi', 6:'samedi'}
    calcule = (14-date['mois'])//12
    annee = date['annee'] - calcule
    mois = date['mois'] +12*calcule-2
    jous_de_semaine =(date['jour']+annee+annee//4-annee//100+annee//400 + (31*mois)//12)%7
    return jour[jous_de_semaine]



# =============================================================================
def calcule_veille_lendemain(date: dict) -> Tuple[dict,dict]:
    """donne le lendemain et la veille de la date

    Args:
        date (dict): une date

    Returns:
        Tuple[dict,dict]: renvoie un tuple qui a deux dico qui contient la veille et le lendemain de la date


    >>> date = cree_date(1,1,2021)
    >>> calcule_veille_lendemain(date)
    ({'jour': 31, 'mois': 12, 'annee': 2020}, {'jour': 2, 'mois': 1, 'annee': 2021})
    >>> date = cree_date(31,1,2021)
    >>> calcule_veille_lendemain(date)
    ({'jour': 30, 'mois': 1, 'annee': 2021}, {'jour': 1, 'mois': 2, 'annee': 2021})
    >>> date = cree_date(1,12,2020)
    >>> calcule_veille_lendemain(date)
    ({'jour': 30, 'mois': 11, 'annee': 2020}, {'jour': 2, 'mois': 12, 'annee': 2020})
    >>> date = cree_date(31,12,2020)
    >>> calcule_veille_lendemain(date)
    ({'jour': 30, 'mois': 12, 'annee': 2020}, {'jour': 1, 'mois': 1, 'annee': 2021})
    """
    #copie des dates pour modifier en suite
    date_lendemain = copie_date(date)
    date_veille = copie_date(date)

    #verif la date de base
    if valide_complet(date):

        #pour les mois de 31 jours
        if date['mois'] == 3 or date['mois'] == 5 or date['mois'] == 7 or date['mois'] == 8 or date['mois'] == 10:
            #si le jours n'est pas égale à 31
            if date['jour'] != 31:
                #rajoute un jour pour le lendemain
                date_lendemain = cree_date(date_lendemain['jour'] + 1, date['mois'], date['annee'])
            else:
                #si le jour est égale à 31 alors le jour = 1 puis le mois suivant
                date_lendemain = cree_date(date_lendemain['jour'] -30, date['mois']+1, date['annee'])


            #si le jours n'est pas égale à 1
            if date['jour'] != 1:
                date_veille = cree_date(date['jour'] - 1, date['mois'], date['annee'])
            else:
                #si le jour est égale à 1 alors le jour = 31 puis le mois d'aprés
                date_veille = cree_date(date['jour'] + 29, date['mois']-1, date['annee'])


        #pour les mois de 30 jours
        if date['mois'] == 4 or date['mois'] == 6 or date['mois'] == 9 or date['mois'] == 11:
            #si le jours n'est pas égale à 30
            if date['jour'] != 30:
                #rajoute un jour pour le lendemain
                date_lendemain = cree_date(date['jour'] + 1, date['mois'], date['annee'])
            else:
                #si le jour est égale à 30 alors le jour = 1 puis le mois suivant
                date_lendemain = cree_date(date['jour'] -29, date['mois']+1, date['annee'])


            #si le jours n'est pas égale à 1
            if date['jour'] != 1:
                date_veille = cree_date(date['jour'] - 1, date['mois'], date['annee'])
            else:
                #si le jour est égale à 1 alors le jour = 30 puis le mois d'avant
                date_veille = cree_date(date['jour'] + 28, date['mois']-1, date['annee'])
                
        #si le mois est janvier
        if date['mois'] == 1:
            #si le jour n'est pas égal 31          
            if date['jour'] != 31:
                #on passe on jour suivant
                date_lendemain = cree_date(date['jour'] + 1, date['mois'], date['annee'])
            else:
                #si le jour égalt à 2 le jour = 1 et le au mois suivant
                date_lendemain = cree_date(date['jour'] - 30, date['mois']+1, date['annee'])


            if date['jour'] != 1:
                date_veille= cree_date(date['jour'] - 1, date['mois'], date['annee'])
            else:
                date_veille = cree_date(date['jour'] + 30, date['mois']+11, date['annee']-1)

        #le mois de décembre
        if date['mois'] == 12:
            if date['jour'] != 31:
                date_lendemain = cree_date(date['jour'] + 1, date['mois'], date['annee'])
            else:
                date_lendemain = cree_date(date['jour'] - 30, date['mois']-11, date['annee']+1)


            if date['jour'] != 1:
                date_veille= cree_date(date['jour'] -1, date['mois'], date['annee'])
            else:
                date_veille = cree_date(date['jour'] + 29, date['mois']-1, date['annee'])
        #si l'année bissextile 
        if est_bissextile(date['annee']):
            if date['mois']==2:
                if date['jour'] != 29:
                    date_lendemain = cree_date(date['jour'] +1, date['mois'], date['annee'])
                else:
                    date_lendemain = cree_date(date['jour'] -28, date['mois']+1, date['annee'])
                if date['jour'] != 1:
                    date_veille = cree_date(date['jour'] -1, date['mois'], date['annee'])
                else:
                    date_veille = cree_date(date['jour'] + 30, date['mois']-1, date['annee'])
        else:
            if date['mois']==2:
                if date['jour'] != 28:
                    date_lendemain = cree_date(date['jour'] +1, date['mois'], date['annee'])
                else:
                    date_lendemain = cree_date(date['jour'] -27, date['mois']+1, date['annee'])
                if date['jour'] != 1:
                    date_veille = cree_date(date['jour'] -1, date['mois'], date['annee'])
                else:
                    date_veille = cree_date(date['jour'] + 30, date['mois']-1, date['annee'])

    #on met les deux dico dans un tuples
    veille_lendemain = date_veille, date_lendemain
    return veille_lendemain
        

        

# =============================================================================
def ajoute_fetes(calendrier:list, annee:int) -> NoReturn:
    """àjoute des evenement au calendrier 

    Args:
        calendrier (list): liste des évenement
        annee (int): une annee

    Returns:
        Noreturn
    """
    #ajout d'evenement dans le calendrier
    calendrier.append("25/12/{} : Noel".format(annee))
    calendrier.append("1/1/{} : Nouvel an".format(annee))
    calendrier.append("14/7/{} : Fete Nationnal".format(annee))
    calendrier.append("2/6/{} : Mon anniv".format(annee))
    calendrier.append("1/4/{} : Poisson d'avril".format(annee))

# =============================================================================

def afficheur_mensuel(calendrier : list, mois : int, annee:int):
    """affiche le calendrier en fonction du mois et de l'annee

    Args:
        calendrier (list): liste d'evenement
        mois (int): 
        annee (int): une année
    """
    #en tete de la liste du calendrier
    print('**{} {} **'.format(mois_dict[mois],annee))
    #boucle de 31 jours
    for i in range(1,32):
        #crée des date
        date = cree_date(i,mois,annee)
        #transfrome le n° des jour en des jours de semaine
        date = calcule_jour(date)
        #permet d'avoir un 0 si il y a que des unité dans le nombre
        if i < 9:
            chiffre = '0{}'.format(i)
        else:
            chiffre = i
        #affiche le  calendrier mensuelle
        print('{} {} :'.format(date,chiffre))


# =============================================================================


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


