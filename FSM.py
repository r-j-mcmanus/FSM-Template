
from StateFactory import StateFactory, StateIDs


class FSM:
	def __init__(self, startStateID):
		self.__states = {
			#stateID : state
		}
		self.__activeID = startStateID
		self.addState(startStateID)

	#----------------------------------------------------------------#

	#fns for making the FMS

	def addState(self, ID):
		self.__states[ID] = StateFactory(ID)

	def addStates(self):
		attr = dir(StateIDs)
		attr.remove("__doc__")
		attr.remove("__module__")
		ID = None
		for i in range(len(attr)):
			ID = getattr(StateIDs, attr[i])
			self.__states[ID] = StateFactory(ID)

	def addTransition(self, startID, endID, tansitionReqFn, transitionFn = None):
		try:
			self.__states[startID].addTransition(endID, tansitionReqFn, transitionFn)
		except KeyError, message:
			print "attepted to add transition from non existant state with ID", startID
			print message
			raise SystemExit

	#----------------------------------------------------------------#

	def update(self, data):

		activestate = self.__states[self.__activeID]
		test = False
		for trans in activestate.transitions:
			if trans.transitionRequirementFn(data) == True:
				self.__lastID = self.__activeID
				self.__activeID = trans.endID
				transitionFn = trans.transitionFn
				test = True
				break

		if test == True:
			exitFn = activestate.exitFn
			try:
				entryFn = self.__states[self.__activeID].entryFn
			except KeyError, message:
				print "Attempted to transition to a state", self.__activeID ,"that does not exist"
				print message
				raise SystemExit

			if exitFn!=None:
				exitFn() 
			if transitionFn!=None:
				transitionFn() 
			if entryFn!=None:
				entryFn() 


		

