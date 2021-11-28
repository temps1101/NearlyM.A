from csv import reader
from random import choice, sample, shuffle, randint


class Timeline:
    '''CSVのデータを扱うためのクラス'''
    def __init__(self, csv_filename: str) -> None:
        '''初期化関数。csv_filenameには現在の場所からの相対パスを入力してもらう形でOK

        Args:
            csv_filename (str): CSVデータのファイルパス
        '''
        with open(csv_filename) as f:
            self.raw_timetable = [row for row in reader(f)][1:]

        self.timestamps = list()
        for row in self.raw_timetable:
            if row[0] != 'N/A':
                self.timestamps.append(row)

    def get_timestamp(self) -> list:
        '''年代が記されている出来事の中からランダムに一つ選んで返す関数

        Returns:
            list: 選ばれた年代が記されている出来事のリスト。リストの中身は[年代、出来事、詳細（オプション）]になっている
        '''
        return choice(self.timestamps)

    def get_option_from_timestamp(self, tgt_timestamp: list) -> list:
        '''四択問題を作る際の他の候補を作成するメソッド。複数の出来事が起こった年代が干渉しないようにする工夫をしている

        Args:
            tgt_timestamp (list): 四択問題の答えとなるリスト。self.timestampsに入っている内容ではないとエラーが起こる

        Returns:
            list: 四択問題の選択肢が含まれているリスト
        '''
        no_time_overlap_timestamps = list()
        for timestamp in self.timestamps:
            if (timestamp == tgt_timestamp) or (timestamp[0] != tgt_timestamp[0]):
                no_time_overlap_timestamps.append(timestamp)

        center_idx = no_time_overlap_timestamps.index(tgt_timestamp)
        last_idx = len(no_time_overlap_timestamps) - 1

        if center_idx - 3 <= 0:
            option_idc = list(range(7))
        if center_idx + 4 >= last_idx:
            option_idc = list(range(last_idx - 7, last_idx))
        else:
            option_idc = list(range(center_idx - 3, center_idx + 4))
        option_idc.remove(center_idx)

        option_idc = sample(option_idc, 3) + [center_idx]
        shuffle(option_idc)

        return [no_time_overlap_timestamps[idx] for idx in option_idc]

    def get_sort_tgt(self) -> list:
        '''並び替え問題の候補を順序どうりにくれるメソッド

        Returns:
            list: ソートされた近い時期でまとまった並び替えようリスト
            list: 上のものをランダムにシャッフルしたリスト
        '''
        last_idx = len(self.raw_timetable) - 1
        center_idx = randint(0, last_idx)

        if center_idx - 3 <= 0:
            option_idc = list(range(7))
        if center_idx + 4 >= last_idx:
            option_idc = list(range(last_idx - 7, last_idx))
        else:
            option_idc = list(range(center_idx - 3, center_idx + 4))
        option_idc.remove(center_idx)

        option_idc = sample(option_idc, 4)

        return [self.raw_timetable[idx] for idx in sorted(option_idc)], [self.raw_timetable[idx] for idx in option_idc]
