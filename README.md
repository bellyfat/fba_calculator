# FBA Revenue Calculator
Amazon FBA Revenue Calculator allows you to get the Amazon fees associated with your product when selling FBA.

##How To Use
######You can use this at the following url:

	https://ocwpmnb46i.execute-api.us-west-2.amazonaws.com/beta/api/v1/fba-revenue-calculator?

######Required Parameters:

	1. length
	2. width
	3. height
	4. weight

######Optional Parameters

	1. media (True or False)
	2. pro (True or False)
	3. appareal (True or False)


##Limits
1. 200 requests a second
2. 500 burst requests a second

##Sample
####Here is a sample request
	https://ocwpmnb46i.execute-api.us-west-2.amazonaws.com/beta/api/v1/fba-revenue-calculator?unit_weight=0.15&pro=False&width=0.6&media=True&height=7.5&apparel=False&length=5.3

####Here is the response
	{'cost': 2.56}

##Testing
	`python test.py`

###TODO
1. Currently the large standard media fails.
2. Currently the special oversized fails because a misdescription on Amazon's sample page.