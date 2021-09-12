class Car(object):

    def __init__(self, model_name, mileage, manufacture):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        print('{0.manufacture}の{0.model_name}(燃費:{0.mileage}), アクセル全開!!'.format(self))


    def brakes(self):
        print('{0.manufacture}の{0.model_name}(燃費:{0.mileage}), ブレーキ!!'.format(self))


if __name__ == '__main__':
    conti_gt = Car('Bentley Continental', 4, 'Bentley')
    prius = Car('Prius', 20, 'TOYOTA')
    print(prius.mileage)
    prius.gas()
    prius.brakes()
    conti_gt.gas()