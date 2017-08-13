# coding=utf-8
"""
购物结算系统

考生需要模拟实现一个简单的购物结算系统，实现挑选和删除商品、按照最佳优惠方案进行结算、查询购物车订单信息及购物卡余额和积分的功能。
系统初始化时购物卡中有3000元余额和150积分，可以输入命令来初始化系统。

见:http://117.78.32.67/exam/ShowProblemInfo?method=campusProblemInfo&id=2279

r
o 1-15
b
o 1-2
o 2-3
o 0-4
b

这道题主要麻烦点在于对于所有的3种情况都需要考虑,就是不打折,打折以及满XX减XX
可以考虑分成大于500和不大于500的最小值情况分开考虑.
"""


class ShoppingBill(object):
    GOODS_ORDERS = (0, 1, 2)

    class Goods(object):
        __slots__ = ('order', 'price', 'discount', 'cut_bar', 'cut_amount')

        def __init__(self, **kwargs):
            for s in self.__slots__:
                setattr(self, s, None)
            for k, v in kwargs.items():
                setattr(self, k, v)

    class Orders(object):
        def __init__(self, order, count):
            self.order = order
            self.count = count

    def __init__(self):
        self.rem_balance = 3000
        self.point = 150
        self.goods = [
            ShoppingBill.Goods(order=0, price=10, discount=0.9, cut_bar=100, cut_amount=18),
            ShoppingBill.Goods(order=1, price=120, cut_bar=200, cut_amount=40),
            ShoppingBill.Goods(order=2, price=30, discount=0.5),
        ]
        self.charts = []

    def op_reset(self):
        self.__init__()
        return "S001"

    def op_order(self, param):
        ps = param.split("-")
        try:
            good_order, good_cnt = int(ps[0]), int(ps[1])
            if good_order not in self.GOODS_ORDERS or good_cnt <= 0 or good_cnt > 100:
                return "E002"
            if len(self.charts) >= 5:
                return "E003"
            self.charts.append(self.Orders(good_order, good_cnt))
            return "S002"
        except ValueError:
            return "E002"

    def op_clear(self, param):
        ps = param.split("-")
        try:
            good_order, good_cnt = int(ps[0]), int(ps[1])
            if good_order not in self.GOODS_ORDERS or good_cnt <= 0 or good_cnt > 100:
                return "E002"
            if not self.charts:
                return "E005"
            for i, e in enumerate(self.charts):
                if e.order == good_order and e.count == good_cnt:
                    del self.charts[i]
                    return "S003"
            return "E004"
        except ValueError:
            return "E002"

    def calculate_min_sum_helper(self, goods_sum, order, temp_sum, min_sum, above=True):
        if order >= len(goods_sum):
            if not min_sum:
                if above and temp_sum >= 500:
                    min_sum.append(temp_sum)
                elif not above and temp_sum < 500:
                    min_sum.append(temp_sum)
            elif temp_sum < min_sum[0]:
                if above and temp_sum >= 500:
                    min_sum[0] = temp_sum
                elif not above and temp_sum < 500:
                    min_sum[0] = temp_sum
            return
        for i in range(len(goods_sum[order])):
            self.calculate_min_sum_helper(goods_sum, order + 1, temp_sum + goods_sum[order][i], min_sum, above)

    def calculate_min_sum(self, goods_sum):
        res = []
        min_sum = []
        self.calculate_min_sum_helper(goods_sum, 0, 0, min_sum, False)
        res.append(min_sum[0] if min_sum else 0)
        min_sum = []
        self.calculate_min_sum_helper(goods_sum, 0, 0, min_sum, True)
        res.append(min_sum[0] if min_sum else 0)
        return res

    def get_goods_count_map(self):
        res = {e: 0 for e in self.GOODS_ORDERS}
        for e in self.charts:
            res[e.order] += e.count
        return res

    def op_balance(self):
        if not self.charts:
            return "E005"
        g_map = self.get_goods_count_map()
        goods_sum = [[0 for _ in range(3)] for _ in range(len(self.goods))]
        pay, pay_point, to_pay_point = 0, 0, 0
        for k, v in g_map.items():
            good = self.goods[int(k)]
            goods_sum[k][0] = good.price * v
            goods_sum[k][1] = goods_sum[k][0] * good.discount if good.discount else goods_sum[k][0]
            goods_sum[k][2] = (goods_sum[k][0] - goods_sum[k][0] // good.cut_bar * good.cut_amount) \
                if good.cut_bar else goods_sum[k][0]
        min_sum = self.calculate_min_sum(goods_sum)
        if min_sum[1] > 0:
            if min_sum[1] * 0.8 <= min_sum[1] - min(120, self.point):
                min_sum[1] *= 0.8
            else:
                to_pay_point = min(120, self.point)
                min_sum[1] -= to_pay_point
        if (min_sum[1] > min_sum[0] > 0) or min_sum[1] == 0:
            pay = min_sum[0]
        else:
            pay = min_sum[1]
            pay_point = to_pay_point
        if self.rem_balance < pay or self.point < pay_point:
            return "E006"
        self.rem_balance -= pay
        self.point -= pay_point
        self.point += pay // 10
        del self.charts[:]
        return "%d\n%d\n%d" % (pay, pay_point, pay // 10)

    def op_list(self, param):
        try:
            category = int(param)
            if category not in (0, 1):
                return "E002"
            if category == 0:
                return "%d\n%d" % (self.rem_balance, self.point)
            else:
                m = self.get_goods_count_map()
                return "%d\n%s" % (len(self.charts), "\n".join([str(m[k]) for k in sorted(m.keys())]))
        except ValueError:
            return "E002"

    def op_cmd(self, cmd):
        """
        :type cmd: str
        :rtype: str
        """
        cmd_dispatcher = {
            'r': self.op_reset,
            'o': self.op_order,
            'c': self.op_clear,
            'b': self.op_balance,
            'l': self.op_list,
        }
        scmd = cmd.split(' ', 1)
        return cmd_dispatcher[scmd[0]]() if len(scmd) <= 1 else cmd_dispatcher[scmd[0]](scmd[1])


def main():
    shopping_bill = ShoppingBill()
    while True:
        cmd = raw_input()
        if not cmd or cmd == 'e':
            break
        print shopping_bill.op_cmd(cmd)


if __name__ == '__main__':
    main()
