
def campaign(name,status,adgroup,*keywords,**keywordsMatchTypes):
    """Print out a campaign, status of campaign, ad groups.
    campaign:       Name of the campaign
    status:         Campaign status
    ad groups:      Name of ad groups
    *keywords:      List of keywords in that ad group (sequence, positional arguments)
    **keywords:     List of keywords and match types in that ad group (keyword arguments)
    """
    print("=" * 40)
    print("Campaign Name: ", name)
    print("Status: ", status)
    print("ad group: ", adgroup)
    print('the keywords are: ')
    for keyword in keywords:
        print(keyword)
    '''
    for keyword, matchtype in keywords.items(): 
        print(keyword, ": ",matchtype)
    '''
   # print("{0:-^40}".format(" registered students "))    
    

if __name__ == "__main__":
    campaign("Link Building",
             "Active",
             "Link Building Exact",
             ("Python Software Foundation","exact"),
             "Python software",
             "python software company"
             "Python Software Foundation",
             "Python software",
             "python software company"
             )