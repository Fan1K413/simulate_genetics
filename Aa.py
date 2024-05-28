import random

def simulate_genetics(parent1, parent2, num_offspring):
    # 假设基因型由两个字符表示，例如'Aa'或'aa'
    alleles = ['A', 'a']
    offspring = []

    for _ in range(num_offspring):
        # 随机选择每个亲代的一个等位基因
        allele1 = random.choice(parent1)
        allele2 = random.choice(parent2)
        # 合并等位基因形成后代基因型，并确保基因型是排序过的
        offspring_genotype = ''.join(sorted(allele1 + allele2))
        offspring.append(offspring_genotype)

    #计算每种基因型的频率


    genotype_frequency = {genotype: offspring.count(genotype) / num_offspring for genotype in set(offspring)}
    return genotype_frequency

# 输入亲代基因型和模拟次数
parent_genotype1 = input('请输入第一个亲代的基因型（例如：Aa）: ')
parent_genotype2 = input('请输入第二个亲代的基因型（例如：Aa）: ')
num_simulations = int(input('请输入模拟次数: '))

# 运行模拟并输出结果
result = simulate_genetics(parent_genotype1, parent_genotype2, num_simulations)
print('模拟结果：')
for genotype, frequency in result.items():
    print(f'基因型 {genotype}: 频率 {frequency:.2f}')

# 提供选项进行再次模拟或退出
while True:
    user_choice = input('输入 "1" 保留所有数据再次模拟遗传，输入"2"仅保留基因型再次模拟遗传，输入"3"清除所有数据再次模拟遗传，输入 "0" 退出程序: ')
    if user_choice == '1':
        result = simulate_genetics(parent_genotype1, parent_genotype2, num_simulations)
        print('新的模拟结果：')
        for phenotype, frequency in result.items():
            print(f'表型 {phenotype}: 频率 {frequency:.4f}')

    elif user_choice == '2':
        num_simulations = int(input('请输入模拟次数: '))
        result = simulate_genetics(parent_genotype1, parent_genotype2, num_simulations)
        print('新的模拟结果：')
        for phenotype, frequency in result.items():
            print(f'表型 {phenotype}: 频率 {frequency:.4f}')

    elif user_choice == '3':
        parent_genotype1 = input('请输入第一个亲代的基因型（例如：Aa）: ')
        parent_genotype2 = input('请输入第二个亲代的基因型（例如：Aa）: ')
        num_simulations = int(input('请输入模拟次数: '))
        result = simulate_genetics(parent_genotype1, parent_genotype2, num_simulations)
        print('新的模拟结果：')
        for phenotype, frequency in result.items():
            print(f'表型 {phenotype}: 频率 {frequency:.4f}')
            
    elif user_choice == '0':
        print('程序已退出')
        break
    else:
        print('无效输入，请输入有效数字.')



