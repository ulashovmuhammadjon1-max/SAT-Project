# MACRO 4.4 Banking and the Expansion of the Money Supply — 50 questions
# ---------------------------------------------------------------------------
# T-ACCOUNT verified (all figures in dollars). Reserve requirement rr = 10%.
#   Assets:  Required reserves    100
#            Excess reserves      150
#            Loans              1,750
#            Total assets       2,000
#   Liabilities: Demand deposits 1,000
#                Owners' equity  1,000  -- kept so the two sides balance: 2,000 = 2,000
#   Check: required reserves = 0.10 x 1,000 = 100. Correct.
#          total reserves = 100 + 150 = 250. Excess = 250 - 100 = 150. Correct.
#   If rr rises to 25%: required = 0.25 x 1,000 = 250, so excess = 250 - 250 = 0.
#   If rr falls to 5%:  required = 50, so excess = 250 - 50 = 200.
# ---------------------------------------------------------------------------
# MONEY MULTIPLIER m = 1/rr, every value used in this bank derived here:
#   rr = 0.10 -> m = 10      rr = 0.20 -> m = 5       rr = 0.25 -> m = 4
#   rr = 0.05 -> m = 20      rr = 0.50 -> m = 2       rr = 0.02 -> m = 50
#   rr = 0.125 -> m = 8      rr = 1.00 -> m = 1  (100% reserves, no expansion)
# ---------------------------------------------------------------------------
# EXPANSION arithmetic. Two distinct questions, and the distinction is tested:
#   (a) MAXIMUM CHANGE IN THE MONEY SUPPLY from an OPEN MARKET PURCHASE of $1,000
#       (new reserves injected from outside the banking system, all of it excess):
#       1,000 x (1/0.10) = $10,000.
#   (b) A $1,000 CASH DEPOSIT into a checking account by the public. The deposit
#       itself is not new money -- currency (money) simply became a deposit (money).
#       Excess reserves created = 1,000 - 100 = 900.
#       New loans created = 900 x (1/0.10) = 9,000.
#       Total deposits end at 1,000 x 10 = 10,000, but the CHANGE IN THE MONEY
#       SUPPLY is 10,000 - 1,000 of currency withdrawn from circulation = $9,000.
#   Other worked cases:
#     $500 open market purchase, rr = 0.20 -> 500 x 5 = $2,500.
#     $2,000 open market purchase, rr = 0.25 -> 2,000 x 4 = $8,000.
#     $1,000 cash deposit, rr = 0.20 -> excess 800, loans 800 x 5 = $4,000,
#            deposits reach $5,000, money supply change = $4,000.
#     $400 cash deposit, rr = 0.05 -> excess 380, loans 380 x 20 = $7,600.
#     $10,000 open market SALE, rr = 0.10 -> money supply falls by $100,000.
#     $600 in excess reserves, rr = 0.20 -> maximum new loans 600 x 5 = $3,000.
# ---------------------------------------------------------------------------
TOPIC = ("4.4", "Banking and the Expansion of the Money Supply", 4)

TACCT = dict(
    headers=["Assets", "Amount", "Liabilities and net worth", "Amount"],
    rows=[
        ["Required reserves", "$100", "Demand deposits", "$1,000"],
        ["Excess reserves", "$150", "Owners' equity", "$1,000"],
        ["Loans", "$1,750", "", ""],
        ["Total", "$2,000", "Total", "$2,000"],
    ],
)

