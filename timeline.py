import csv
from random import choice, sample, shuffle


class Timeline:
    def __init__(self, csv_filename):
        with open(csv_filename) as f:
            self.raw_timetable = [row for row in csv.reader(f)][1:]

        self.yeps = list()
        for row in self.raw_timetable:
            if row[0] != 'N/A':
                self.yeps.append(row)

    def get_year_event_pair(self):
        return choice(self.yeps)

    def get_suggestions_from_year_event_pair(self, yep):
        overlap_removed = list()
        for yep_i in self.yeps:
            if (yep_i == yep) or (yep_i[0] != yep[0]):
                overlap_removed.append(yep_i)

        center_idx = overlap_removed.index(yep)

        last_idx = len(overlap_removed) - 1
        if center_idx - 3 <= 0:
            suggestion_temp = list(range(7))
        if center_idx + 4 >= last_idx:
            suggestion_temp = list(range(last_idx - 7, last_idx))
        else:
            suggestion_temp = list(range(center_idx - 3, center_idx + 4))
        suggestion_temp.remove(center_idx)

        suggestion_idx = sample(suggestion_temp, 3) + [center_idx]
        shuffle(suggestion_idx)

        return [overlap_removed[i] for i in suggestion_idx]
