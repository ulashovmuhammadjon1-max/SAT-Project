# MACRO 2.3 Unemployment — 50 questions
# Table verified (LAB, all figures in millions of people):
#   Total population                                    250
#   Under 16, institutionalized, or in the military      50
#   -> Adult (16+) noninstitutional population = 250 - 50 = 200
#   Employed                                            120
#   Unemployed (jobless, available, actively searching)  10
#   Not in the labor force                               70
#   Check: 120 + 10 + 70 = 200  OK (equals the adult noninstitutional population)
#   Of the 70 not in the labor force, 5 are discouraged workers.
#
#   Labor force            = 120 + 10 = 130
#   Unemployment rate      = 10 / 130 = 0.076923 = 7.7%
#   Labor force part. rate = 130 / 200 = 0.65 = 65.0%
#   Employment-population ratio = 120 / 200 = 0.60 = 60.0%
#
#   If the 5 discouraged workers were counted as unemployed:
#     labor force = 135, unemployed = 15
#     unemployment rate = 15 / 135 = 0.1111 = 11.1%
#     LFPR = 135 / 200 = 0.675 = 67.5%
#   If instead 5 of the 10 unemployed gave up searching:
#     labor force = 125, unemployed = 5
#     unemployment rate = 5 / 125 = 0.04 = 4.0%  (the measured rate FALLS)
#     LFPR = 125 / 200 = 0.625 = 62.5%
TOPIC = ("2.3", "Unemployment", 2)

LAB = dict(headers=["Category", "Millions of people"],
           rows=[["Total population", "250"],
                 ["Under 16, institutionalized, or in the military", "50"],
                 ["Employed", "120"],
                 ["Unemployed", "10"],
                 ["Not in the labor force", "70"],
                 ["(of which) discouraged workers", "5"]])

