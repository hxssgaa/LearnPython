# coding=utf-8
"""
自动售货系统

考生需要模拟实现一个简单的自动售货系统，实现投币、购买商品、退币、查询库存商品及存钱盒信息的功能。
系统初始化时自动售货机中商品为6种商品,商品的单价参见1.1规格说明，
存钱盒内放置1元、2元、5元、10元钱币，商品数量和钱币张数通过初始化命令设置，参见2.1 系统初始化。

具体说明见: http://117.78.32.67/exam/ShowProblemInfo?method=campusProblemInfo&id=2280

注意多层复杂sort的实现,就是通过多个sort来实现,sort能保证序列为稳定的序列
"""


class VirtualVendingMachine(object):
    GOOD_PRICES = (2, 3, 4, 5, 8, 6)
    GOOD_NAMES = ("A1", "A2", "A3", "A4", "A5", "A6")
    SAVING_BOX_PRICES = [1, 2, 5, 10]

    class Goods(object):
        def __init__(self, name, price, count):
            self.name = name
            self.price = price
            self.count = count

    class SavingBox(object):
        def __init__(self, value, count):
            self.value = value
            self.count = count

    def __init__(self):
        self.goods = [VirtualVendingMachine.Goods(self.GOOD_NAMES[i], self.GOOD_PRICES[i], 0) for i in range(0, 6)]
        self.saving_boxes = [VirtualVendingMachine.SavingBox(e, 0) for e in self.SAVING_BOX_PRICES]
        self.remain_balance = 0

    def op_reset(self, param):
        ps = param.split()
        goods_cnt, saving_cnt = ps[0], ps[1]
        for i, c in enumerate(goods_cnt.split("-")):
            self.goods[i].count = int(c)
        for i, c in enumerate(saving_cnt.split("-")):
            self.saving_boxes[i].count = int(c)
        self.remain_balance = 0
        return "S001:Initialization is successful"

    def op_pay(self, param):

        pay_amount = int(param)
        if not pay_amount in self.SAVING_BOX_PRICES:
            return "E002:Denomination error"
        m_max_change = self.saving_boxes[0].count * self.saving_boxes[0].value + \
                       self.saving_boxes[1].count * self.saving_boxes[1].value
        if pay_amount not in (1, 2) and m_max_change < pay_amount:
            return "E003:Change is not enough, pay fail"
        if self.remain_balance + pay_amount > 10:
            return "E004:Pay the balance is beyond the scope biggest"
        goods_sold_out = True
        for good in self.goods:
            if good.count > 0:
                goods_sold_out = False
                break
        if goods_sold_out:
            return "E005:All the goods sold out"
        self.remain_balance += pay_amount
        self.saving_boxes[self.SAVING_BOX_PRICES.index(pay_amount)].count += 1
        return "S002:Pay success,balance=%d" % self.remain_balance

    def op_buy(self, name):
        if name not in self.GOOD_NAMES:
            return "E006:Goods does not exist"
        buy_good = self.goods[self.GOOD_NAMES.index(name)]
        if buy_good.count == 0:
            return "E007:The goods sold out"
        if self.remain_balance < buy_good.price:
            return "E008:Lack of balance"
        self.remain_balance -= buy_good.price
        buy_good.count -= 1
        return "S003:Buy success,balance=%d" % self.remain_balance

    def is_safe_change(self, change):
        if self.remain_balance >= 5:
            rem = self.remain_balance - change
            cnt = min(rem // self.saving_boxes[1].value, self.saving_boxes[1].count)
            rem -= cnt * self.saving_boxes[1].value
            return self.saving_boxes[0].count * self.saving_boxes[0].value >= rem
        return True

    def op_change(self):
        if self.remain_balance <= 0:
            return "E009:Work failure"
        change_map = {e: 0 for e in self.SAVING_BOX_PRICES}
        for e in reversed(self.saving_boxes):
            if e.value > self.remain_balance or e.count == 0:
                continue
            cnt = min(self.remain_balance // e.value, e.count)
            if not self.is_safe_change(cnt * e.value):
                continue
            self.remain_balance -= cnt * e.value
            e.count -= cnt
            change_map[e.value] += cnt
        self.remain_balance = 0
        return "\n".join(["%d yuan coin number=%d" % (k, change_map[k]) for k in sorted(change_map.keys())])

    def op_query_good(self):
        query_goods = self.goods[:]
        query_goods.sort(key=lambda x: x.name)
        query_goods.sort(key=lambda x: x.count, reverse=True)
        return "\n".join(["%s %d %d" % (e.name, e.price, e.count) for e in query_goods])

    def op_query_saving_box(self):
        return "\n".join(["%d yuan coin number=%d" % (k.value, k.count) for k in self.saving_boxes])

    def op_query(self, param):
        try:
            query_cmd = int(param)
            if query_cmd not in (0, 1):
                return "E010:Parameter error"
            return self.op_query_good() if query_cmd == 0 else self.op_query_saving_box()
        except ValueError:
            return "E010:Parameter error"

    def op_cmd(self, cmd):
        """
        :type cmd: str
        :return: str
        """
        cmd_dispatcher = {
            'r': self.op_reset,
            'p': self.op_pay,
            'b': self.op_buy,
            'c': self.op_change,
            'q': self.op_query,
        }
        scmd = cmd.split(' ', 1)
        return cmd_dispatcher[scmd[0]]() if len(scmd) <= 1 else cmd_dispatcher[scmd[0]](scmd[1])


def main():
    cmds = raw_input()
    m = VirtualVendingMachine()
    for cmd in cmds.split(";"):
        if not cmd:
            continue
        print m.op_cmd(cmd)


if __name__ == '__main__':
    main()
