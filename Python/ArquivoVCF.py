import vcf

file = open("C:/Users/JrStudio/Downloads/GNT6093_S1.vcf", "r")
reader = vcf.Reader(file)
for record in reader:
    ugt1a1 = False
    pos = str(record.POS)
    ref = str(record.REF)
    print(pos)
    #print(ref)