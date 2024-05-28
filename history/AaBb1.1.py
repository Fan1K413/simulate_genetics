import random

def simulate_genetics(parent1, parent2, num_offspring):
    alleles_A = ['A', 'a']
    alleles_B = ['B', 'b']
    offspring = []

    for _ in range(num_offspring):
        allele1_A = random.choice(parent1[0:2])
        allele2_A = random.choice(parent2[0:2])
        allele1_B = random.choice(parent1[2:4])
        allele2_B = random.choice(parent2[2:4])
        offspring_genotype = ''.join(sorted(allele1_A + allele2_A)) + ''.join(sorted(allele1_B + allele2_B))
        offspring.append(offspring_genotype)

    # 合并基因型为表型
    phenotype_frequency = {'A_B_': 0, 'aaB_': 0, 'A_bb': 0, 'aabb': 0}
    for genotype in offspring:
        if 'A' in genotype[0:2] and 'B' in genotype[2:]:
            phenotype_frequency['A_B_'] += 1
        elif 'A' not in genotype[0:2] and 'B' in genotype[2:]:
            phenotype_frequency['aaB_'] += 1
        elif 'A' in genotype[0:2] and 'B' not in genotype[2:]:
            phenotype_frequency['A_bb'] += 1
        elif genotype == 'aabb':
            phenotype_frequency['aabb'] += 1

    # 计算表型频率
    for phenotype in phenotype_frequency:
        phenotype_frequency[phenotype] /= num_offspring

    return phenotype_frequency

# 输入亲代基因型和模拟次数
parent_genotype1 = input('请输入第一个亲代的基因型（例如：AaBb）: ')
parent_genotype2 = input('请输入第二个亲代的基因型（例如：AaBb）: ')
num_simulations = int(input('请输入模拟次数: '))

# 运行模拟并输出结果
result = simulate_genetics(parent_genotype1, parent_genotype2, num_simulations)
print('模拟结果：')
for phenotype, frequency in result.items():
    print(f'表型 {phenotype}: 频率 {frequency:.2f}')