#baekjoon_2941
#크로아티아 알파벳

croAlpha={"c=":"č",  "c-":"ć", "dz=":"dž", "d-":"đ", "lj":"lj", "nj":"nj", "s=":"š", "z=":"ž"}
count = 0

arr = input()

for croSpell in croAlpha:
    if(arr.find(croSpell) >= 0):
        count += arr.count(croSpell)
        arr = arr.replace(croSpell,'##')

for excuteSpell in arr:
    if (excuteSpell.isalpha()):
        count += 1
print(count)