QUESTIONS = [
 dict(q="Fractional reserve banking means that banks", choices=[
   "hold all deposits as reserves",
   "hold only a fraction of deposits as reserves and lend out the rest",
   "hold no reserves at all",
   "are owned by the government",
   "may not make loans"], ans=1,
   why="Lending out part of deposits is what allows banks to create money."),
 dict(q="A bank's required reserves equal", choices=[
   "total deposits",
   "the reserve requirement multiplied by the bank's demand deposits",
   "total reserves minus loans",
   "the bank's loans",
   "the bank's equity"], ans=1,
   why="The requirement is stated as a percentage of deposits."),
 dict(q="Excess reserves equal", choices=[
   "required reserves plus loans",
   "total reserves minus required reserves",
   "deposits minus loans",
   "total reserves plus deposits",
   "the reserve requirement"], ans=1,
   why="Excess reserves are the portion above the legal minimum, and they are what a bank can lend."),
 dict(q="Using the T-account, the reserve requirement must be", table=TACCT, choices=[
   "5%", "10%", "15%", "20%", "25%"], ans=1,
   why="Required reserves of $100 against $1,000 of demand deposits is 10 percent."),
 dict(q="Using the T-account, the bank's total reserves are", table=TACCT, choices=[
   "$100", "$150", "$250", "$1,000", "$2,000"], ans=2,
   why="Total reserves are required reserves of $100 plus excess reserves of $150."),
 dict(q="Using the T-account, the maximum amount this bank alone can lend out immediately is", table=TACCT, choices=[
   "$100", "$150", "$250", "$1,000", "$1,500"], ans=1,
   why="A single bank can lend only its excess reserves, which are $150."),
 dict(q="Using the T-account, if the reserve requirement is raised to 25 percent, the bank's excess reserves become", table=TACCT, choices=[
   "$0", "$50", "$100", "$150", "$250"], ans=0,
   why="Required reserves rise to $250, exactly equal to total reserves, leaving nothing excess."),
 dict(q="Using the T-account, if the reserve requirement is cut to 5 percent, excess reserves become", table=TACCT, choices=[
   "$50", "$100", "$150", "$200", "$250"], ans=3,
   why="Required reserves fall to $50, so $250 minus $50 leaves $200 excess."),
 dict(q="On a bank's balance sheet, customer deposits are", choices=[
   "an asset because the bank holds the money",
   "a liability because the bank owes the funds to depositors",
   "part of owners' equity",
   "a loan",
   "reserves"], ans=1,
   why="Deposits are claims that customers hold against the bank."),
 dict(q="On a bank's balance sheet, loans made to customers are", choices=[
   "a liability",
   "an asset, since borrowers owe the bank",
   "part of reserves",
   "deposits",
   "equity of the borrower"], ans=1,
   why="A loan is a claim the bank holds on someone else, which makes it an asset."),
 dict(q="The money multiplier is equal to", choices=[
   "the reserve requirement",
   "1 divided by the reserve requirement",
   "1 minus the reserve requirement",
   "the reserve requirement divided by 1",
   "the marginal propensity to consume"], ans=1,
   why="Each round of lending re-deposits a fraction, and the geometric series sums to 1/rr."),
 dict(q="If the reserve requirement is 20 percent, the money multiplier is", choices=[
   "0.2", "2", "4", "5", "20"], ans=3,
   why="1 divided by 0.20 is 5."),
 dict(q="If the reserve requirement is 10 percent, the money multiplier is", choices=[
   "0.1", "1", "5", "10", "100"], ans=3,
   why="1 divided by 0.10 is 10."),
 dict(q="If the reserve requirement is 25 percent, the money multiplier is", choices=[
   "0.25", "2.5", "4", "25", "40"], ans=2,
   why="1 divided by 0.25 is 4."),
 dict(q="If the reserve requirement is 5 percent, the money multiplier is", choices=[
   "0.05", "5", "15", "20", "50"], ans=3,
   why="1 divided by 0.05 is 20."),
 dict(q="If the reserve requirement is 50 percent, the money multiplier is", choices=[
   "0.5", "2", "5", "20", "50"], ans=1,
   why="1 divided by 0.50 is 2, so expansion is very limited."),
 dict(q="Under a 100 percent reserve requirement the money multiplier is", choices=[
   "0", "1", "10", "100", "infinite"], ans=1,
   why="With no lending possible, a dollar of new reserves adds exactly one dollar of deposits."),
 dict(q="A lower reserve requirement makes the money multiplier", choices=[
   "smaller", "larger", "unchanged", "zero", "negative"], ans=1,
   why="Banks may lend a larger share of each deposit, so each round leaks less."),
 dict(q="The central bank buys $1,000 of bonds from a commercial bank when the reserve requirement is 10 percent. The maximum possible increase in the money supply is", choices=[
   "$1,000", "$1,100", "$9,000", "$10,000", "$100,000"], ans=3,
   why="All $1,000 arrives as excess reserves, so the full multiplier of 10 applies."),
 dict(q="The central bank buys $500 of bonds from a commercial bank and the reserve requirement is 20 percent. The maximum increase in the money supply is", choices=[
   "$500", "$1,000", "$2,000", "$2,500", "$10,000"], ans=3,
   why="$500 of new excess reserves times a multiplier of 5."),
 dict(q="An open market purchase of $2,000 with a reserve requirement of 25 percent can expand the money supply by at most", choices=[
   "$500", "$2,000", "$6,000", "$8,000", "$50,000"], ans=3,
   why="$2,000 times a multiplier of 4."),
 dict(q="A household deposits $1,000 of cash into a checking account. The reserve requirement is 10 percent. The maximum amount of new loans the banking system can create is", choices=[
   "$100", "$900", "$1,000", "$9,000", "$10,000"], ans=3,
   why="Only the $900 of excess reserves can be lent, and $900 times the multiplier of 10 is $9,000."),
 dict(q="A household deposits $1,000 of cash into a checking account when the reserve requirement is 10 percent. The maximum increase in the money supply is", choices=[
   "$900", "$1,000", "$9,000", "$10,000", "$11,000"], ans=2,
   why="Deposits can reach $10,000, but $1,000 of currency left circulation, so money rises by $9,000."),
 dict(q="The reason a cash deposit and an open market purchase of the same size have different effects on the money supply is that", choices=[
   "the multiplier differs",
   "the cash deposit is not itself new money, since currency already counted as money, while the open market purchase injects new reserves from outside",
   "banks treat them differently by law",
   "cash deposits are not lent out",
   "open market purchases are not multiplied"], ans=1,
   why="Only the open market purchase adds reserves to the system without removing money from circulation."),
 dict(q="A $1,000 cash deposit with a 20 percent reserve requirement allows the banking system to create new loans of at most", choices=[
   "$200", "$800", "$1,000", "$4,000", "$5,000"], ans=3,
   why="Excess reserves of $800 times a multiplier of 5 is $4,000."),
 dict(q="A $400 cash deposit with a 5 percent reserve requirement supports maximum new loans of", choices=[
   "$380", "$2,000", "$7,600", "$8,000", "$20,000"], ans=2,
   why="Excess reserves of $380 times a multiplier of 20 is $7,600."),
 dict(q="A bank holds $600 in excess reserves and the reserve requirement is 20 percent. The maximum expansion of loans in the banking system as a whole is", choices=[
   "$120", "$600", "$3,000", "$3,600", "$12,000"], ans=2,
   why="$600 of excess reserves times a multiplier of 5."),
 dict(q="An open market SALE of $10,000 in bonds with a 10 percent reserve requirement will, at most,", choices=[
   "increase the money supply by $100,000",
   "decrease the money supply by $100,000",
   "decrease the money supply by $10,000",
   "increase the money supply by $10,000",
   "leave the money supply unchanged"], ans=1,
   why="Selling bonds drains $10,000 of reserves, and the multiplier of 10 works in reverse."),
 dict(q="A single commercial bank can safely lend an amount equal to", choices=[
   "its total deposits",
   "its excess reserves",
   "its excess reserves times the money multiplier",
   "its total reserves",
   "its equity"], ans=1,
   why="Only the banking system as a whole gets the multiplied effect; one bank must expect to lose the loan in clearing."),
 dict(q="The banking system as a whole can expand loans by more than any single bank because", choices=[
   "banks are allowed to break the reserve requirement",
   "money lent by one bank is redeposited at another, creating new reserves and further lending",
   "the central bank prints the difference",
   "banks share reserves",
   "the multiplier applies only to one bank"], ans=1,
   why="Successive rounds of lending and redepositing are what generate the multiplier."),
 dict(q="The actual money multiplier is usually smaller than 1/rr because", choices=[
   "reserve requirements are ignored",
   "some funds leak out as currency holdings and banks may hold excess reserves rather than lend",
   "the central bank forbids full lending",
   "loans are never repaid",
   "the reserve requirement is too high"], ans=1,
   why="Cash leakage and voluntary excess reserves interrupt the chain of redeposits."),
 dict(q="If banks decide to hold large excess reserves during a recession, an open market purchase will", choices=[
   "have a larger effect than the simple multiplier predicts",
   "have a smaller effect than the simple multiplier predicts",
   "have exactly the predicted effect",
   "reduce the money supply",
   "have no effect on reserves"], ans=1,
   why="Reserves that are not lent out never start the deposit expansion process."),
 dict(q="When a bank makes a loan by crediting the borrower's checking account, the money supply", choices=[
   "is unchanged",
   "increases immediately by the amount of the loan",
   "decreases",
   "increases only after the loan is repaid",
   "increases by the reserve requirement"], ans=1,
   why="A new checkable deposit is new M1, which is how banks create money."),
 dict(q="When a borrower repays a bank loan, the money supply", choices=[
   "rises", "falls", "is unchanged", "doubles", "becomes negative"], ans=1,
   why="Repayment extinguishes the deposit that was created when the loan was made."),
 dict(q="Which of the following is a liability of a commercial bank?", choices=[
   "loans to customers",
   "checkable deposits",
   "reserves held at the central bank",
   "government bonds it owns",
   "the bank's building"], ans=1,
   why="Deposits are what the bank owes to others."),
 dict(q="Which of the following is an asset of a commercial bank?", choices=[
   "customer savings accounts",
   "reserves held at the central bank",
   "checkable deposits",
   "money owed to depositors",
   "certificates of deposit it has issued"], ans=1,
   why="Reserves are funds the bank owns and holds."),
 dict(q="A balance sheet must always satisfy", choices=[
   "assets equal liabilities",
   "assets equal liabilities plus owners' equity",
   "loans equal deposits",
   "reserves equal deposits",
   "equity equals reserves"], ans=1,
   why="Owners' equity is the residual that makes the two sides equal."),
 dict(q="Raising the reserve requirement will, other things equal,", choices=[
   "increase excess reserves and expand the money supply",
   "reduce excess reserves and contract the money supply",
   "leave the money supply unchanged",
   "raise the money multiplier",
   "increase bank lending"], ans=1,
   why="More of each deposit must be held idle, and the multiplier shrinks as well."),
 dict(q="Lowering the reserve requirement is", choices=[
   "contractionary because banks hold more reserves",
   "expansionary because it frees excess reserves and raises the money multiplier",
   "neutral",
   "a fiscal policy tool",
   "a way to reduce the money supply"], ans=1,
   why="Banks can lend a larger share of deposits, and each round leaks less."),
 dict(q="If the reserve requirement falls from 20 percent to 10 percent, the money multiplier goes from", choices=[
   "2 to 4", "4 to 8", "5 to 10", "10 to 5", "20 to 10"], ans=2,
   why="1/0.20 is 5 and 1/0.10 is 10."),
 dict(q="A bank with $5,000 of demand deposits and $700 of total reserves faces a 10 percent reserve requirement. Its excess reserves are", choices=[
   "$0", "$200", "$500", "$700", "$1,200"], ans=1,
   why="Required reserves are $500, so $700 minus $500 leaves $200 excess."),
 dict(q="A bank with $8,000 of demand deposits and $1,600 of total reserves faces a 20 percent reserve requirement. This bank", choices=[
   "has $1,600 of excess reserves",
   "is exactly meeting its requirement with no excess reserves",
   "is short of required reserves",
   "can lend $1,600",
   "must raise the reserve requirement"], ans=1,
   why="Required reserves of 0.20 times $8,000 is exactly $1,600."),
 dict(q="A bank that finds itself short of required reserves can", choices=[
   "ignore the shortfall",
   "borrow reserves from other banks or from the central bank's discount window",
   "print money",
   "raise the reserve requirement",
   "convert loans into deposits"], ans=1,
   why="Interbank borrowing and the discount window exist to cover reserve shortfalls."),
 dict(q="The primary economic function of a commercial bank is to", choices=[
   "print currency",
   "act as a financial intermediary, accepting deposits from savers and lending to borrowers",
   "set interest rates for the economy",
   "collect taxes",
   "regulate the money supply"], ans=1,
   why="Intermediation between savers and borrowers is what banks do."),
 dict(q="Deposit insurance reduces the risk of bank runs because", choices=[
   "it forces banks to hold 100 percent reserves",
   "depositors know their funds are protected, so they have no reason to rush to withdraw",
   "it eliminates lending",
   "it raises the reserve requirement",
   "it prevents banks from failing to earn profits"], ans=1,
   why="A run happens when depositors fear losing funds, and insurance removes that fear."),
 dict(q="A bank run is dangerous under fractional reserve banking because", choices=[
   "banks hold all deposits in cash",
   "banks hold only a fraction of deposits as reserves and cannot pay everyone at once",
   "banks have no assets",
   "the central bank forbids withdrawals",
   "loans are worthless"], ans=1,
   why="Most of the deposits are tied up in loans that cannot be called in instantly."),
 dict(q="An increase in the money supply through bank lending requires that", choices=[
   "banks hold their excess reserves idle",
   "banks find creditworthy borrowers willing to take loans",
   "the reserve requirement rise",
   "the central bank sell bonds",
   "the public withdraw currency"], ans=1,
   why="Money is created only when a loan is actually made, so willing borrowers are essential."),
 dict(q="If the public decides to hold more of its money as currency and less as deposits, the money multiplier", choices=[
   "rises", "falls", "is unchanged", "becomes 1/rr exactly", "becomes infinite"], ans=1,
   why="Currency held outside banks cannot be lent, so the expansion chain leaks."),
 dict(q="Suppose the reserve requirement is 12.5 percent. The money multiplier is", choices=[
   "1.25", "4", "8", "12.5", "80"], ans=2,
   why="1 divided by 0.125 is 8."),
 dict(q="A student says an open market purchase of $1,000 with a 10 percent reserve requirement raises the money supply by $100. The error is that the student", choices=[
   "used the wrong reserve requirement",
   "multiplied by the reserve requirement instead of dividing by it",
   "forgot the currency drain",
   "confused assets with liabilities",
   "used the spending multiplier"], ans=1,
   why="The multiplier is 1/rr, so the calculation is $1,000 divided by 0.10, not multiplied."),
]
