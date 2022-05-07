'''
================================================================================
Python program to enumerate the distinct logics possible under a given composition structure
Written by: Yasharth Yadav

This program also uses codes taken from the following GitHub repository:
https://github.com/asamallab/MCBF

REFERENCES:

[1] "Boolean composition restricts biological logics".
Thomas A. Fink, Ryan Hannam, arXiv 2109.12551;
doi: https://doi.org/10.48550/arXiv.2109.12551

[2] "Minimum complexity drives regulatory logic in Boolean models of living systems".
Ajay Subbaroyan, Olivier C. Martin, Areejit Samal, bioRxiv 2021.09.20.461164;
doi: https://doi.org/10.1101/2021.09.20.461164
================================================================================
'''

class generate:
    '''
    Use this class to generate lists of different types of BFs.
    '''

    def all_BF(k):
        '''
        returns all the 2^(2^k) BFs. Works upto k=4

        #instance
        >>> all_BF(1)
        >>> ['00', '01', '10', '11']
        '''
        L = []
        func = 2**(2**k)
        for integer in range(func):
            b = bin(integer)[2:].zfill(2**k)
            L+=[b]
        return L

    def half_BF(k):
        '''
        returns only the first half the 2^(2^k) BFs (i.e. the complement of a BF is not considered)
        Works upto k=4

        #instance
        >>> half_BF(2)
        >>> ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111']
        '''
        L = []
        func = 2**(2**k)
        for integer in range(int(func/2)):
            b = bin(integer)[2:].zfill(2**k)
            L+=[b]
        return L

    def rep_composed_BF(comp_struc):
        '''
        returns the distinct functions possible under a given representative composition structure
        input composition structure as a list
        e.g. comp_struc = [2,3] corresponds to f(g1(a,b),g2(c,d,e))
        '''
        from itertools import product
        #Input composition struture as list e.g. [2,2]
        k = sum(comp_struc)
        n = len(comp_struc)
        #Define all g_i's
        g = {}
        for i in range(0,n):
            g[i] = generate.half_BF(comp_struc[i])
        #Define f
        f = generate.all_BF(n)
        #Generate BFs corresponding to all possible combinations of f and g_i's
        possible_logics = []
        for element in product(*g.values()):
            for function in f:
                temp = [function[int(''.join(each),2)] for each in product(*element)]
                possible_logics+=[''.join(temp)]
        distinct_logics = list(set(possible_logics))
        return distinct_logics

    def all_composed_BF(comp_struc):
        '''
        returns all the functions possible under a given composition structure, after accounting for
        all the permutations of inputs.
        Input composition structure as a list.
        e.g. comp_struc = [2,3] corresponds to f(g1(a,b),g2(c,d,e)) and all the permutations of a, b, c, d, e
        '''
        import string
        comp_struc = sorted(comp_struc)
        k = sum(comp_struc)
        original_inputs = list(string.ascii_lowercase)[:k]

        input_perms = properties.noneq_input_perms(comp_struc)
        input_perms = [[item for sublist in each for item in sublist] for each in input_perms]
        input_perms.remove(original_inputs)

        rep_BF = generate.rep_composed_BF(comp_struc)
        distinct_logics = [func for func in rep_BF]

        for each_perm in input_perms:
            for func in rep_BF:
                orig_dnf = properties.get_dnf(k, func)
                perm_dnf = properties.permuted_dnf(k, orig_dnf, each_perm)
                distinct_logics += [properties.dnf_to_string(k, perm_dnf)]

        return list(set(distinct_logics))

    def read_all_composed_BF(comp_struc):
        '''
        reads from 'composed_BF_catalog' and returns all the functions possible under a given composition structure,
        after accounting for all the permutations of inputs.
        Only the composition structures upto k = 5 inputs (except {1,1,1,1,1} and {5}) are available in the catalog.
        Input composition structure as a list.
        e.g. comp_struc = [2,3] corresponds to f(g1(a,b),g2(c,d,e)) and all the permutations of a, b, c, d, e
        '''
        import json
        k = sum(comp_struc)
        outfile_name = 'composed_BF_catalog/' + '-'.join(str(item) for item in comp_struc) + '.json'
        with open(outfile_name,'r') as outfile:
            distinct_logics = [bin(func)[2:].zfill(2**k) for func in json.load(outfile)]
        return distinct_logics

