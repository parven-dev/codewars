def apparently(st: str) -> str:
    
    data = []
    # for item in st.split(" "):
    #     if ("and" == item or "but" == item ): 
    #         datt = st.replace(item, f"{item} apparently")  
    #         data.append(datt)
    
    if "and" or "but" in st.split(" "):
        gry = st.replace("and","and apartment")
        print(gry)
      
    
    return data
    


#'It was great and apparently I have never been on live television before but apparently sometimes I dont watch this"

st = "It was great and I have never been on live television and before but sometimes I dont watch this." 
print(apparently(st))
