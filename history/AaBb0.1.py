import random

# 定义基因杂交函数
def cross_genes():
    # 父母的基因型
    parent_genotype = ['A', 'a', 'B', 'b']
    
    # 从每个父母那里随机选择一个A基因和一个B基因
    child = random.choice(parent_genotype[:2]) + random.choice(parent_genotype[:2]) + \
            random.choice(parent_genotype[2:]) + random.choice(parent_genotype[2:])
    return child

# 定义基因型格式化函数
def format_genotype(genotype):
    # 将基因型按字母排序并合并
    return ''.join(sorted(genotype[:2], reverse=True)) + ''.join(sorted(genotype[2:], reverse=True))

# 进行10000次基因杂交
cross_results = [cross_genes() for _ in range(10000)]

# 统计各基因型次数
genotype_counts = {}
for genotype in cross_results:
    # 格式化基因型
    formatted_genotype = format_genotype(genotype)
    if formatted_genotype not in genotype_counts:
        genotype_counts[formatted_genotype] = 0
    genotype_counts[formatted_genotype] += 1

# 打印结果
for genotype, count in sorted(genotype_counts.items()):
    print(f"{genotype}: {count}")
