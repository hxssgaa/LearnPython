from subprocess import call

from uuid import uuid4

import time

from oj import exception
from oj.common.utils import call_command
from oj.exam.backends.model import OJ


class Manager(object):
    def __init__(self):
        self.exam_map = self._map_exams()
        self.user_score_map = self._map_users_score()

    def _map_exams(self):
        exams = {}
        with open('data/oj.data') as f:
            cnt = int(f.readline())
            for _ in xrange(cnt):
                exam = OJ()
                exam.id = int(f.readline().strip('\n'))
                exam.title = f.readline().strip('\n')
                exam.description = f.readline().strip('\n')
                exam.test_sets = []
                while True:
                    line = f.readline().strip('\n')
                    if line == '</html>':
                        exam.description += '</html>'
                        break
                    exam.description += (line + '<br/>')
                f.readline()
                while True:
                    input_line = f.readline().strip('\n')
                    if input_line == '</test>':
                        break
                    output_line = f.readline().strip('\n')
                    exam.test_sets.append((input_line, output_line))
                exams[exam.id] = exam
        return exams

    def _map_users_score(self):
        users_score = {}
        with open('data/users_score.data') as f:
            cnt = int(f.readline())
            for _ in xrange(cnt):
                line = f.readline().strip('\n')
                user_score_data = line.split()
                users_score[(user_score_data[0], user_score_data[1])] = user_score_data[2]
        return users_score

    def _build_exam_test(self, bin_name, exam):
        score_diff = 10
        right_cnt = 0
        wrong_test_set = []
        runtime = 0
        for test_set in exam.test_sets:
            with open('tmp/%s.txt' % bin_name, 'w') as f:
                for input_data in test_set[0].split():
                    f.write('%s\n' % input_data)
            begin_t = time.time()
            code, output = call_command(['tmp/%s' % bin_name], stdin=open('tmp/%s.txt' % bin_name))
            end_t = time.time()
            runtime = max(end_t - begin_t, runtime)
            if output.strip('\n') == test_set[1]:
                right_cnt += 1
            else:
                wrong_test_set.append('%s --> %s : %s' % (test_set[0], output, test_set[1]))
            if code != 0:
                raise exception.CommitOJFailed("code running timeout")
        code = call(['rm', 'tmp/%s.txt' % bin_name])
        if code != 0:
            raise exception.CommitOJFailed("remove temp file failed")
        return 100 if right_cnt == len(exam.test_sets) else score_diff * right_cnt, wrong_test_set, runtime

    def commit_exam(self, exam_data, oj_id, user_id):
        if not exam_data or not oj_id or not user_id:
            raise exception.ParameterNotValid("input parameter is wrong")
        exam = self.get_exam_detail(oj_id)
        if not exam:
            raise exception.ParameterNotValid("exam does not exists")
        temp_file_name = str(uuid4())
        temp_file_path = 'tmp/%s.c' % temp_file_name
        with open(temp_file_path, 'w') as f:
            f.write(exam_data)
        code = call(['gcc', temp_file_path, '-o', 'tmp/%s' % temp_file_name])
        if code != 0:
            raise exception.CommitOJFailed("code compile failed")
        score, wrong_test_set, runtime = self._build_exam_test(temp_file_name, exam)
        for remove_file in ['%s.c' % temp_file_name, temp_file_name]:
            code = call(['rm', 'tmp/%s' % remove_file])
            if code != 0:
                raise exception.CommitOJFailed("remove temp file failed")
        exam.score = score
        exam.status = 'OK'
        exam.runtime = runtime
        exam.wrong_info = '<br/>'.join(wrong_test_set)
        return exam

    def get_exam_detail(self, oj_id=-1):
        exam = self.exam_map.get(oj_id, None)
        exam_ids = sorted(self.exam_map.keys())
        if not exam and self.exam_map:
            oj_id = exam_ids[0]
            exam = self.exam_map[oj_id]
        return exam

    def get_exam(self, oj_id, user_id):
        exam = self.get_exam_detail(oj_id)
        oj_id = exam.id
        exam_ids = sorted(self.exam_map.keys())
        exam.score = self.user_score_map[(user_id, oj_id)] if (user_id, oj_id) in self.user_score_map else 0
        exam.prev_id = None if oj_id == exam_ids[0] else self.exam_map[exam_ids[exam_ids.index(oj_id) - 1]].id
        exam.next_id = None if oj_id == exam_ids[-1] else self.exam_map[exam_ids[exam_ids.index(oj_id) + 1]].id
        return exam
