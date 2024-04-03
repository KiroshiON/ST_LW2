import math
import unittest

class Calculator:
    
    def frequency_of_treatment(self, T):
        return 1/T
    
    def period_of_treatment_corner(self, W):
        return (2 * 3.14)/W
    
    def period_of_treatment_time(self, t, N):
        return t/N
        
    def linear_skewness(self, S, t):
        return S/t
    
    def linear_skewness_period(self, r, T):
        return (2 * 3.14 * r) / T
    
    def angular_velocity(self, angle_of_rotation, t):
        return angle_of_rotation / t
    
    def angular_velocity_period(self, T):
        return (2 * 3.14) / T
    
    def angular_velocity_to_linear_velocity(self, W, r):
        return W * r
    
    def centripetal_acceleration(self, V, r):
        return (V**2) / r
    
    def centripetal_acceleration_corner(self, W, r):
        return (W**2) * r
    
    def choice(self):
        print("Выберите элемент, который хотите рассчитать")
        print(" 1 - Частота обращения \n 2 - Период обращения через угловую скорость\n 3 - Период обращения через время\n 4 - Линейная скорость \n 5 - Линейная скорость, через период обращения\n 6 - Угловая скорость \n 7 - Угловая скорость, через период \n 8 - Перевод из угловой скорости в линейную\n 9 - Центростремительное ускорение\n 10 - Центростермительное ускорение, через линейную скорость\n")
        input_string = int(input("Введите номер: "))
        
        
        if input_string == 1:
            T = float(input("Введите период: "))
            return self.frequency_of_treatment(T)
        
        elif input_string == 2:
            W = float(input("Введите угловую скорость: "))
            return self.period_of_treatment_corner(W)
        
        elif input_string == 3:
            t = float(input("Введите время: "))
            N = float(input("Введите количество вращений: "))
            return self.period_of_treatment_time(t, N)
       
        elif input_string == 4:
            S = float(input("Введите расстояние: "))
            t = float(input("Введите время: "))
            return self.linear_skewness(S, t)
        
        elif input_string == 5:
            r = float(input("Введите радиус: "))
            T = float(input("Введите период: "))
            return self.linear_skewness_period(r, T)
        
        elif input_string == 6:
            angle_of_rotation = float(input("Введите угол поворота: "))
            t = float(input("Введите время: "))
            return self.angular_velocity(angle_of_rotation, t)
        
        elif input_string == 7:
            T = float(input("Введите период: "))
            return self.angular_velocity_period(T)
        
        elif input_string == 8:
            W = float(input("Введите угловую скорость: "))
            r = float(input("Введите радиус: "))
            return self.angular_velocity_to_linear_velocity(W, r)
        
        elif input_string == 9:
            V = float(input("Линейная скорость: "))
            r = float(input("Введите радиус: "))
            return self.centripetal_acceleration(V, r)
        
        elif input_string == 10:
            W = float(input("Введите угловую скорость: "))
            r = float(input("Введите радиус: "))
            return self.centripetal_acceleration_corner(W, r)
        
        else:
            print("Некорректный номер операции")
    
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_frequency_of_treatment(self):
        self.assertEqual(self.calculator.frequency_of_treatment(2), 0.5)
        self.assertEqual(self.calculator.frequency_of_treatment(3), 1/3)

    def test_period_of_treatment_corner(self):
        self.assertAlmostEqual(self.calculator.period_of_treatment_corner(2), 3.14, places=2)
        self.assertAlmostEqual(self.calculator.period_of_treatment_corner(3), 2.09, places=2)

    def test_period_of_treatment_time(self):
        self.assertEqual(self.calculator.period_of_treatment_time(2, 2), 1)
        self.assertEqual(self.calculator.period_of_treatment_time(3, 3), 1)

    def test_linear_skewness(self):
        self.assertEqual(self.calculator.linear_skewness(2, 2), 1)
        self.assertEqual(self.calculator.linear_skewness(3, 3), 1)

    def test_linear_skewness_period(self):
        self.assertAlmostEqual(self.calculator.linear_skewness_period(2, 2), 6.28, places=2)
        self.assertAlmostEqual(self.calculator.linear_skewness_period(3, 3), 6.28, places=2)


    def test_angular_velocity(self):
        self.assertEqual(self.calculator.angular_velocity(2, 2), 1)
        self.assertEqual(self.calculator.angular_velocity(3, 3), 1)

    def test_angular_velocity_period(self):
        self.assertAlmostEqual(self.calculator.angular_velocity_period(2), 3.14, places=2)
        self.assertAlmostEqual(self.calculator.angular_velocity_period(3), 2.09, places=2)

    def test_angular_velocity_to_linear_velocity(self):
        self.assertEqual(self.calculator.angular_velocity_to_linear_velocity(2, 2), 4)
        self.assertEqual(self.calculator.angular_velocity_to_linear_velocity(3, 3), 9)

    def test_centripetal_acceleration(self):
        self.assertAlmostEqual(self.calculator.centripetal_acceleration(2, 2), 2, places=2)
        self.assertAlmostEqual(self.calculator.centripetal_acceleration(3, 3), 3, places=2)

    def test_centripetal_acceleration_corner(self):
        self.assertAlmostEqual(self.calculator.centripetal_acceleration_corner(2, 2), 8, places=2)
        self.assertAlmostEqual(self.calculator.centripetal_acceleration_corner(3, 3), 27, places=2)

if __name__ == '__main__':
    unittest.main()
