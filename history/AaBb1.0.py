import random

def simulate_genetics(parent1, parent2, num_offspring):
    # 假设基因型由四个字符表示，例如'AaBb'或'aabb'
    alleles_A = ['A', 'a']
    alleles_B = ['B', 'b']
    offspring = []

    for _ in range(num_offspring):
        # 随机选择每个亲代的一个等位基因
        allele1_A = random.choice(parent1[0:2])
        allele2_A = random.choice(parent2[0:2])
        allele1_B = random.choice(parent1[2:4])
        allele2_B = random.choice(parent2[2:4])
        # 合并等位基因形成后代基因型
        offspring_genotype = ''.join(sorted(allele1_A + allele2_A)) + ''.join(sorted(allele1_B + allele2_B))
        offspring.append(offspring_genotype)

    # 计算每种基因型的频率
    genotype_frequency = {genotype: offspring.count(genotype) / num_offspring for genotype in set(offspring)}
    return genotype_frequency

# 输入亲代基因型和模拟次数
parent_genotype1 = input('请输入第一个亲代的基因型（例如：AaBb）: ')
parent_genotype2 = input('请输入第二个亲代的基因型（例如：AaBb）: ')
num_simulations = int(input('请输入模拟次数: '))

# 运行模拟并输出结果
result = simulate_genetics(parent_genotype1, parent_genotype2, num_simulations)
print('模拟结果：')
for genotype, frequency in result.items():
    # 将aA和Aa合并为Aa
    genotype = genotype.replace('aA', 'Aa').replace('bB', 'Bb')
    print(f'基因型 {genotype}: 频率 {frequency:.2f}')