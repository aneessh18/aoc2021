import sys
import collections


def main():
    filename = sys.argv[1]
    steps = int(sys.argv[2])
    with open(filename) as filename:
        lines = filename.readlines()
        polymer_template = lines[0].rstrip()
        polymer_pairs = ["".join(pair) for pair in zip(polymer_template[:-1], polymer_template[1:])]
        polymer = collections.Counter(polymer_pairs)
        transitions_map = [lines[i].rstrip().split(" -> ") for i in range(2, len(lines))]
        transitions_map = {k: [k[0] + v, v + k[1]] for k, v in transitions_map}
        for i in range(steps):
            update_polymer = collections.defaultdict(int)
            for pol, count in polymer.items():
                for transition in transitions_map[pol]:
                    update_polymer[transition] += count

            polymer = update_polymer.copy()

        counter = collections.defaultdict(int)

        for poly, count in polymer.items():
            for ch in poly:
                counter[ch] += count
        counter = [(c + 1) // 2 for k, c in counter.items()]
        # for i in range(steps):
        #     # polymer_template_snapshot = list(polymer_template)
        #     stack = []
        #     print(i)
        #     for j in range(len(polymer_template)):
        #         ln = len(stack)
        #         if ln == 0 or transitions_map.get(stack[ln - 1] + polymer_template[j]) is None:
        #             stack.append(polymer_template[j])
        #         else:
        #             transition = transitions_map[stack[ln - 1] + polymer_template[j]]
        #             stack.append(transition)
        #             stack.append(polymer_template[j])
        #     # print(stack)
        #     polymer_template = "".join(stack)

        mn = min(counter)
        mx = max(counter)

        print(mx - mn)


if __name__ == "__main__":
    main()
