class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue = [(startGene, 0)]
        visited = set([startGene])
        n = len(startGene)
        genes_set = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
        while queue:
            print(queue)
            current_gene, mutations = queue.pop(0)
            print(current_gene, mutations)
            if current_gene == endGene:
                return mutations
            
            for i in range(n):
                for j in genes_set[current_gene[i]]:
                    new_gene = current_gene[:i] + j + current_gene[i+1::]
                    print(new_gene)
                    if new_gene in bank_set and (new_gene not in visited):
                        print(new_gene)
                        visited.add(new_gene)
                        queue.append((new_gene, mutations + 1))
        return -1



if __name__ == "__main__":
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    a = Solution()
    ans = a.minMutation(start, end, bank)
    print(ans)