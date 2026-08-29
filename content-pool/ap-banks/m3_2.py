# MACRO 3.2 Multipliers — 50 questions
# Every numeric result used below, worked out:
#   spending multiplier k = 1/(1-MPC) = 1/MPS ; tax multiplier = -MPC/MPS ; balanced budget = 1
#   MPC 0.5  -> MPS 0.5  -> k = 2    -> tax multiplier -1
#   MPC 0.6  -> MPS 0.4  -> k = 2.5  -> tax multiplier -1.5
#   MPC 0.75 -> MPS 0.25 -> k = 4    -> tax multiplier -3
#   MPC 0.8  -> MPS 0.2  -> k = 5    -> tax multiplier -4
#   MPC 0.9  -> MPS 0.1  -> k = 10   -> tax multiplier -9
#   MPC 0.95 -> MPS 0.05 -> k = 20   -> tax multiplier -19
# Applications:
#   G +100, MPC 0.8      -> 5 x 100 = 500
#   G +50,  MPC 0.75     -> 4 x 50  = 200
#   I +40,  MPS 0.2      -> 5 x 40  = 200
#   I +30,  MPC 0.6      -> 2.5 x 30 = 75
#   T -200, MPC 0.8      -> -4 x (-200) = +800
#   T +100, MPC 0.9      -> -9 x (+100) = -900
#   T -80,  MPC 0.75     -> -3 x (-80) = +240
#   G +100 and T +100, MPC 0.8 -> 500 - 400 = +100  (balanced budget multiplier 1)
#   Gap 400, MPC 0.75 (k=4) -> spending needed 400/4  = 100
#   Gap 600, MPC 0.8  (k=5) -> spending needed 600/5  = 120
#   Gap 400, MPC 0.8  (tax multiplier 4) -> tax cut 400/4 = 100
#   Gap 500, MPC 0.9  (k=10) -> spending 50 ; tax cut 500/9 = 55.6
#   MPS 0.25, G +60 -> 4 x 60 = 240
#   Total change 750 from G +150 -> k = 5 -> MPC = 0.8
#   Total change 300 from T -100 -> tax multiplier magnitude 3 -> MPC = 0.75
TOPIC = ('3.2', 'Multipliers', 3)
QUESTIONS = [
 dict(q='The marginal propensity to consume is defined as', choices=[
   'total consumption divided by total income',
   'the fraction of each additional dollar of disposable income that is spent on consumption',
   'the fraction of income paid in taxes',
   'the change in saving divided by the change in consumption',
   'the average level of consumer spending'], ans=1,
   why='MPC is a marginal concept: the change in consumption divided by the change in disposable income.'),
 dict(q='The marginal propensity to save is', choices=[
   'the fraction of each additional dollar of disposable income that is saved',
   'the interest rate on savings accounts',
   'always equal to the MPC',
   'the fraction of income spent on imports',
   'total saving divided by total income'], ans=0,
   why='MPS is the change in saving divided by the change in disposable income.'),
 dict(q='In a simple model with no taxes or trade, MPC + MPS equals', choices=[
   '1',
   'the multiplier',
   'the interest rate',
   '0',
   '0.5'], ans=0,
   why='Every additional dollar of disposable income is either spent or saved, so the two fractions sum to one.'),
 dict(q='If the MPC is 0.8, the MPS equals', choices=[
   '0.05',
   '0.1',
   '0.2',
   '0.25',
   '0.8'], ans=2,
   why='MPS = 1 − MPC = 1 − 0.8 = 0.2.'),
 dict(q='If the MPS is 0.25, the MPC equals', choices=[
   '0.25',
   '0.5',
   '0.6',
   '0.75',
   '0.9'], ans=3,
   why='MPC = 1 − MPS = 1 − 0.25 = 0.75.'),
 dict(q='The spending multiplier is given by', choices=[
   'MPC/MPS',
   '1/(1 − MPC), which is the same as 1/MPS',
   '1/MPC',
   '−MPC/MPS',
   'MPC + MPS'], ans=1,
   why='Because MPS = 1 − MPC, the two expressions for the spending multiplier are identical.'),
 dict(q='If the MPC is 0.75, the spending multiplier equals', choices=[
   '0.75',
   '1.33',
   '3',
   '4',
   '5'], ans=3,
   why='1/(1 − 0.75) = 1/0.25 = 4.'),
 dict(q='If the MPS is 0.1, the spending multiplier equals', choices=[
   '0.9',
   '1.1',
   '5',
   '9',
   '10'], ans=4,
   why='The spending multiplier is 1/MPS = 1/0.1 = 10.'),
 dict(q='If the MPC is 0.5, the spending multiplier equals', choices=[
   '0.5',
   '1',
   '1.5',
   '2',
   '5'], ans=3,
   why='1/(1 − 0.5) = 2, the smallest multiplier among the commonly used MPC values.'),
 dict(q='A larger MPC produces', choices=[
   'a multiplier of exactly one',
   'a smaller spending multiplier',
   'a larger spending multiplier, because more of each round of income is re-spent',
   'no change in the multiplier',
   'a negative multiplier'], ans=2,
   why='The higher the fraction re-spent at each round, the longer the chain of induced spending.'),
 dict(q='The multiplier process works because', choices=[
   'the government prints money to match new spending',
   "one person's spending becomes another person's income, part of which is spent again",
   'prices fall when spending rises',
   'banks are required to lend all deposits',
   'taxes fall automatically'], ans=1,
   why='Induced consumption at each successive round is what turns an initial injection into a larger total change in GDP.'),
 dict(q='Government spending increases by $100 billion and the MPC is 0.8. The total change in real GDP, in billions of dollars, is', choices=[
   '80',
   '100',
   '180',
   '400',
   '500'], ans=4,
   why='The multiplier is 1/0.2 = 5, and 5 × 100 = 500.'),
 dict(q='Government spending increases by $50 billion and the MPC is 0.75. The total change in real GDP, in billions of dollars, is', choices=[
   '37.5',
   '50',
   '150',
   '200',
   '250'], ans=3,
   why='The multiplier is 1/0.25 = 4, and 4 × 50 = 200.'),
 dict(q='Investment spending rises by $40 billion in an economy with an MPS of 0.2. Real GDP changes, in billions of dollars, by', choices=[
   '8',
   '40',
   '80',
   '160',
   '200'], ans=4,
   why='The multiplier is 1/0.2 = 5, so the change is 5 × 40 = 200.'),
 dict(q='Investment rises by $30 billion where the MPC is 0.6. Real GDP rises, in billions of dollars, by', choices=[
   '18',
   '30',
   '48',
   '75',
   '300'], ans=3,
   why='The multiplier is 1/0.4 = 2.5, and 2.5 × 30 = 75.'),
 dict(q='Government spending rises by $60 billion and the MPS is 0.25. Real GDP rises, in billions of dollars, by', choices=[
   '15',
   '60',
   '180',
   '240',
   '300'], ans=3,
   why='The multiplier is 1/0.25 = 4, so 4 × 60 = 240.'),
 dict(q='The tax multiplier is given by', choices=[
   '−MPC/MPS',
   '−1/MPS',
   'MPS/MPC',
   'MPC × MPS',
   '1/MPS'], ans=0,
   why='A tax change first affects disposable income, and only the MPC fraction of it is spent, so the multiplier is smaller in magnitude and opposite in sign.'),
 dict(q='The tax multiplier is smaller in absolute value than the spending multiplier because', choices=[
   'taxes do not affect consumption',
   'the government spends more efficiently than households',
   'the MPC is greater than one',
   'taxes are collected slowly',
   'part of a tax cut is saved rather than spent, so the first round of new spending is less than the full amount'], ans=4,
   why='Government spending enters the expenditure stream in full, while a tax cut enters only to the extent households consume it.'),
 dict(q='If the MPC is 0.8, the tax multiplier equals', choices=[
   '-5',
   '-4',
   '-1.25',
   '-0.8',
   '4'], ans=1,
   why='−MPC/MPS = −0.8/0.2 = −4.'),
 dict(q='If the MPC is 0.9, the tax multiplier equals', choices=[
   '-10',
   '-9',
   '-1.11',
   '-0.9',
   '9'], ans=1,
   why='−0.9/0.1 = −9.'),
 dict(q='If the MPS is 0.25, the tax multiplier equals', choices=[
   '-4',
   '-3',
   '-1.33',
   '-0.75',
   '3'], ans=1,
   why='MPC is 0.75, so the tax multiplier is −0.75/0.25 = −3.'),
 dict(q='Taxes are cut by $200 billion and the MPC is 0.8. Real GDP changes, in billions of dollars, by', choices=[
   '160',
   '200',
   '640',
   '800',
   '1,000'], ans=3,
   why='The tax multiplier is −4, and −4 × (−200) = +800.'),
 dict(q='Taxes are raised by $100 billion and the MPC is 0.9. Real GDP changes, in billions of dollars, by', choices=[
   '-1,000',
   '-900',
   '-100',
   '-90',
   '900'], ans=1,
   why='The tax multiplier is −9, so the change is −9 × 100 = −900.'),
 dict(q='Taxes are cut by $80 billion and the MPC is 0.75. Real GDP changes, in billions of dollars, by', choices=[
   '60',
   '80',
   '160',
   '240',
   '320'], ans=3,
   why='The tax multiplier is −3, and −3 × (−80) = +240.'),
 dict(q='A $100 billion tax cut with an MPC of 0.8 raises consumption in the first round, in billions of dollars, by', choices=[
   '20',
   '80',
   '100',
   '400',
   '500'], ans=1,
   why='Households spend the MPC fraction of the extra disposable income, that is 0.8 × 100 = 80, and save the rest.'),
 dict(q='The balanced budget multiplier equals', choices=[
   '0',
   '1',
   '1/MPS',
   '−MPC/MPS',
   'the MPC'], ans=1,
   why='An equal increase in spending and taxes raises GDP by exactly the amount of the change, regardless of the MPC.'),
 dict(q='Government spending and taxes both rise by $100 billion and the MPC is 0.8. Real GDP changes, in billions of dollars, by', choices=[
   '0',
   '20',
   '100',
   '400',
   '900'], ans=2,
   why='The spending effect is +500 and the tax effect is −400, and 500 − 400 = 100, exactly the size of the budget change.'),
 dict(q='The balanced budget multiplier is 1 because', choices=[
   'taxes have no effect on GDP',
   'the MPC equals the MPS',
   'the government always saves the tax revenue',
   'spending and taxes have identical effects',
   'the spending multiplier exceeds the absolute value of the tax multiplier by exactly one'], ans=4,
   why='1/MPS minus MPC/MPS equals (1 − MPC)/MPS, which is MPS/MPS = 1.'),
 dict(q='An economy has an MPC of 0.75 and a recessionary gap of $400 billion. Closing the gap purely with government spending requires an increase, in billions of dollars, of', choices=[
   '80',
   '100',
   '133',
   '300',
   '400'], ans=1,
   why='The multiplier is 4, so the required spending is 400/4 = 100.'),
 dict(q='An economy has an MPC of 0.8 and a recessionary gap of $600 billion. The required increase in government spending, in billions of dollars, is', choices=[
   '100',
   '120',
   '150',
   '480',
   '600'], ans=1,
   why='With a multiplier of 5, the injection needed is 600/5 = 120.'),
 dict(q='An economy has an MPC of 0.8 and a recessionary gap of $400 billion. Closing it purely with a tax cut requires a cut, in billions of dollars, of', choices=[
   '80',
   '100',
   '125',
   '320',
   '400'], ans=1,
   why='The tax multiplier has magnitude 4, so the cut needed is 400/4 = 100.'),
 dict(q='An economy has an MPC of 0.9 and a recessionary gap of $500 billion. The government spending increase needed, in billions of dollars, is', choices=[
   '45',
   '50',
   '56',
   '450',
   '500'], ans=1,
   why='The multiplier is 10, so 500/10 = 50 is enough.'),
 dict(q='To close a given recessionary gap, the required tax cut is', choices=[
   'exactly equal to it',
   'always zero',
   'independent of the MPC',
   'smaller than the required increase in government spending',
   'larger than the required increase in government spending'], ans=4,
   why='Because the tax multiplier is smaller in magnitude, a bigger tax change is needed to move GDP by the same amount.'),
 dict(q='An increase in government spending of $150 billion raises real GDP by $750 billion. The MPC must be', choices=[
   '0.2',
   '0.5',
   '0.75',
   '0.8',
   '0.9'], ans=3,
   why='The multiplier is 750/150 = 5, so MPS = 0.2 and MPC = 0.8.'),
 dict(q='A tax cut of $100 billion raises real GDP by $300 billion. The MPC must be', choices=[
   '0.25',
   '0.5',
   '0.6',
   '0.75',
   '0.8'], ans=3,
   why='The tax multiplier magnitude is 3, and MPC/(1 − MPC) = 3 gives MPC = 0.75.'),
 dict(q='An economy has an MPC of 0.95. The spending multiplier is', choices=[
   '0.95',
   '1.05',
   '5',
   '19',
   '20'], ans=4,
   why='1/(1 − 0.95) = 1/0.05 = 20, which is why very high MPC economies respond strongly to injections.'),
 dict(q='Which of the following would make the real-world multiplier smaller than the simple formula predicts?', choices=[
   'leakages into imports, taxes, and saving at each round of spending',
   'a higher MPC',
   'a closed economy with no taxes',
   'an increase in consumer confidence',
   'a lower marginal tax rate'], ans=0,
   why="Any income that leaks out of the domestic spending stream cannot become someone else's domestic income in the next round."),
 dict(q='In an open economy with a marginal propensity to import, the spending multiplier is', choices=[
   'exactly 1/MPS',
   'negative',
   'equal to the tax multiplier',
   'larger than 1/MPS',
   'smaller than 1/MPS'], ans=4,
   why='Spending on imports leaks abroad, shortening the chain of induced domestic income.'),
 dict(q='If the MPC is 0.8 and the initial increase in spending is $100 billion, the second round of induced consumption, in billions of dollars, equals', choices=[
   '20',
   '64',
   '80',
   '100',
   '500'], ans=2,
   why='Recipients of the first $100 billion of income spend 0.8 of it, which is $80 billion.'),
 dict(q='The multiplier process implies that a decrease in investment spending will', choices=[
   'affect only the price level',
   'reduce GDP by less than the fall in investment',
   'reduce GDP by a multiple of the fall in investment',
   'leave GDP unchanged',
   'raise GDP'], ans=2,
   why='The multiplier works in both directions, so contractions are also amplified.'),
 dict(q='A transfer payment increase of $100 billion with an MPC of 0.75 raises real GDP by, in billions of dollars,', choices=[
   '75',
   '100',
   '300',
   '400',
   '500'], ans=2,
   why='Transfers work like a tax cut, so the relevant multiplier magnitude is 3 and the change is 300.'),
 dict(q='Which statement about the spending and tax multipliers is correct?', choices=[
   'The spending multiplier always exceeds the tax multiplier in absolute value by exactly one.',
   'The tax multiplier is always positive.',
   'The spending multiplier is negative.',
   'Neither depends on the MPC.',
   'They are equal in magnitude.'], ans=0,
   why='1/MPS − MPC/MPS = 1, so the gap between them is always one.'),
 dict(q='If households become more cautious and save a larger share of each additional dollar, the spending multiplier', choices=[
   'is unchanged',
   'becomes negative',
   'becomes infinite',
   'rises',
   'falls'], ans=4,
   why='A higher MPS means a smaller multiplier, since less income is re-spent each round.'),
 dict(q='The multiplier effect on real GDP is largest when', choices=[
   'imports are very large',
   'taxes are highly progressive',
   'the economy is at full employment and prices adjust fully',
   'the economy has substantial unused capacity, so extra spending raises output rather than prices',
   'the MPC is near zero'], ans=3,
   why='If the economy is already at capacity, additional demand shows up mostly as a higher price level rather than more real output.'),
 dict(q='Which pairing of MPC and spending multiplier is correct?', choices=[
   'MPC 0.6, multiplier 6',
   'MPC 0.6, multiplier 2.5',
   'MPC 0.9, multiplier 9',
   'MPC 0.5, multiplier 5',
   'MPC 0.75, multiplier 3'], ans=1,
   why='With MPC 0.6 the MPS is 0.4, and 1/0.4 = 2.5.'),
 dict(q='Real GDP falls by $250 billion after investment falls by $50 billion. The MPS is', choices=[
   '0.1',
   '0.2',
   '0.25',
   '0.4',
   '0.5'], ans=1,
   why='The multiplier is 250/50 = 5, so MPS = 1/5 = 0.2.'),
 dict(q='An economy with an MPC of 0.5 receives a $200 billion increase in exports. Real GDP rises, in billions of dollars, by', choices=[
   '100',
   '200',
   '400',
   '600',
   '1,000'], ans=2,
   why='The multiplier is 1/0.5 = 2, so the change is 2 × 200 = 400.'),
 dict(q='Suppose the government wants to raise real GDP by $600 billion in an economy with an MPC of 0.75. It could do so with', choices=[
   'a $100 billion spending increase only',
   'no fiscal action at all',
   'a $600 billion tax cut or a $600 billion spending increase',
   'a $150 billion spending increase or a $200 billion tax cut',
   'a $200 billion spending increase or a $150 billion tax cut'], ans=3,
   why='With multipliers of 4 and 3, the required amounts are 600/4 = 150 in spending or 600/3 = 200 in tax cuts.'),
 dict(q='The multiplier concept assumes, among other things, that', choices=[
   'there is no saving',
   'the MPC changes at every round',
   'induced consumption depends on income and unused capacity exists so output can expand',
   'prices rise proportionally with spending',
   'the government finances all spending with taxes'], ans=2,
   why='Induced spending on income and slack in the economy are what let an initial injection multiply into real output.'),
 dict(q='Two economies receive an identical increase in government spending, but one has a higher marginal propensity to import. Compared with the other, that economy will experience', choices=[
   'a larger increase in real GDP',
   'a smaller increase in real GDP because more of each round of spending leaks abroad',
   'an identical increase in real GDP',
   'a fall in real GDP',
   'no change in real GDP'], ans=1,
   why='Import leakage removes income from the domestic spending chain, shrinking the effective multiplier.'),
]
