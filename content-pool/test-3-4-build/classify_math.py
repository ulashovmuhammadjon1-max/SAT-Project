import json

# key = (source, module, num) -> skill code
CLASSIFY = {
    # ===== MayIntA MATH_M1 =====
    ("MayIntA","MATH_M1",1):"ALG-LE",       # 13x=42-x
    ("MayIntA","MATH_M1",2):"ALG-LI",       # min/max inequality range
    ("MayIntA","MATH_M1",3):"ALG-LE",       # savings word problem linear
    ("MayIntA","MATH_M1",4):"ADV-NF",       # y-intercept of quadratic
    ("MayIntA","MATH_M1",5):"PSDA-DI",      # graph reading population
    ("MayIntA","MATH_M1",6):"ALG-LF",       # f(x)=5x+b linear function b
    ("MayIntA","MATH_M1",7):"ADV-NF",       # h(x)=5|x| function eval
    ("MayIntA","MATH_M1",8):"PSDA-ST",      # frequency table min value (stats)
    ("MayIntA","MATH_M1",9):"PSDA-ST",      # mean of data set
    ("MayIntA","MATH_M1",10):"ADV-NE",      # system linear+quadratic
    ("MayIntA","MATH_M1",11):"ALG-LF",      # linear model predicted value
    ("MayIntA","MATH_M1",12):"ADV-NF",      # exponential growth model identify
    ("MayIntA","MATH_M1",13):"ALG-LE",      # system of linear equations
    ("MayIntA","MATH_M1",14):"ALG-LF",      # perpendicular line slope
    ("MayIntA","MATH_M1",15):"ADV-NE",      # quadratic word problem (product)
    ("MayIntA","MATH_M1",16):"ALG-LE",      # shirts coupon linear (KEEP - dup of JuneV2 M1 17 dropped)
    ("MayIntA","MATH_M1",17):"ADV-NE",      # abs value equation solutions
    ("MayIntA","MATH_M1",19):"GT-AV",       # cube/sphere volume
    ("MayIntA","MATH_M1",20):"ADV-NF",      # exponential function ab
    ("MayIntA","MATH_M1",21):"ADV-NF",      # exponential growth rate rewrite
    ("MayIntA","MATH_M1",22):"ADV-NE",      # sqrt equation solve for a

    # ===== MayIntA MATH_M2 =====
    ("MayIntA","MATH_M2",1):"ALG-LE",
    ("MayIntA","MATH_M2",2):"PSDA-DI",      # graph reading star cluster (approx, kept)
    ("MayIntA","MATH_M2",4):"ADV-NF",       # exponential table
    ("MayIntA","MATH_M2",5):"ADV-NE",       # x^2=2601 solutions count
    ("MayIntA","MATH_M2",6):"ADV-NF",       # population exponential model
    ("MayIntA","MATH_M2",7):"PSDA-ST",      # age distribution table stats
    ("MayIntA","MATH_M2",8):"PSDA-RP",      # ratio length:width
    ("MayIntA","MATH_M2",9):"ADV-EQ",       # equivalent expression expand
    ("MayIntA","MATH_M2",10):"GT-AV",       # similar rectangles area/volume-ish (scale)
    ("MayIntA","MATH_M2",11):"PSDA-ST",     # data sets comparison range
    ("MayIntA","MATH_M2",12):"PSDA-DI",     # graph reading mass composition
    ("MayIntA","MATH_M2",13):"ADV-NF",      # cubic function x-intercepts
    ("MayIntA","MATH_M2",14):"ADV-NF",      # pressure model interpretation
    ("MayIntA","MATH_M2",15):"GT-AV",       # circle circumference/diameter
    ("MayIntA","MATH_M2",16):"GT-TR",       # right triangle trig side
    ("MayIntA","MATH_M2",17):"GT-TR",       # right triangle sin/cos relationship
    ("MayIntA","MATH_M2",18):"PSDA-RP",     # buffalo composition ratio
    ("MayIntA","MATH_M2",19):"ADV-EQ",      # factor identification
    ("MayIntA","MATH_M2",20):"ALG-LE",      # system rewrite (31(x-n)=31y+31n)
    ("MayIntA","MATH_M2",21):"ALG-LF",      # cost equation rewrite
    ("MayIntA","MATH_M2",22):"GT-LA",       # similar triangles side/angle

    # ===== MarchIntB_T1 MATH_M1 =====
    ("MarchIntB_T1","MATH_M1",1):"PSDA-DI", # scatterplot line of best fit
    ("MarchIntB_T1","MATH_M1",2):"ALG-LE",  # system solve
    ("MarchIntB_T1","MATH_M1",3):"ALG-LE",  # 8x+56=36x
    ("MarchIntB_T1","MATH_M1",4):"ALG-LE",  # 4(x+3)=3(x+3)+56
    ("MarchIntB_T1","MATH_M1",5):"ALG-LF",  # f(x)=7/10x+63 eval
    ("MarchIntB_T1","MATH_M1",6):"ADV-NF",  # f(x)=2+sqrt(x) eval
    ("MarchIntB_T1","MATH_M1",7):"GT-LA",   # congruent triangles
    ("MarchIntB_T1","MATH_M1",8):"PSDA-RP", # visitor room percentages
    ("MarchIntB_T1","MATH_M1",9):"ALG-LF",  # gasoline linear model
    ("MarchIntB_T1","MATH_M1",10):"GT-AV",  # circle center from equation
    ("MarchIntB_T1","MATH_M1",11):"ADV-NF", # exponential decay model
    ("MarchIntB_T1","MATH_M1",12):"ALG-LF", # parallel line slope
    ("MarchIntB_T1","MATH_M1",13):"ALG-LE", # bus rental cost linear
    ("MarchIntB_T1","MATH_M1",14):"ADV-NF", # quadratic model projects
    ("MarchIntB_T1","MATH_M1",15):"ALG-LE", # mulch/rock linear cost eq
    ("MarchIntB_T1","MATH_M1",16):"GT-AV",  # hemisphere volume
    ("MarchIntB_T1","MATH_M1",17):"ADV-NF", # projectile quadratic
    ("MarchIntB_T1","MATH_M1",18):"GT-TR",  # right triangle cos
    ("MarchIntB_T1","MATH_M1",19):"PSDA-DI",# pheasant population estimate
    ("MarchIntB_T1","MATH_M1",20):"PSDA-ST",# leaf water potential samples stats
    ("MarchIntB_T1","MATH_M1",21):"ALG-LF", # table linear equation
    ("MarchIntB_T1","MATH_M1",22):"ALG-LE", # system no solution

    # ===== MarchIntB_T1 MATH_M2 =====
    ("MarchIntB_T1","MATH_M2",1):"ADV-EQ",
    ("MarchIntB_T1","MATH_M2",2):"ADV-NE",  # system linear+quadratic graph
    ("MarchIntB_T1","MATH_M2",3):"GT-LA",   # triangle angle sum
    ("MarchIntB_T1","MATH_M2",4):"ALG-LF",  # table linear relationship
    ("MarchIntB_T1","MATH_M2",5):"ALG-LF",  # y-intercept linear shift
    ("MarchIntB_T1","MATH_M2",6):"ADV-NF",  # exponential pressure model
    ("MarchIntB_T1","MATH_M2",7):"ADV-NE",  # abs value equation sum
    ("MarchIntB_T1","MATH_M2",8):"ADV-NF",  # exponential y-intercept
    ("MarchIntB_T1","MATH_M2",9):"ADV-NE",  # quadratic discriminant form
    ("MarchIntB_T1","MATH_M2",10):"PSDA-ST",# dot plot mean/median
    ("MarchIntB_T1","MATH_M2",11):"ALG-LF", # g(x)=9x solve
    ("MarchIntB_T1","MATH_M2",12):"ALG-LI", # consecutive integers inequality
    ("MarchIntB_T1","MATH_M2",13):"ALG-LE", # fractional equation equivalence
    ("MarchIntB_T1","MATH_M2",14):"ADV-NF", # quadratic vertex form
    ("MarchIntB_T1","MATH_M2",15):"ALG-LF", # line graph reading (approx placeholder)
    ("MarchIntB_T1","MATH_M2",16):"GT-LA",  # similar triangles area ratio
    ("MarchIntB_T1","MATH_M2",17):"PSDA-RP",# percent removed word problem
    ("MarchIntB_T1","MATH_M2",18):"PSDA-ST",# median of data set
    ("MarchIntB_T1","MATH_M2",19):"ADV-NE", # system discriminant condition
    ("MarchIntB_T1","MATH_M2",20):"GT-LA",  # isosceles right triangle
    ("MarchIntB_T1","MATH_M2",22):"PSDA-RP",# unit conversion acceleration

    # ===== JuneV2 MATH_M1 =====
    ("JuneV2","MATH_M1",2):"ALG-LI",
    ("JuneV2","MATH_M1",3):"ALG-LE",
    ("JuneV2","MATH_M1",4):"ADV-EQ",
    ("JuneV2","MATH_M1",5):"ADV-NF",        # f(x)=x^3+14 eval
    ("JuneV2","MATH_M1",6):"ALG-LF",        # g(x)=x/2 solve
    ("JuneV2","MATH_M1",7):"PSDA-DI",       # scatterplot linear model
    ("JuneV2","MATH_M1",8):"ADV-NF",        # vertex interpretation
    ("JuneV2","MATH_M1",9):"ALG-LF",        # table linear equation match
    ("JuneV2","MATH_M1",10):"PSDA-RP",      # mixture volume
    ("JuneV2","MATH_M1",11):"ALG-LE",       # system solve
    ("JuneV2","MATH_M1",12):"ADV-NF",       # loyalty program exponential
    ("JuneV2","MATH_M1",13):"ADV-NF",       # bacteria doubling time
    ("JuneV2","MATH_M1",14):"ALG-LF",       # infinitely many solutions slope
    ("JuneV2","MATH_M1",15):"ADV-EQ",       # quadratic manipulate
    ("JuneV2","MATH_M1",17):None,           # DROP: duplicate of MayIntA M1 16
    ("JuneV2","MATH_M1",19):"GT-TR",
    ("JuneV2","MATH_M1",21):"ADV-NF",       # min value of quadratic
    ("JuneV2","MATH_M1",22):"GT-TR",        # unit circle angle radians

    # ===== JuneV2 MATH_M2 =====
    ("JuneV2","MATH_M2",1):"ALG-LF",
    ("JuneV2","MATH_M2",2):"PSDA-ST",       # median comparison
    ("JuneV2","MATH_M2",3):"PSDA-ST",       # margin of error
    ("JuneV2","MATH_M2",4):"ALG-LI",        # graph inequality region (approx)
    ("JuneV2","MATH_M2",5):"ADV-NF",        # quadratic from table
    ("JuneV2","MATH_M2",6):"ADV-NF",        # exponential population graph (approx)
    ("JuneV2","MATH_M2",7):"ALG-LF",        # temperature linear rate
    ("JuneV2","MATH_M2",8):"GT-TR",         # 30-60-90 triangle
    ("JuneV2","MATH_M2",9):"PSDA-RP",       # proportional relationship
    ("JuneV2","MATH_M2",10):"GT-AV",        # cube volume/surface area
    ("JuneV2","MATH_M2",11):"ALG-LE",       # no solution linear equation
    ("JuneV2","MATH_M2",12):"ALG-LF",       # x-intercept interpretation
    ("JuneV2","MATH_M2",13):"ALG-LE",       # rearrange equation
    ("JuneV2","MATH_M2",14):None,           # DROP: duplicate of DecIntB M2 13
    ("JuneV2","MATH_M2",15):"ADV-NF",       # f(x)=4x^2 eval
    ("JuneV2","MATH_M2",16):"ADV-EQ",       # exponent rewrite
    ("JuneV2","MATH_M2",17):"ADV-NE",       # abs value one solution
    ("JuneV2","MATH_M2",18):"ADV-NE",       # no real solution largest b
    ("JuneV2","MATH_M2",19):"ADV-EQ",       # equivalent function forms
    ("JuneV2","MATH_M2",20):None,           # DROP: duplicate of DecIntB M2 21
    ("JuneV2","MATH_M2",21):"PSDA-RP",      # percent mass ratio
    ("JuneV2","MATH_M2",22):"GT-LA",        # similar triangle SAS sufficiency

    # ===== DecIntB MATH_M1 =====
    ("DecIntB","MATH_M1",1):"PSDA-ST",      # probability defect
    ("DecIntB","MATH_M1",2):"PSDA-RP",      # population density
    ("DecIntB","MATH_M1",3):"ALG-LI",       # savings goal inequality
    ("DecIntB","MATH_M1",4):"ADV-NF",       # quadratic f(0)
    ("DecIntB","MATH_M1",5):"ALG-LF",       # table linear
    ("DecIntB","MATH_M1",6):"GT-LA",        # equilateral triangle
    ("DecIntB","MATH_M1",7):"ALG-LE",       # no solution / infinite check
    ("DecIntB","MATH_M1",8):"PSDA-DI",      # scatterplot slope
    ("DecIntB","MATH_M1",9):"ALG-LE",       # system intersection
    ("DecIntB","MATH_M1",10):"ALG-LE",      # tiles linear equation
    ("DecIntB","MATH_M1",11):"ADV-NE",      # no real solution quadratic
    ("DecIntB","MATH_M1",12):"ALG-LF",      # line equation from slope/point
    ("DecIntB","MATH_M1",13):"ADV-NF",      # isotope decay interpretation
    ("DecIntB","MATH_M1",14):"ALG-LE",      # rearrange for m
    ("DecIntB","MATH_M1",15):"ADV-NF",      # projectile vertex form
    ("DecIntB","MATH_M1",16):"ALG-LE",      # system solve x
    ("DecIntB","MATH_M1",17):"GT-AV",       # circle point on circle
    ("DecIntB","MATH_M1",18):"ALG-LF",      # linear graph shift (approx)
    ("DecIntB","MATH_M1",19):"GT-AV",       # square prism volume
    ("DecIntB","MATH_M1",20):"GT-TR",       # right triangle sin/cos
    ("DecIntB","MATH_M1",21):"ADV-NF",      # exponential shift g(x)=f(x-2)
    ("DecIntB","MATH_M1",22):"ADV-EQ",      # factoring AM-GM max ac

    # ===== DecIntB MATH_M2 =====
    ("DecIntB","MATH_M2",1):"ALG-LF",
    ("DecIntB","MATH_M2",2):"ADV-EQ",       # 90y+80y equivalent
    ("DecIntB","MATH_M2",3):"PSDA-ST",      # mean of task times
    ("DecIntB","MATH_M2",4):"ALG-LE",       # 6(x+1)=36
    ("DecIntB","MATH_M2",5):"ADV-NF",       # polynomial x-intercepts
    ("DecIntB","MATH_M2",6):"ALG-LI",       # inequality tables
    ("DecIntB","MATH_M2",7):"ALG-LF",       # linear function slope+point
    ("DecIntB","MATH_M2",8):"PSDA-DI",      # population linear model estimate
    ("DecIntB","MATH_M2",9):"ALG-LF",       # increasing linear description
    ("DecIntB","MATH_M2",10):"ALG-LE",      # system solve combo
    ("DecIntB","MATH_M2",11):"ALG-LE",      # rational equation solve
    ("DecIntB","MATH_M2",12):"PSDA-RP",     # percent mass phosphorus
    ("DecIntB","MATH_M2",13):"PSDA-RP",     # ballot ratio word problem (KEEP)
    ("DecIntB","MATH_M2",14):"ADV-NE",      # no real solutions least n
    ("DecIntB","MATH_M2",15):"ADV-NF",      # exponential intercepts b
    ("DecIntB","MATH_M2",16):"GT-AV",       # triangle area algebra
    ("DecIntB","MATH_M2",17):"ADV-NE",      # tangent system x value
    ("DecIntB","MATH_M2",18):"ADV-EQ",      # factoring product of roots
    ("DecIntB","MATH_M2",19):"ALG-LI",      # temperature range inequality
    ("DecIntB","MATH_M2",20):"GT-AV",       # similar rectangles area/perimeter
    ("DecIntB","MATH_M2",21):"ALG-LE",      # rental cost equation (KEEP)
    ("DecIntB","MATH_M2",22):None,          # DROP: unresolved figure (parallel lines)
}

if __name__ == "__main__":
    print(len(CLASSIFY), "entries;", sum(1 for v in CLASSIFY.values() if v), "classified,", sum(1 for v in CLASSIFY.values() if v is None), "dropped")
