#!/usr/bin/envs python

def parse_monn_modified_alignment(align_file):
    align_result_dict = {}
    with open(align_file,'r') as alignment:
        for line in alignment:
            if line.startswith("target_name"):
                target_name = line.strip().split(" ")[1]
                # result_dict[target_name] = (seq_target, seq_query, align, target_start, query_start)
                align_result_dict[target_name] = ["", "", "", 0, 0]
            if line.startswith("optimal_alignment_score"):
                target_start = int(line.split()[7])
                query_start = int(line.split()[11])
                align_result_dict[target_name][3] = target_start
                align_result_dict[target_name][4] = query_start
            if line.startswith(" "):
                align_result_dict[target_name][2] += line.strip('\n').split('\t')[1]
            if line.startswith("Target"):
                align_result_dict[target_name][0] += line.split("\t")[1]
            if line.startswith("Query"):
                align_result_dict[target_name][1] += line.split("\t")[1]
        alignment.close()
    return align_result_dict

if __name__ == '__main__':
    result_dict = parse_monn_modified_alignment("smith-waterman-src/out6.3_pdb_align.txt")
    for k, v in result_dict.items():
        print(k)
        print(v)

            

