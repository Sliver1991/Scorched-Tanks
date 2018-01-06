import pygame,unittest, equ, tanks

class TestSE(unittest.TestCase):
    
    def testLinear(self):
        angle = 20
        power = 100
        time = 5
        expected = (156,57)
        test = equ.linear(angle,power,time)
        self.assertEqual(test,expected,"Linear Failed")
        
    def testBallistic(self):
        angle = 20
        power = 100
        time = 5
        expected = (31,10)
        self.assertEqual(equ.ballistic(angle,power,time),expected,"Ballistic Failed")
        
    def testGuided(self):
        angle = 20
        power = 100
        time = 5
        expected = (50, 92)
        self.assertEqual(equ.guided(angle,power,time),expected,"Guided Failed")
    
    def testCrazy(self):
        angle = 20
        power = 100
        time = 5
        expected = (33, -80)
        self.assertEqual(equ.crazy(angle,power,time),expected,"Crazy Failed")
        
    def testDistance(self):
        x1,y1 = 10,20
        x2,y2 = 20,20
        expected = 10
        self.assertEqual(equ.distance(x1,y1,x2,y2),expected,"Distance Failed")
    
    def testTurnOrder(self):
        players = 2
        turn = tanks.turnOrder(players)
        self.assertTrue(turn==[1,2] or turn==[2,1],'Turn Order Failed')
        

unittest.main()

pygame.quit()