QUESTIONS = [
 dict(q="To be counted as unemployed, a person must be", choices=[
   "without a job",
   "without a job, available for work, and actively searching for work",
   "collecting unemployment benefits",
   "working fewer hours than desired",
   "over the age of 18 and not in school"], ans=1,
   why="All three conditions must hold; simply lacking a job is not enough."),
 dict(q="The labor force consists of", choices=[
   "everyone in the country",
   "the employed plus the unemployed",
   "the employed only",
   "everyone over the age of 16",
   "the employed plus everyone not in the labor force"], ans=1,
   why="The labor force counts people who are working or actively seeking work."),
 dict(q="The unemployment rate is calculated as", choices=[
   "unemployed ÷ total population",
   "unemployed ÷ labor force",
   "unemployed ÷ employed",
   "labor force ÷ unemployed",
   "unemployed ÷ adult population"], ans=1,
   why="The denominator is the labor force, not the whole population."),
 dict(q="The labor force participation rate is calculated as", choices=[
   "labor force ÷ total population",
   "labor force ÷ adult noninstitutional population",
   "employed ÷ labor force",
   "employed ÷ total population",
   "unemployed ÷ labor force"], ans=1,
   why="LFPR measures the share of working-age civilians who are in the labor force."),
 dict(q="Which of the following people is counted as unemployed?", choices=[
   "a full-time student not looking for work",
   "an engineer laid off last month who sends out applications every week",
   "a retiree who has stopped looking",
   "a parent caring for children at home by choice",
   "a person working 15 hours a week who wants 40"], ans=1,
   why="The engineer is jobless, available, and actively searching."),
 dict(q="A person working 20 hours a week who wants full-time work is classified as", choices=[
   "unemployed", "employed", "not in the labor force", "a discouraged worker", "structurally unemployed"], ans=1,
   why="Anyone who did any paid work in the survey week counts as employed, which is why underemployment is invisible in the rate."),
 dict(q="A retired 70-year-old who is not looking for work is counted as", choices=[
   "employed", "not in the labor force", "unemployed", "a discouraged worker", "frictionally unemployed"], ans=1,
   why="Without an active job search, a person is outside the labor force entirely."),
 dict(q="A discouraged worker is someone who", choices=[
   "is unhappy in their current job",
   "wants a job but has stopped actively searching because they believe none is available",
   "works part time involuntarily",
   "has just quit a job to find a better one",
   "is retraining for a new occupation"], ans=1,
   why="The defining feature is that the person has given up searching, which removes them from the labor force."),
 dict(q="Because discouraged workers are not counted, the official unemployment rate", choices=[
   "overstates the true extent of joblessness",
   "understates the true extent of joblessness",
   "measures it exactly",
   "is always zero",
   "equals the natural rate"], ans=1,
   why="People who want work but stopped searching disappear from both the numerator and the labor force."),
 dict(q="If a large number of unemployed workers become discouraged and stop searching, the measured unemployment rate will", choices=[
   "rise", "fall", "be unchanged", "become negative", "equal the participation rate"], ans=1,
   why="They leave the numerator and the labor force at once, and removing a person from a small numerator lowers the ratio."),
 dict(q="If discouraged workers become optimistic and resume searching, the measured unemployment rate will initially", choices=[
   "fall", "rise", "stay the same", "become negative", "fall then immediately rise"], ans=1,
   why="They re-enter as unemployed, adding to both the numerator and the labor force, and the numerator effect dominates."),
 dict(q="Frictional unemployment arises from", choices=[
   "a downturn in the business cycle",
   "the time it takes workers and jobs to find each other, including new entrants and voluntary job switchers",
   "a permanent mismatch of skills",
   "technological obsolescence of an entire occupation",
   "a minimum wage above equilibrium"], ans=1,
   why="Search and matching take time even in a healthy economy."),
 dict(q="Structural unemployment arises from", choices=[
   "a temporary fall in aggregate demand",
   "a mismatch between workers' skills or locations and the requirements of available jobs",
   "normal job search by new graduates",
   "seasonal weather patterns",
   "workers voluntarily quitting to look for better pay"], ans=1,
   why="Structural unemployment persists because the jobs and the workers do not fit each other."),
 dict(q="Cyclical unemployment arises from", choices=[
   "job search",
   "a downturn in the business cycle that reduces aggregate demand and therefore the demand for labor",
   "obsolete skills",
   "geographic immobility",
   "seasonal fluctuations"], ans=1,
   why="It is the unemployment that appears in recessions and disappears in expansions."),
 dict(q="A textile worker whose job was permanently eliminated by automation and who lacks the skills for available jobs is", choices=[
   "frictionally unemployed", "structurally unemployed", "cyclically unemployed", "not in the labor force", "seasonally employed"], ans=1,
   why="The job is gone permanently and the worker's skills do not match what employers now want."),
 dict(q="A recent college graduate spending two months interviewing for a first job is", choices=[
   "cyclically unemployed", "frictionally unemployed", "structurally unemployed", "a discouraged worker", "not in the labor force"], ans=1,
   why="Normal search by a new entrant is frictional."),
 dict(q="An auto worker laid off during a recession and expecting recall when demand recovers is", choices=[
   "structurally unemployed", "cyclically unemployed", "frictionally unemployed", "a discouraged worker", "not in the labor force"], ans=1,
   why="The layoff is caused by a temporary fall in aggregate demand."),
 dict(q="The natural rate of unemployment equals", choices=[
   "cyclical unemployment only",
   "frictional plus structural unemployment",
   "frictional plus cyclical unemployment",
   "structural plus cyclical unemployment",
   "total unemployment in a recession"], ans=1,
   why="The natural rate is the unemployment that remains when cyclical unemployment is zero."),
 dict(q="Full employment occurs when", choices=[
   "the unemployment rate is zero",
   "cyclical unemployment is zero and the economy is at its natural rate",
   "every adult has a job",
   "frictional unemployment is zero",
   "the participation rate reaches 100%"], ans=1,
   why="Some frictional and structural unemployment always remains, so full employment is not a zero rate."),
 dict(q="The unemployment rate at full employment is not zero because", choices=[
   "measurement errors are large",
   "frictional and structural unemployment persist even in a healthy economy",
   "people refuse to work",
   "the labor force is too large",
   "cyclical unemployment can never be eliminated"], ans=1,
   why="Search takes time and skill mismatches exist even when aggregate demand is strong."),
 dict(q="If the actual unemployment rate is 7% and the natural rate is 5%, cyclical unemployment equals", choices=[
   "0%", "2%", "5%", "7%", "12%"], ans=1,
   why="Cyclical unemployment is the actual rate minus the natural rate, 7 − 5 = 2 percentage points."),
 dict(q="If the actual unemployment rate is below the natural rate, the economy is most likely", choices=[
   "in a recession",
   "producing beyond full-employment output, with an inflationary gap",
   "at long-run equilibrium",
   "experiencing deflation",
   "at zero cyclical unemployment"], ans=1,
   why="Unemployment below the natural rate signals output above potential."),
 dict(q="Using the table below, the labor force equals", table=LAB, choices=[
   "120 million", "130 million", "190 million", "200 million", "250 million"], ans=1,
   why="Labor force = employed (120) + unemployed (10) = 130 million."),
 dict(q="Using the same table, the unemployment rate is closest to", table=LAB, choices=[
   "4.0%", "5.0%", "7.7%", "8.3%", "11.1%"], ans=2,
   why="10 / 130 = 0.0769, or about 7.7%."),
 dict(q="Using the same table, the labor force participation rate is", table=LAB, choices=[
   "52.0%", "60.0%", "65.0%", "67.5%", "80.0%"], ans=2,
   why="130 million in the labor force out of an adult noninstitutional population of 250 − 50 = 200 million gives 65%."),
 dict(q="Using the same table, the adult noninstitutional population equals", table=LAB, choices=[
   "130 million", "190 million", "200 million", "220 million", "250 million"], ans=2,
   why="250 million total less the 50 million who are under 16, institutionalized, or in the military."),
 dict(q="Using the same table, the employment-population ratio equals", table=LAB, choices=[
   "48.0%", "52.0%", "60.0%", "65.0%", "92.3%"], ans=2,
   why="120 million employed out of the 200 million adult noninstitutional population is 60%."),
 dict(q="Using the same table, if the 5 million discouraged workers were reclassified as unemployed, the unemployment rate would be closest to", table=LAB, choices=[
   "7.7%", "8.5%", "11.1%", "12.5%", "15.0%"], ans=2,
   why="15 million unemployed in a labor force of 135 million gives 11.1%."),
 dict(q="Using the same table, if 5 million of the unemployed gave up searching, the measured unemployment rate would become", table=LAB, choices=[
   "4.0%", "5.0%", "7.7%", "8.3%", "10.0%"], ans=0,
   why="5 million unemployed in a labor force that has shrunk to 125 million gives 4%, a striking illustration of how discouragement flatters the statistic."),
 dict(q="Using the same table, if 5 million of the unemployed gave up searching, the labor force participation rate would become", table=LAB, choices=[
   "60.0%", "62.5%", "65.0%", "67.5%", "70.0%"], ans=1,
   why="The labor force falls to 125 million out of 200 million adults."),
 dict(q="Seasonal unemployment, such as a ski instructor out of work in July, is usually treated as a form of", choices=[
   "cyclical unemployment", "frictional unemployment", "structural unemployment", "discouragement", "underemployment"], ans=1,
   why="It is short-term and predictable, part of the ordinary churn of the labor market, and official series are seasonally adjusted for it."),
 dict(q="Which policy would most directly reduce structural unemployment?", choices=[
   "an increase in government spending during a recession",
   "job retraining programs and relocation assistance",
   "a cut in interest rates",
   "an increase in unemployment benefits",
   "a tax rebate to households"], ans=1,
   why="Structural unemployment is a mismatch problem, so retraining and mobility address its cause."),
 dict(q="Which policy would most directly reduce cyclical unemployment?", choices=[
   "job-matching websites",
   "expansionary fiscal or monetary policy that raises aggregate demand",
   "vocational retraining",
   "reducing the minimum wage",
   "relocation subsidies"], ans=1,
   why="Cyclical unemployment comes from deficient aggregate demand, so demand-side policy is the remedy."),
 dict(q="Improved online job-matching services would be expected to reduce", choices=[
   "cyclical unemployment", "frictional unemployment", "structural unemployment", "the participation rate", "the natural rate to zero"], ans=1,
   why="Faster matching shortens search spells."),
 dict(q="Generous and long-lasting unemployment benefits tend to", choices=[
   "reduce the natural rate of unemployment",
   "raise the natural rate somewhat by lengthening job search",
   "eliminate cyclical unemployment",
   "reduce the participation rate to zero",
   "have no effect on unemployment"], ans=1,
   why="Longer benefit duration reduces the urgency of accepting the first available offer, which raises measured frictional unemployment."),
 dict(q="A minimum wage set above the market-clearing wage contributes to", choices=[
   "frictional unemployment", "structural unemployment", "cyclical unemployment", "discouraged workers only", "a lower natural rate"], ans=1,
   why="A binding wage floor creates a persistent surplus of low-skill labor, which is structural."),
 dict(q="The natural rate of unemployment can change over time because of", choices=[
   "changes in aggregate demand",
   "changes in labor market institutions, demographics, and technology",
   "changes in the price level alone",
   "monetary policy",
   "the business cycle"], ans=1,
   why="The natural rate reflects the structure of the labor market rather than the state of demand."),
 dict(q="An economy in a deep recession would be expected to show", choices=[
   "unemployment below the natural rate",
   "unemployment above the natural rate and positive cyclical unemployment",
   "zero frictional unemployment",
   "a rising participation rate",
   "no structural unemployment"], ans=1,
   why="A recession adds cyclical unemployment on top of the natural rate."),
 dict(q="A rise in the labor force participation rate of women over several decades, holding employment growth constant, would tend to", choices=[
   "lower measured unemployment immediately",
   "raise the labor force and, in the short run, raise the measured unemployment rate as new entrants search",
   "have no effect on the labor force",
   "lower the adult population",
   "eliminate frictional unemployment"], ans=1,
   why="New entrants join the labor force as searchers before they are matched to jobs."),
 dict(q="The unemployment rate can rise even as the number of employed people rises if", choices=[
   "the population falls",
   "the labor force grows faster than employment",
   "employment grows faster than the labor force",
   "discouraged workers leave the labor force",
   "the participation rate falls"], ans=1,
   why="Both the numerator and denominator can grow, and the rate rises when the labor force outpaces jobs created."),
 dict(q="Which of the following is counted as employed by the official survey?", choices=[
   "an unpaid volunteer at a hospital",
   "a person who worked five paid hours last week as a dog walker",
   "a person actively applying for jobs",
   "a discouraged worker",
   "a full-time student not working"], ans=1,
   why="Any paid work during the survey week, however brief, counts as employment."),
 dict(q="Underemployment refers to", choices=[
   "being unemployed for over a year",
   "working part time or below one's skill level when full-time or better-matched work is desired",
   "not being in the labor force",
   "being discouraged",
   "being employed at the minimum wage"], ans=1,
   why="The person is working, so they count as employed, and the rate does not register the shortfall."),
 dict(q="A country reports an unemployment rate of 4% and a labor force participation rate that has fallen sharply. The most likely interpretation is that", choices=[
   "the labor market is unusually strong",
   "the low rate partly reflects people leaving the labor force rather than finding jobs",
   "employment must have risen",
   "the natural rate has fallen to zero",
   "cyclical unemployment is negative"], ans=1,
   why="A falling participation rate shrinks the labor force, which can pull the unemployment rate down without any gain in employment."),
 dict(q="If the labor force is 160 million and 8 million are unemployed, the unemployment rate is", choices=[
   "4.0%", "5.0%", "8.0%", "16.0%", "20.0%"], ans=1,
   why="8 / 160 = 0.05."),
 dict(q="If the adult noninstitutional population is 250 million and the labor force is 160 million, the participation rate is", choices=[
   "36.0%", "56.0%", "64.0%", "76.0%", "84.0%"], ans=2,
   why="160 / 250 = 0.64."),
 dict(q="If an economy has 95 million employed and an unemployment rate of 5%, the number unemployed is closest to", choices=[
   "4.75 million", "5.0 million", "5.26 million", "9.5 million", "19.0 million"], ans=1,
   why="If U is unemployed, U / (95 + U) = 0.05, so U = 4.75 + 0.05U, giving U = 5.0 million and a labor force of 100 million."),
 dict(q="Which combination best describes an economy at full employment?", choices=[
   "zero unemployment and zero inflation",
   "positive frictional and structural unemployment, and zero cyclical unemployment",
   "positive cyclical unemployment and zero structural unemployment",
   "zero frictional unemployment and positive cyclical unemployment",
   "an unemployment rate of exactly zero"], ans=1,
   why="Full employment means the cyclical component has been eliminated, not that everyone has a job."),
 dict(q="A worker who quits a job in one city and moves to another before taking a new position is best classified as", choices=[
   "structurally unemployed", "frictionally unemployed", "cyclically unemployed", "not in the labor force", "employed"], ans=1,
   why="Voluntary job-to-job transitions are part of normal search."),
 dict(q="Two economies have the same unemployment rate, but one has a much higher share of long-term unemployment. This suggests that in that economy", choices=[
   "unemployment is mostly frictional",
   "unemployment is more likely structural, since spells are lasting a long time",
   "the labor force is smaller",
   "there is no cyclical unemployment",
   "the participation rate is higher"], ans=1,
   why="Long spells point to workers who cannot be matched to available jobs rather than to ordinary search."),
 dict(q="Which would raise the measured unemployment rate without any change in the number of people who want work?", choices=[
   "an increase in discouragement",
   "a policy requiring benefit recipients to document an active job search, which reclassifies non-searchers as unemployed",
   "an increase in retirements",
   "a fall in the adult population",
   "an increase in part-time work"], ans=1,
   why="People who wanted work all along move from outside the labor force into the unemployed count."),
]