class properties:
    def noneq_input_perms(comp_struc):
        '''
        returns the possible permutations of inputs for a given composition structure.
        among the permutations resulting in the same set of BFs, only one such permutation is considered.
        '''
        import string
        from itertools import permutations

        num_inputs = sum(comp_struc)
        num_TF = len(comp_struc)
        inputs_list = list(string.ascii_lowercase)[:num_inputs]

        some_list = [0]
        some_num = 0
        for item in comp_struc:
            some_num = some_num + item
            some_list+=[some_num]

        all_perms = []
        for permutation in permutations(inputs_list):
            y = [frozenset(permutation[some_list[i]:some_list[i+1]]) for i in range(num_TF)]
            all_perms.append(frozenset(y))

        all_perms = list(set(all_perms))
        all_perms_new = []
        for each in all_perms:
            y = [sorted(list(item)) for item in each]
            y.sort()
            y.sort(key=len)
            all_perms_new.append(y)

        all_perms_new.sort()
        return all_perms_new

    def get_dnf(k,f):
        '''
        returns the full DNF and Quine-McCluskey minimized DNF of the BF

        #instance
        >>> bf(3,'10001010' ).get_dnf()
        >>> {'full_DNF': '(~a & ~b & ~c) | (a & ~b & ~c) | (a & b & ~c)',
             'QM-DNF': (a & ~c) | (~b & ~c)}
        '''
        import string
        chars = string.ascii_lowercase[:k]
        indices = [bin(i)[2:].zfill(k) for i, bit in enumerate(f) if bit == '1']
        dnf = ''
        for ele in indices:
            s = ''
            for i in range(k):
                if ele[i] == '1':
                    s += chars[i]+' & '
                else:
                    s += '~'+ chars[i] +' & '
            s = s[:-3]
            dnf += '(' + s + ')' + ' | '
        dnf = dnf[:-3]
        #simp_dnf = simplify_logic(parse_expr(dnf), 'dnf')
        return dnf #{'full_DNF':dnf, 'QM-DNF':simp_dnf}

    def permuted_dnf(k, dnf, permuted_inputs):
        '''
        given a dnf, returns the modified dnf defined by permuting the inputs
        k = number of inputs
        dnf = dnf corresponding to unpermuted indices
        permuted_indices = one instance of permuted indices
        '''
        import string
        original_inputs = list(string.ascii_lowercase)[:k]
        permuted_inputs_caps = [item.upper() for item in permuted_inputs]
        new_dnf = dnf
        for init_input, new_input in zip(original_inputs, permuted_inputs_caps):
            new_dnf = new_dnf.replace(init_input, new_input)
        for uppercase_input, lowercase_input in zip(permuted_inputs_caps, permuted_inputs):
            new_dnf = new_dnf.replace(uppercase_input, lowercase_input)
        return new_dnf

    def dnf_to_string(k,dnf):
        '''
        given the dnf for a BF, returns the binary string for the BF.
        '''
        if dnf == '':
            return ''.zfill(2**k)

        import string
        inputs_list = list(string.ascii_lowercase)[:k]
        BF_string = list(''.zfill(2**k))
        for each_term in dnf.split('|'):
            each_term = each_term.strip()
            truth_table_row = list(bin(2**k-1)[2:])
            input_index = 0
            for each_input in inputs_list:
                if '~'+each_input in each_term:
                    truth_table_row[input_index] = '0'
                input_index+=1
            truth_table_row = ''.join(truth_table_row)
            truth_table_row = int(truth_table_row,2)
            BF_string[truth_table_row] = '1'
        BF_string = ''.join(BF_string)
        return BF_string
