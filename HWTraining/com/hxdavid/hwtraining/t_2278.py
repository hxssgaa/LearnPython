# coding=utf-8
"""
医院门诊管理系统

考生需要模拟实现一个简单的医院门诊管理系统，实现系统初始化、挂号、就诊、缴费、查询的功能。
病人挂号、缴费时不需要考虑排队情况，就诊阶段需要考虑排队情况。

详情见:http://117.78.32.67/exam/ShowProblemInfo?method=campusProblemInfo&id=2278
"""


class Hospital(object):
    MAX_DOCTOR_TREAT = 4
    DOCTOR_DIAG_FEE = 10
    DOCTOR_TREAT_FEE = 50

    class Patient(object):
        STATUS_NORMAL, STATUS_TREAT, STATUS_PAY = range(1, 4)

        def __init__(self, id, kind, cash, insurance, status=None):
            self.id = id
            self.kind = kind
            self.cash = cash
            self.insurance = insurance
            self.status = status if status else self.STATUS_NORMAL

    def __init__(self):
        self.patients = [
            self.Patient('pat01', 0, 100, 0),
            self.Patient('pat02', 1, 100, 100),
            self.Patient('pat03', 0, 100, 0),
            self.Patient('pat04', 1, 100, 50),
            self.Patient('pat05', 1, 10, 10),
            self.Patient('pat06', 1, 20, 10),
        ]
        self.patient_map = {e.id: e for e in self.patients}
        self.wait_queue = []

    def op_init(self):
        self.__init__()
        return "E000"

    def op_register(self, p_id):
        patient = self.patient_map[p_id]
        if patient.status in (self.Patient.STATUS_TREAT, self.Patient.STATUS_PAY):
            return "E002"
        if len(self.wait_queue) >= self.MAX_DOCTOR_TREAT:
            return "E003"
        pay_succeed = False
        if patient.insurance >= self.DOCTOR_DIAG_FEE:
            patient.insurance -= self.DOCTOR_DIAG_FEE
            pay_succeed = True
        elif patient.cash >= self.DOCTOR_DIAG_FEE:
            patient.cash -= self.DOCTOR_DIAG_FEE
            pay_succeed = True
        if not pay_succeed:
            return "E004"
        patient.status = self.Patient.STATUS_TREAT
        self.wait_queue.append(patient)
        return "E001"

    def op_diag(self):
        if not self.wait_queue:
            return "E006"
        patient = self.wait_queue.pop(0)
        patient.status = self.Patient.STATUS_PAY
        return "E005"

    def op_pay(self, pid):
        patient = self.patient_map[pid]
        if patient.status != self.Patient.STATUS_PAY:
            return "E014"
        patient.status = self.Patient.STATUS_NORMAL
        pay_succeed = False
        if patient.insurance >= self.DOCTOR_TREAT_FEE:
            patient.insurance -= self.DOCTOR_TREAT_FEE
            pay_succeed = True
        elif patient.cash >= self.DOCTOR_TREAT_FEE:
            patient.cash -= self.DOCTOR_TREAT_FEE
            pay_succeed = True
        if not pay_succeed:
            return "E008"
        return "E007"

    def op_query(self, param):
        ps = param.split("-")
        if ps[0] == "0":  # By doctor
            return "E013:dct %s" % " ".join([e.id for e in self.wait_queue]) if self.wait_queue else "E013:dct 0"
        else:
            patient = self.patient_map[ps[1]]
            if patient.status == self.Patient.STATUS_NORMAL:
                return "E012:%s 0 %d,%d" % (patient.id, patient.insurance, patient.cash)
            elif patient.status == self.Patient.STATUS_TREAT:
                return "E012:%s 1 %d,%d,%d" % (patient.id, self.wait_queue.index(patient) + 1,
                                               patient.insurance, patient.cash)
            else:
                return "E012:%s 2 %d,%d" % (patient.id, patient.insurance, patient.cash)

    def op_cmd(self, cmd):
        cmd_dispatcher = {
            'i': self.op_init,
            'reg': self.op_register,
            'diag': self.op_diag,
            'pay': self.op_pay,
            'qu': self.op_query,
        }
        scmd = cmd.split('_', 1)
        return cmd_dispatcher[scmd[0]]() if len(scmd) <= 1 else cmd_dispatcher[scmd[0]](scmd[1])


def main():
    cmds = raw_input()
    h = Hospital()
    for cmd in cmds.split(","):
        if not cmd:
            continue
        print h.op_cmd(cmd)


if __name__ == '__main__':
    main()
