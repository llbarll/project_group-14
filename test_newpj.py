import unittest
import newpj


with open("testfeeds.txt") as f:
    for i, l in enumerate(f):
        pass
i += 1

with open("testplayers.txt") as f:
    for n, l in enumerate(f):
        pass
n += 1

with open("testchamps.txt") as f:
    for j, l in enumerate(f):
        pass
j += 1


class TestNewPj(unittest.TestCase):
    
    def test_CheckLogin_f(self):
        
        result = newpj.CheckLogin_f("testplayers.txt","testname","testpass")
        self.assertEqual(result,1)
    def test_FeedsUp_f(self):
        
        newpj.FeedsUp_f("testfeeds.txt","testfeed","testname")
        with open("testfeeds.txt") as f:
            for k, l in enumerate(f):
                pass
        k += 1
        self.assertEqual(i+1,k)
        
    def test_UpdateScore(self):
     
        newpj.UpdateScore("testchamps.txt")
        
        with open("testchamps.txt") as f:
            lines = f.readlines()
        
        lines[1] = str(lines[1]).split()
        lines[2] = str(lines[2]).split()
     
     
        self.assertTrue(int(lines[1][1])>=int(lines[2][1]))
        
    def test_CSign_f(self):
     
        newpj.CSign_f("testplayers.txt","testchamps.txt","newname","newpass")
        
        with open("testchamps.txt") as f:
            lines1 = f.readlines()
            
        with open("testplayers.txt") as f:
            lines2 = f.readlines()
        
        lines1[j] = str(lines1[j]).split()
        lines2[n] = str(lines2[n]).split()
        
        self.assertEqual(lines1[j][1],'0')
        self.assertEqual(lines2[n][0],'newname')
        self.assertEqual(lines2[n][1],'newpass')
    
    def test_custom_sort(self):
     
        L = [("Alice", 25), ("Bob", 20), ("Alex", 5)]
        L.sort(key=newpj.custom_sort)
        T = [('Alex', 5), ('Bob', 20), ('Alice', 25)]
        self.assertEqual(L,T)
       
    def test_CSing_c(self):
     
        result = newpj.CSing_c("testchamps.txt","blablabla")
        self.assertEqual(result,0)
        result = newpj.CSing_c("testchamps.txt","testname")
        self.assertEqual(result,1)
    
    def test_Score_f(self):
         
        with open("testchamps.txt") as f:
            lines = f.readlines()
        
        lines[0] = str(lines[0]).split()
        oldscore = int(lines[0][1])
        newpj.Score_f("testchamps.txt",'toptest')
        
        with open("testchamps.txt") as f:
            lines2 = f.readlines()
        
        lines2[0] = str(lines2[0]).split()
        
        self.assertTrue(int(lines2[0][1])==oldscore+1)
    
if __name__ == '__main__':
    unittest.main()