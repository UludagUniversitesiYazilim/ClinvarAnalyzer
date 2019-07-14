
def get_assertion(element):
    if element[2].tag == "ReferenceClinVarAssertion":
        desc = element[2][2][1].text
        mid = get_MeasureSetType(element[2])
    else:
        for elem in element:
            if elem.tag == "ReferenceClinVarAssertion":
                desc = elem[2][1].text
                break
        mid = get_MeasureSetType(elem)
    return mid, desc

def get_MeasureSetType(element):
    vid = ''
    for elem in element:
        if elem.tag =="GenotypeSet":
            vid = elem[0].attrib["ID"]
            break
        if elem.tag == "MeasureSet":
            vid = elem.attrib["ID"]
            break
    return vid

def get_CVset(path, speed):
    import time
    import lxml.etree as et

    if not speed == 0:
        real_speed = 1/speed
    else:
        real_speed = 0

    error_count = 0
    set_count = 0
    
    context = et.iterparse(path, events=("end",), tag="ClinVarSet")

    for event, element in context:
        set_id = ''

        try:
            description = get_assertion(element)
        except IndexError:
            error_count += 1
            print(set_count, error_count)
            

        set_count += 1

        yield description
        
        element.clear()
        time.sleep(real_speed)

    print("Toplam:", set_count)
    return set_count, error_count


if __name__ == "__main__":
    import time
    
    sets = get_CVset("./mock/MockData-2.xml", 0)

    t1 = time.time()

    for i, j in sets:
        print(f"{i} -- {j}")
        
        
    t2 = time.time()

    print(t2 - t1)

    # print(f"Kayit Sayisi: {sets[0]}, Hata Sayisi: {sets[1]}")
    
    
    

