import os
import sys
import Logger
import Assessment
import Util

Util.clear()


Logger.logIt(os.path.splitext(os.path.basename(__file__))[0])
noOfQuestions = int(sys.argv[1])

QUESTIONS = [("0+0", "0"), ("0+1", "1"), ("0+2", "2"), ("0+3", "3"), ("0+4", "4"), ("0+5", "5"), ("0+6", "6"),
             ("0+7", "7"), ("0+8", "8"), ("0+9", "9"), ("0+10", "10"), ("0+11", "11"), ("0+12", "12"), ("0+13", "13"),
             ("0+14", "14"), ("0+15", "15"), ("0+16", "16"), ("0+17", "17"), ("0+18", "18"), ("0+19", "19"),
             ("0+20", "20"), ("1+1", "2"), ("1+2", "3"), ("1+3", "4"), ("1+4", "5"), ("1+5", "6"), ("1+6", "7"),
             ("1+7", "8"), ("1+8", "9"), ("1+9", "10"), ("1+10", "11"), ("1+11", "12"), ("1+12", "13"), ("1+13", "14"),
             ("1+14", "15"), ("1+15", "16"), ("1+16", "17"), ("1+17", "18"), ("1+18", "19"), ("1+19", "20"),
             ("2+2", "4"), ("2+3", "5"), ("2+4", "6"), ("2+5", "7"), ("2+6", "8"), ("2+7", "9"), ("2+8", "10"),
             ("2+9", "11"), ("2+10", "12"), ("2+11", "13"), ("2+12", "14"), ("2+13", "15"), ("2+14", "16"),
             ("2+15", "17"), ("2+16", "18"), ("2+17", "19"), ("2+18", "20"), ("3+3", "6"), ("3+4", "7"), ("3+5", "8"),
             ("3+6", "9"), ("3+7", "10"), ("3+8", "11"), ("3+9", "12"), ("3+10", "13"), ("3+11", "14"), ("3+12", "15"),
             ("3+13", "16"), ("3+14", "17"), ("3+15", "18"), ("3+16", "19"), ("3+17", "20"), ("4+4", "8"), ("4+5", "9"),
             ("4+6", "10"), ("4+7", "11"), ("4+8", "12"), ("4+9", "13"), ("4+10", "14"), ("4+11", "15"), ("4+12", "16"),
             ("4+13", "17"), ("4+14", "18"), ("4+15", "19"), ("4+16", "20"), ("5+5", "10"), ("5+6", "11"),
             ("5+7", "12"), ("5+8", "13"), ("5+9", "14"), ("5+10", "15"), ("5+11", "16"), ("5+12", "17"),
             ("5+13", "18"), ("5+14", "19"), ("5+15", "20"), ("6+6", "12"), ("6+7", "13"), ("6+8", "14"), ("6+9", "15"),
             ("6+10", "16"), ("6+11", "17"), ("6+12", "18"), ("6+13", "19"), ("6+14", "20"), ("7+7", "14"),
             ("7+8", "15"), ("7+9", "16"), ("7+10", "17"), ("7+11", "18"), ("7+12", "19"), ("7+13", "20"),
             ("8+8", "16"), ("8+9", "17"), ("8+10", "18"), ("8+11", "19"), ("8+12", "20"), ("9+9", "18"),
             ("9+10", "19"), ("9+11", "20")]

Assessment.assess(QUESTIONS, noOfQuestions)