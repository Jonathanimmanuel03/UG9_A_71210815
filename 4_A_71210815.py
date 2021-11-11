print('===== MASUKAN JUMLAH MAKANAN')
pesanan_1 = int(input('IKAN BAKAR       Rp25.000 : '))
pesanan_2 = int(input('ES DOGER         Rp6.000  : '))
pesanan_3 = int(input('RUJAK CINGUR     Rp8.000  : '))
print('===== TOTAL =====')
jmlhorder1 = pesanan_1*25000
jmlhorder2 = pesanan_2*6000
jmlhorder3 = pesanan_3*8000
print('Total IKAN BAKAR     : Rp',jmlhorder1)
print('Total ES DOGER       : Rp',jmlhorder2)
print('Total RUJAK CINGUR   : Rp',jmlhorder3)
print('Jumlah Total Biaya yang Harus Dibayar adalah Rp',jmlhorder1+jmlhorder2+jmlhorder3)
