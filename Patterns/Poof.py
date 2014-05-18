from Patterns.PatternBase import PatternBase
class Chase(PatternBase):
	def __init__(self, *args):
		self.inputParams = {
						'triggerStep' : {
							'descriptionInPattern' : 'Trigger next step in sequence',
							'type' : 'pulse',
							'subType' : 'timer',
							'inputs' : [{
								'min' : 100,
								'max' : 3000, 
								'default' : 2000
							}]
						},
						'triggerSequence' : {
							'descriptionInPattern' : 'Trigger chase',
							'type' : 'pulse',
							'subType' : 'onOff'
						},
						'numberOn' : {
							'descriptionInPattern' : 'Number of poofers on at once',
							'type' : 'value',
							'subType' : 'int',
							'inputs' : [{
								'min' : 1,
								'max' : 5,
								'default' : 2
							}]
						},
						'stepping' : {
							'descriptionInPattern' : 'Number of poofers to jump per step',
							'type' : 'value',
							'subType' : 'int',
							'inputs' : [{
								'min' : 1,
								'max' : 5,
								'default' : 1
							}]
						},
						'numberPulses' : {
							'descriptionInPattern' : 'Number of pulses chasing each other',
							'type' : 'value',
							'subType' : 'int',
							'inputs' : [{
								'min' : 1,
								'max' : 3,
								'default' : 1
							}]
						}
					}
		PatternBase.__init__(self, *args)
		self.patternName = 'Poofer Chase'

		self.position = 0
		self.sequenceTriggered = True

	def triggerStep(self):
		self.position += self.inputs.stepping.getValue()
		if self.position > self.gridSize[1]:
			self.position -= self.gridSize[1]
			self.sequenceTriggered = self.inputs.triggerSequence.getValue()
		self.updateTriggerFunction()
		
	def triggerSequence(self):
		self.sequenceTriggered = True
	def getState(self, row, col):
		result = False
		if self.sequenceTriggered:
			spacing = self.gridSize[1] / self.inputs.numberPulses.getValue()
			intervalCount = 0
			while intervalCount < self.inputs.numberPulses.getValue() and not result:
				lowerLimit = self.position + intervalCount * spacing
				upperLimit = lowerLimit + self.inputs.numberOn.getValue()
				if col >= lowerLimit and col < upperLimit:
					result = True
				if self.inputs.numberPulses.getValue() > 1:
					lowerLimit = self.position - intervalCount * spacing
					upperLimit = lowerLimit + self.inputs.numberOn.getValue()
					if col >= lowerLimit and col < upperLimit:
						result = True
				intervalCount += 1
		return result
		
class AllPoof(PatternBase):
	def foo():
		pass
