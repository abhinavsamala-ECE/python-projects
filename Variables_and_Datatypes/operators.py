"""OPERATOR PRECEDENCE
NOT>AND>OR"""

not True and False or True

#in this case, the NOT operator will be evaluated first, then the AND operator and finally the OR operator

#therefore it then becomes:
(not True) and False or True
= False and False or True
= False or True
= True  #since the OR operator is used, the final result will be True if any of the two operands is True