def get_trph(div_tag, cat):
    
    empty_list = []
    if(cat == "LOC"):
        index = 5
    elif cat == "NAC":
        index = 14
    elif cat == "INT":
        index = 23
    
    try:
        trph = div_tag.contents[index].text
        return trph.split(" - ")

    except:
        return empty_list