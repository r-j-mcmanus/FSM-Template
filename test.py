
from FSM import FSM
from StateFactory import StateFactory, StateIDs

class transFns:
	@staticmethod
	def Foo1():
		print "transition 1"

	@staticmethod
	def Foo2():
		print "transition 2"

class transReqFns:
	@staticmethod
	def FooRight(data):
		if data == "Right":
			print "trans Right true"
			return True
		return False

	@staticmethod
	def FooLeft(data):
		if data == "Left":
			print "trans Left true"
			return True
		return False


	@staticmethod
	def FooNone(data):
		if data == "None":
			print "trans None true"
			return True
		return False

fsm = FSM(StateIDs.Standing)

fsm.addStates()

fsm.addTransition(StateIDs.Standing, StateIDs.StartRunningRight, 
					transReqFns.FooRight)
fsm.addTransition(StateIDs.StartRunningRight, StateIDs.RunningRight, 
					transReqFns.FooRight)
fsm.addTransition(StateIDs.Standing, StateIDs.StartRunningLeft, 
					transReqFns.FooLeft)
fsm.addTransition(StateIDs.StartRunningLeft, StateIDs.RunningLeft, 
					transReqFns.FooLeft)
fsm.addTransition(StateIDs.StartRunningLeft, StateIDs.Standing, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.StartRunningRight, StateIDs.Standing, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.RunningRight, StateIDs.TurningLeft, 
					transReqFns.FooLeft)
fsm.addTransition(StateIDs.RunningLeft, StateIDs.TurningRight, 
					transReqFns.FooRight)
fsm.addTransition(StateIDs.RunningRight, StateIDs.StopRunningRight, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.RunningLeft, StateIDs.StopRunningLeft, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.StopRunningRight, StateIDs.Standing, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.StopRunningLeft, StateIDs.Standing, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.TurningLeft, StateIDs.Standing, 
					transReqFns.FooNone)
fsm.addTransition(StateIDs.TurningRight, StateIDs.Standing, 
					transReqFns.FooNone)

#Standing
fsm.update("Right")
#StartRunningRight
fsm.update("Right")
#RunningRight
fsm.update("Left")
#TurningLeft
fsm.update("None")
#Standing
fsm.update("Left")
#StartRunninfLeft
fsm.update("None")
#Standing
fsm.update("Left")
#StartRunninfLeft
fsm.update("Left")
#RunninfLeft
