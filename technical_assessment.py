def max_skill(N, M, Ai, Bi):
    if N < 1:
        return 'N harus lebih besar atau sama dengan 1!'
    if M > 100:
        return 'M harus kurang dari atau sama dengan 100!'
    if len(Ai) != N or len(Bi) != N:
        return 'Jumlah baris 1 dan 2 tidak sesuai!'
    if not all(1 <= ai <= 1000 for ai in Ai):
        return 'Semua element didalam List Ai harus diantara 1 dan 1000!'
    if not all(1 <= bi <= 1000 for bi in Bi):
        return 'Semua element didalam List Bi harus diantara 1 dan 1000!'
    
    list_lawan = list(zip(Ai, Bi))
    list_lawan.sort()
    
    juned_skill = M
    
    for ai, bi in list_lawan:
        if juned_skill >= ai:
            juned_skill += bi
        else:
            break
    
    return juned_skill
        

# Contoh Input!
N = 4
M = 2
Ai = [8, 9, 3, 2]
Bi = [5, 4, 1, 3]

# Ouput:
print(max_skill(N, M, Ai, Bi))