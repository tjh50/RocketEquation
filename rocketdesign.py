import math

class Spaceship:
      def __init__(self,payload):
            self.payload = payload
            self.stagelist = []
            self.initialMass = self.payload

      def addStage(self,Stage):
            print('Stage Added')
            self.stagelist.append(Stage)
            self.initialMass += Stage.totalMass(Stage.propList)
            return self.stagelist

      def removeStage(self,Stage):
            print("Staging in 3...2....1....")
            print(self.initialMass)
            self.initialMass -= Stage.totalMass(Stage.propList)
            print(self.initialMass)
            return self.initialMass
            
class Stage:
      def __init__(self,structMass,propList):
            self.structMass = structMass
            self.propList = propList
      def getIsp(self,lst):
            self.isp = 0
            self.flowList = []
            for i in range(0,len(lst)):
                  x = lst[i].isp * lst[i].flowRate
                  self.isp += x
                  self.flowList.append(lst[i].flowRate)
            self.isp = self.isp/sum(self.flowList)
            return self.isp
      def totalMass(self,lst):
            self.totLst = []
            for i in range(0,len(lst)):
                  self.totLst.append(lst[i].totalMass)
            self.totMass = sum(self.totLst) + self.structMass
            return self.totMass
      def fuelMass(self,lst):
            self.fuelLst = []
            for i in range(0,len(lst)):
                  self.fuelLst.append(lst[i].fuelMass)
            self.fuelMass = sum(self.fuelLst)
            return self.fuelMass

      
class Mission:
      def __init__(self,name):
            self.name = name
            self.deltaV = []
            self.manueverList = []
            
      def missionSummary(self,expect,reality):
            for i in range(0,len(expect)):
                  if mission.deltaV[i] >= mission.manueverList[i].targetV :
                        print("Manuever %s  was successful! Rocket has reached %s !" %(i,mission.manueverList[i].desiredLoc))
                        print("The delta V produced in this manuever was %s" %(mission.deltaV[i]))
                  else:
                        print("Manuever %s was a failure" %(i))
                        print(mission.deltaV[i])
            
            
      def rocketEquation(self,StageList):
            for i in range(0,len(StageList)):
                  finalMass = craft.initialMass - StageList[i].fuelMass(StageList[i].propList)
                  deltaV = StageList[i].getIsp(StageList[i].propList)*9.81 * math.log((craft.initialMass)/(finalMass))
                  self.deltaV.append(deltaV)
                  craft.removeStage(StageList[i])
      def missionSetup(self):
            numManu = int(input("How many manuevers are needed in this mission?" ))
            for i in range(0,numManu):
                  desiredLoc = input("Where should the ship be by the end of this manuever")
                  targetV = int(input("What is the delta V necessary for performing this manuever"))
                  self.manueverList.append(Manuever(desiredLoc,targetV))
                                   
                  
class Manuever:
      def __init__(self,desiredLoc,targetV):
            self.desiredLoc = desiredLoc
            self.targetV = targetV
class Engine:
      def __init__(self,isp,flowRate,mass,fuelMass):
            self.isp = isp
            self.flowRate = flowRate
            self.mass = mass
            self.fuelMass = fuelMass
            self.totalMass = self.fuelMass + self.mass
            

print("Welcome to TJH Space Lab!")
missionName = input("What is the name of this mission??")
mission = Mission(missionName)
mission.missionSetup()
payload = int(input("What is the mass of your payload?"))
craft = Spaceship(payload)
numStage = int(input("How many stages will your rocket have?"))
counter = 1
if numStage <=  0:
      print("A rocket must have at least one stage to produce deltaV ")      
while counter <= numStage:
      structMass = int(input("What is the structural mass of this Stage?"))
      propList = []
      propNum = int(input("How many propulsion devices are on Stage %s" %(counter)))
      for i in range(0,propNum):
            isp = int(input("What is the specific impulse of this engine?"))
            mdot = int(input("What is the mass flow rate of this engine?"))
            mass = int(input("What is the structural mass of the engine itself?"))
            fuelMass = int(input("What is the amount of fuel consumed by this engine in this stage? "))
            propList.append(Engine(isp,mdot,mass,fuelMass))
      stage = Stage(structMass,propList)
      craft.addStage(Stage(structMass,propList))
      counter += 1
mission.rocketEquation(craft.stagelist)
mission.missionSummary(mission.manueverList,mission.deltaV)


      
            



