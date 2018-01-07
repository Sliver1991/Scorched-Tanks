import pygame,unittest, equ, tanks,draw, interface, gameLoop

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
        
    def testDrawSquare(self):
        self.assertTrue(draw.drawSquare(1,1,1,1,1,True),"Draw Failed")

    def testDrawPixel(self):
        self.assertTrue(draw.drawPixel(1,1,1,True),"Draw Failed")
        
    def testDrawLine(self):
        self.assertTrue(draw.drawLine(1,1,1,1,1,1,True),"Draw Failed")
        
    def testDrawCircle(self):
        self.assertTrue(draw.drawCircle(1,1,1,1,True),"Draw Failed")
        
    def testDrawPoly(self):
        self.assertTrue(draw.drawPoly(1,1,True),"Draw Failed")
        
    def testDrawLeftArrow(self):
        self.assertTrue(draw.drawLeftArrow(1,1,1,True),"Draw Failed")
        
    def testDrawRightArrow(self):
        self.assertTrue(draw.drawRightArrow(1,1,1,True),"Draw Failed")
        
    def testDrawImage(self):
        self.assertTrue(draw.drawImage(1,1,1,1,1,1,True),"Draw Failed")
    
    def testInterface(self):
        self.assertTrue(interface.drawInterface(True),"Interface Failed")
          
    def testStats(self):
        self.assertTrue(interface.drawStats(1,1,1,True),"Stats Failed") 
        
    def testGameLoop(self):
        self.assertTrue(gameLoop.gameLoop(True),"Game Loop Failed")
        
    def testCycle(self):
        self.assertTrue(gameLoop.gameCycle(True),"Game Cycle Failed")
        
unittest.main()

pygame.quit()