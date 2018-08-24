def norm(phone):
    
    if (phone=="-"):
        return "-"
    elif (phone=="0"):
        return "0"
    elif (phone=="(null)"):
        return "(null)"
    else:
        isi = phone.split("+")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split("*")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split("?")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split("-")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split("/")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split("(")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split(")")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split(".")
        nomor = ""
        for c in isi:
            nomor += c
        isi = nomor.split(" ")
        nomor = ""
        for c in isi:
            nomor += c
        if (nomor[0]=="0"):
            return "62"+nomor[1:]
        return nomor
        
        

if __name__ == '__main__':
    
    st1 = input("Insert phone number: ")
    print("Normalized:",norm(st1))
