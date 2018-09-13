print ("""
------------------tools generated kouta voucher-------------------

++++++++++++++creat by Mr.ID++++++++++++++++++

Warning :

Tidak semua angka work kita mengacak kode vocher dan tidak semua dapat di gunakan selamat mencoba yah *_*

Contoh :
Masukan no HP

Input: 11
Output: true 
 
Input: 24
Output: false

Program ini hanya bila anda kepepet dan dalam ke adaan darurat 

Resiko :

             No HP di bloked oleh operator 

---------------Important-----------------------
Kode voucher 

Contoh : ^2=kode unik 
-----------------------------------------------
Masukan No HP
""")


from decimal import *

prec=Decimal('.001')

#The challenge requires a precision up to 3 digits after the comma. If you want to be more precise just change prec. example: Decimal('.0001')

ra=list(map(lambda l:int(l),input().split(" ")))

if len(ra)!=1:
    res=list(filter(lambda j: set(list(str(j**2))) & set(list(str(Decimal(j**.5).quantize(prec))))!=set(), list(range(ra[0],ra[1]+1))))
    
    if len(res)!=0:
        print("The numbres with a strange root between",ra[0],"and",ra[1],"are: {}.".format(res))
        
        print("Each common digit is/are:")
        
        for elem in res:
            print(elem,"=>",set(list(str(elem**2))) & set(list(str(Decimal(elem**.5).quantize(prec)))))
    else:
        print(f"There are no numbers with strange roots between {ra[0]} and {ra[1]} .")
else:
    #print("You entered",ra[0],"and it has{}a strange root.".format(" " if set(list(str(ra[0]**2))) & set(list(str(Decimal(ra[0]**0.5).quantize(prec))))!=set() else " not "))
    print("{0}^2={1}".format(ra[0],ra[0]**2))
    
    print("{0}^0.5={1}".format(ra[0],Decimal(ra[0]**.5).quantize(prec)))
    
    if set(list(str(ra[0]**2))) & set(list(str(Decimal(ra[0]**.5).quantize(prec))))!=set():
        print("Therefore, {0} has a strange root.\nThe root and the square have in common: {1}.".format(ra[0],set(list(str(ra[0]**2))) & set(list(str(Decimal(ra[0]**.5).quantize(prec))))))
    else:
        print(ra[0],"has not a strange root.")