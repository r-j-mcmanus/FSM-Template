
class State:
	"""
    	class for holding a node in the fsm
    
    Member Variables
    ----------------
    	entryFn :
    		the function called when the state becomes the active state. Set to None on initalisation
    		When None, no function call is made.
    	exitFn :
    		the function called when the state is nolonger the active state. Set to None on initalisation
			When None, no function call is made.
    	transitions :
    		a list of transition objects defining the exits of the state

    Member Functions
    ----------------
    	addTransition:
    		Will add a transition to the state, stored in tansitions

    Member Class
    ------------
    	transition - holds the information for which state can be moved to, the requiremnt function to judge
    	if transition is posible, and the trnasition function to be called when requirement is met.

    """
	def __init__(self):
		self.entryFn = None
		self.exitFn = None
		self.transitions = []

	def addTransition(self, endID, tansitionReqFn, transitionFn):
		"""
    	Will add a transition to the state, stored in tansitions

    	Arguments
    	---------
    		endID - member of StateIDs, the id of the node transitioned to
    		tansitionReqFn - the function callecd to check transition
    		transitionFn - the function called upon transition
		"""
		self.transitions.append(self.transition(endID, tansitionReqFn, transitionFn))

	class transition:
		"""
		holds the information for which state can be moved to, the requiremnt function to judge
    	if transition is posible, and the trnasition function to be called when requirement is met.
    	"""
		def __init__(self, endID, transitionRequirementFn, transitionFn = None):
			self.endID = endID
			self.transitionRequirementFn = transitionRequirementFn 
			self.transitionFn = transitionFn



class StateIDs:
	"""
	List of IDs for the states
	"""
	RunningRight = "RunningRight"
	RunningLeft = "RunningLeft"
	Standing = "Standing"
	StartRunningRight = "StartRunningRight"
	StopRunningRight = "StopRunningRight"
	StartRunningLeft = "StartRunningLeft"
	StopRunningLeft = "StopRunningLeft"
	TurningLeft = "TurningLeft"
	TurningRight = "TurningRight"


def StateFactory(ID):
	"""
	Will return a state with the appropriate entry and exit function.

	Arguments
	---------
		ID - StateIDs member - the ide of the produced state
	"""
	mState = State()
	mState.ID = ID

	try:
		mState.entryFn = getattr(entryFns, ID)
	except AttributeError:
		print "state", ID, "has no entry fn"
		mState.entryFn = None
	
	try:
		mState.exitFn = getattr(exitFns, ID)
	except AttributeError:
		print "state", ID, "has no exit fn"
		mState.entryFn = None

	return mState



class entryFns:
	@staticmethod
	def Standing():
		print "entry Standing"

	@staticmethod
	def RunningRight():
		print "entry RunningRight"

	@staticmethod
	def RunningLeft():
		print "entry RunningLeft"

	@staticmethod
	def StartRunningRight():
		print "entry StartRunningRight"

	@staticmethod
	def StartRunningLeft():
		print "entry StartRunningLeft"

	@staticmethod
	def StopRunningRight():
		print "entry StopRunningRight"

	@staticmethod
	def StopRunningLeft():
		print "entry StopRunningLeft"

	@staticmethod
	def TurningLeft():
		print "entry TurningLeft"

	@staticmethod
	def TurningRight():
		print "entry TurningRight"



class exitFns:
	@staticmethod
	def Standing():
		print "exit Standing"

	@staticmethod
	def RunningRight():
		print "exit RunningRight"

	@staticmethod
	def RunningLeft():
		print "exit RunningLeft"

	@staticmethod
	def StartRunningRight():
		print "exit StartRunningRight"

	@staticmethod
	def StartRunningLeft():
		print "exit StartRunningLeft"

	@staticmethod
	def StopRunningLeft():
		print "exit StopRunningLeft"

	@staticmethod
	def StopRunningRight():
		print "exit StopRunningRight"

	@staticmethod
	def TurningLeft():
		print "exit TurningLeft"

	@staticmethod
	def TurningRight():
		print "exit TurningRight"





