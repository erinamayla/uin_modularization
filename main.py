nama = 'Erina Maylani'
program = 'Gerak lurus'

print(f'Program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60 }menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

def hitung_berat(massa, gravitasi):
    berat = massa / gravitasi
    print(f'massa = {massa / 30}kg dengan gravitasi = {gravitasi / 9,8}m/s')
    print(f'sehingga berat = {berat} newton')
    return berat

# massa = 30
# gravitasi = 9,8
berat = hitung_berat(30, 5 * 10)
berat = hitung_berat(60, 120 * 30)
