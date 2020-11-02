#zip function is used here
def list_to_dict():
    lst1=[1,2,3,4,5]
    lst2=['suresh','suraj','sandesh','shubham','rohit']
    result = dict(zip(lst1,lst2))
    print(result)
list_to_dict()