import sys
import collections
filename = sys.argv[1]
days = sys.argv[2]

with open(filename) as file:
    lines = file.readlines()
    species_timeline = collections.Counter(list(map(int, lines[0].rstrip().split(","))))
    for day in range(int(days)):
        species_timeline_snapshot = species_timeline.copy()
        for timeline, species_count in species_timeline.items():
            if timeline == 0:
                species_timeline_snapshot[6] += species_count #current species move 6 day window
                species_timeline_snapshot[8] += species_count #new ones are added to the 8 day window
            else:
                species_timeline_snapshot[timeline-1] += species_count

            species_timeline_snapshot[timeline] -= species_count # clean all of them

        species_timeline = species_timeline_snapshot

    print(sum(species_timeline.values()))