# Solutions to the 36 problems in `t2.ipynb`

Numbering follows the original notebook output, which preserves the first-occurrence order of the distinct problem statements. These are mathematical solutions, not predictions of model robustness.

| Problem | Answer | Problem | Answer |
|---:|---:|---:|---:|
| 1 | 50 | 19 | 714 |
| 2 | 201 | 20 | 1280 |
| 3 | 190 | 21 | 98 |
| 4 | 50 | 22 | 588 |
| 5 | 50 | 23 | 245 |
| 6 | 504 | 24 | 143 |
| 7 | 70 | 25 | 32951 |
| 8 | 77 | 26 | 81 |
| 9 | 902 | 27 | 223 |
| 10 | 850 | 28 | 580 |
| 11 | 669 | 29 | 32193 |
| 12 | 768 | 30 | 751 |
| 13 | 26244 | 31 | 16 |
| 14 | 821 | 32 | 145040 |
| 15 | 178 | 33 | 821 |
| 16 | 70 | 34 | 81 |
| 17 | 441 | 35 | 2193 |
| 18 | 277 | 36 | 42 |


## Problem 1

**Answer: 50**

Write Alice's age and sweets as $a,s$, and Bob's as $b,t$. The original statements give
\[
a+s=2(b+t),\qquad as=4bt.
\]
After the transfer, $a+s-5=b+t+5$, so $b+t=10$ and $a+s=20$. Therefore the unordered pair $\{a,s\}$ equals $\{2b,2t\}$: both pairs have sum $20$ and product $4bt$.

Equality of the products after the transfer gives
\[
a(15-a)=b(15-b),\qquad (a-b)(15-a-b)=0.
\]
If $a=b$, the original product equation forces $a=20/3$, which is not an integer. Thus $a+b=15$. Using either $a=2b$ or $a=2t=20-2b$ gives $a=10$, $b=5$. Both initially hold respectively $10$ and $5$ sweets, and the transfer works. The age product is $\boxed{50}$.

## Problem 2

**Answer: 201**

Checking residues modulo $5$ shows that $5\mid n^2+(n+1)^2$ exactly when $n\equiv1,3\pmod5$.

The Fibonacci identity $F_{n-1}^2+F_n^2=F_{2n-1}$ applies. Also $F_{j+5}\equiv3F_j\pmod5$, and the first five residues are $0,1,1,2,3$, so $5\mid F_j$ exactly when $5\mid j$. The excluded condition therefore holds exactly when $n\equiv3\pmod5$.

We must count $n\equiv1\pmod5$ with $1\le n<10^{101}$. There are
\[
N=\frac{10^{101}}5=2^{101}5^{100}.
\]
The number of prime factors with multiplicity is $101+100=\boxed{201}$.

## Problem 3

**Answer: 190**

Let $r$ and $b$ be the red and blue counts. Cancelling the two hypergeometric probabilities gives
\[
\frac{\binom r5\binom b2}{\binom r4\binom b3}
=\frac{r-4}{5}\frac3{b-2}=1,
\qquad 3r-5b=2.
\]
Thus $b\equiv2\pmod3$. The smallest permitted $b$ is $8$, giving $r=14$ and $n=22$. Increasing $b$ by $3$ increases $r$ by $5$, so the five smallest totals are $22,30,38,46,54$. Their sum is $\boxed{190}$.

## Problem 4

**Answer: 50**

The distance from the circumcenter to the chord $AB$ is
\[
\sqrt{26^2-10^2}=24.
\]
The greatest distance from the line $AB$ to a point on the circumcircle is consequently $24+26=\boxed{50}$. It is attained at the circle's farthest point on the perpendicular bisector of $AB$, which produces a nondegenerate triangle.

## Problem 5

**Answer: 50**

Put $t=x-4$, so the parabola is $y=t^2/2-2$. At a tangency point, the radius from $(4,39)$ must be perpendicular to the tangent direction $(1,t)$. Thus
\[
(t,t^2/2-41)\cdot(1,t)=t(t^2/2-40)=0.
\]
For $t=0$, the radius is $41$. For $t^2=80$, the vertical displacement is $-1$, so the radius is $\sqrt{80+1}=9$. These are the two distinct admissible radii, and their sum is $\boxed{50}$.

## Problem 6

**Answer: 504**

The trapezoid's height is the circle's diameter, $6$. Its area gives $r+s=24$. In a quadrilateral with an incircle, the sums of opposite sides agree; hence the two equal legs each have length $12$.

The horizontal projection of each leg is $|r-s|/2$, so
\[
\left(\frac{r-s}{2}\right)^2=12^2-6^2=108.
\]
Therefore
\[
r^2+s^2=\frac{(r+s)^2+(r-s)^2}{2}
=\frac{576+432}{2}=\boxed{504}.
\]

## Problem 7

**Answer: 70**

The two numbers are $b+7$ and $9b+7$. Since
\[
9b+7=9(b+7)-56,
\]
the divisibility condition is $b+7\mid56$. With $b>9$, the only possible divisors are $28$ and $56$, giving bases $21$ and $49$. Their sum is $\boxed{70}$.

## Problem 8

**Answer: 77**

Write $z=x+iy$. Squaring the second equation gives the perpendicular bisector
\[
8x-6y=8k+7.
\]
The first equation describes the circle centered at $(25,20)$ with radius $5$. There is exactly one intersection precisely when the line is tangent, so
\[
\frac{|8(25)-6(20)-8k-7|}{10}=5,
\qquad |73-8k|=50.
\]
Thus $k=23/8$ or $123/8$. Their sum is $73/4$, and $m+n=\boxed{77}$.

## Problem 9

**Answer: 902**

The remaining sum is an integer. Since $3000/37$ is reduced, $37\mid n-10$.

The minimum and maximum possible means after erasing ten numbers are $(n-9)/2$ and $(n+11)/2$. Therefore
\[
152\le n\le171.
\]
The only integer in this interval congruent to $10\pmod{37}$ is $n=158$. Hence
\[
S=\frac{158\cdot159}{2}-\frac{3000}{37}(158-10)=561.
\]
This erasure sum is attainable, for example by erasing $51,52,\ldots,59,66$. Finally $158\cdot561\equiv\boxed{902}\pmod{997}$.

## Problem 10

**Answer: 850**

The angle-bisector theorem gives $BD:CD=200:225=8:9$. Since both lengths are integers, write $BD=8t$, $CD=9t$ for a positive integer $t$.

By the tangent-secant power theorem at $B$ and $C$,
\[
AE=200-\frac{(8t)^2}{200}=200-\frac{8t^2}{25},\qquad
AF=225-\frac{(9t)^2}{225}=225-\frac{9t^2}{25}.
\]
Their integrality forces $5\mid t$. The triangle inequality gives $25<17t<425$, so $2\le t\le24$. The possibilities are $t=5,10,15,20$; both intersections lie strictly inside the requested segments for each of these.

The corresponding $BC$ lengths are $85,170,255,340$, summing to $\boxed{850}$.

## Problem 11

**Answer: 669**

Expand each summand as a geometric series:
\[
S=\sum_{k\ge1}\frac{10^{-k}}{1-10^{-k}}
=\sum_{j\ge1}d(j)10^{-j},
\]
where $d(j)$ is the number of positive divisors of $j$. Consequently
\[
10^{100}S=\sum_{j=1}^{100}d(j)10^{100-j}+T.
\]
The tail $T$ lies between $0$ and $1$: its first two terms are $2/10+8/100$, and the remaining terms are bounded by $\sum_{j\ge103}j10^{100-j}<0.115$.

Thus the floor is exactly the displayed integer sum. Modulo $1000$, only $j=98,99,100$ matter. Their divisor counts are $6,6,9$, so the remainder is $600+60+9=\boxed{669}$.

## Problem 12

**Answer: 768**

For fixed $j$, the floor in the definition is $1$ precisely for $i\le n/j$, and is otherwise $0$. Therefore
\[
f(n)=\sum_{j=1}^n j^{3272}\left\lfloor\frac nj\right\rfloor,
\qquad f(n)-f(n-1)=\sum_{d\mid n}d^{3272}.
\]
For $n=M^7$, the difference factors as
\[
N=\prod_{q\in\{2,3,5,7,11,13\}}(1+q^{3272}+\cdots+q^{7\cdot3272}).
\]
The $q=2$ factor is odd. For each odd $q$, let $u=q^{3272}$. The lifting-the-exponent formula gives
\[
v_2\left(\frac{u^8-1}{u-1}\right)=v_2(u+1)+v_2(8)-1=3,
\]
since $u\equiv1\pmod8$. There are five odd primes, so $k=15$. Hence $2^{15}\bmod8000=\boxed{768}$.

## Problem 13

**Answer: 26244**

Factor $17017=7\cdot11\cdot13\cdot17$. Every divisor of its seventeenth power is $7^a11^b13^c17^d$, with all four exponents between $0$ and $17$.

Modulo $12$, the four primes are respectively $7,11,1,5$. Each of $7,11,5$ has order $2$, and $7\cdot11\equiv5$. The product is $5$ exactly for parity triples
\[
(a,b,d)\equiv(1,1,0)\quad\text{or}\quad(0,0,1)\pmod2.
\]
Each parity has nine exponent choices, while $c$ has eighteen choices. Thus $N=2\cdot9^3\cdot18=\boxed{26244}$.

## Problem 14

**Answer: 821**

Set $g(t)=f(t-1)$ for $t\ge2$. The equation becomes $g(xy)=g(x)+g(y)$ for $x,y\ge2$. All such positive-integer-valued functions are specified by positive integer prime weights $w_p=g(p)$, with
\[
g(t)=\sum_p v_p(t)w_p.
\]
The bound is $g(t)\le617$ for $2\le t\le618$. Since $343=7^3$ and $503$ are in this interval,
\[
1\le w_7\le205,\qquad1\le w_{503}\le617.
\]
Every pair in this rectangle is feasible: assign all other prime weights $1$. A number containing $503$ must be $503$ itself. A number with three factors of $7$ must be $343$. With two or one factors of $7$, its value is at most $2(205)+3=413$ or $205+6=211$, respectively; with neither exceptional prime its value is at most $9$.

Since $3521=7\cdot503$, we have $f(3520)=w_7+w_{503}$. Every integer from $2$ through $822$ is possible, giving $\boxed{821}$ different values.

## Problem 15

**Answer: 178**

Write the sequence as $4,4+d,4+2d,\ldots$, where $d$ is an integer. To contain the larger terms $24$ and $34$, we need $d>0$ and $d\mid20,30$. Thus $d\in\{1,2,5,10\}$.

The tenth terms are $4+9d$, and their sum is $4\cdot4+9(1+2+5+10)=\boxed{178}$.

## Problem 16

**Answer: 70**

The equation is equivalent to
\[
n+1=(a+1)(b+1),
\]
where the two factors are distinct and at least $2$. Thus among $2,3,\ldots,101$, we count composites admitting unequal nontrivial factors.

The only composites without such a factorization are squares of primes. (For a composite square root $u$, a proper factor of $u$ gives an unequal factorization of $u^2$.) There are $26$ primes at most $101$, and the four prime squares in the range are $4,9,25,49$. Out of $100$ candidate integers, $100-26-4=\boxed{70}$ qualify.

## Problem 17

**Answer: 441**

Put $t=\log_{2026}x$, so $x=2026^t$. Taking logarithms of the equation gives
\[
\frac{t^2}{20}=t+\log_{2026}26.
\]
This quadratic has two distinct real roots, whose sum is $20$. They correspond to two positive values of $x$, whose product is
\[
2026^{20}=2^{20}1013^{20}.
\]
Since $1013$ is prime, the number of divisors is $(20+1)^2=\boxed{441}$.

## Problem 18

**Answer: 277**

Let Patrick's speed be $v$ and his travel time be $t$ hours. The equal distances give
\[
vt=(v+2)(t-1)=(v+9)(t-2).
\]
The first equality gives $v=2t-2$, and the equality of the first and third gives $2v=9t-18$. Solving yields $t=14/5$ and $v=18/5$.

The distance is $vt=252/25$ miles, already reduced. Hence $m+n=\boxed{277}$.

## Problem 19

**Answer: 714**

Use oblique coordinates along $AB$ and $AC$, with unit distance on each axis. All shoelace areas in these coordinates are multiplied by the same factor $\sin\angle BAC$.

The relevant coordinates are
\[
A=(0,0),\ D=(14,0),\ E=(58,0),\ B=(88,0),
\quad F=(0,9),\ G=(0,153),\ C=(0,408).
\]
Reflection gives $M=(-14,18)$ and $N=(116,-153)$.

The absolute doubled shoelace area of $DEGF$ is $58\cdot153-14\cdot9=8748$. That of $AFNBCEM$, in the stated vertex order, is $25704$. Thus the requested area is
\[
243\frac{25704}{8748}=\boxed{714}.
\]
The numerical side-length data, rather than the schematic TikZ coordinates, determine this ratio.

## Problem 20

**Answer: 1280**

The angle-bisector theorem gives $BD:CD=1628:932=407:233$. Write $BD=407t$, $CD=233t$ with $t$ a positive integer. The tangent-secant theorem gives
\[
AE=1628-\frac{407t^2}{4},\qquad AF=932-\frac{233t^2}{4}.
\]
Both are integers exactly when $t$ is even. The triangle inequality is $696<640t<2560$, so only $t=2,3$ need consideration. Therefore $t=2$ is the only possibility, giving $AE=1221$, $AF=699$ and $BC=\boxed{1280}$.

## Problem 21

**Answer: 98**

Put $t=x-1$. The parabola becomes $y=t^2/2-6$, and the center is $85$ units above its vertex. Perpendicularity of the radius and tangent gives
\[
(t,t^2/2-85)\cdot(1,t)=t(t^2/2-84)=0.
\]
The vertex gives radius $85$. The other tangency points have $t^2=168$ and vertical displacement $-1$, giving radius $\sqrt{169}=13$. The sum of the two distinct radii is $\boxed{98}$.

## Problem 22

**Answer: 588**

Use unit-distance oblique coordinates along $AB$ and $AC$. Then
\[
A=(0,0),\ D=(4,0),\ E=(20,0),\ B=(28,0),
\quad F=(0,13),\ G=(0,65),\ C=(0,91).
\]
The reflected points are $M=(-4,26)$ and $N=(40,-65)$.

The absolute doubled shoelace areas of $DEGF$ and $AFNBCEM$ are respectively
\[
20\cdot65-4\cdot13=1248,\qquad2548.
\]
Their common coordinate-to-physical-area factor cancels. The requested area is $288(2548/1248)=\boxed{588}$.

## Problem 23

**Answer: 245**

Write $AB=BC=L$, $AC=c$, and $AI=CI=w$. If the altitude from $B$ is $h$, the inradius is $r=ch/(2L+c)$. Since $h^2=L^2-c^2/4$, this gives
\[
w^2=c^2/4+r^2=\frac{c^2L}{2L+c}.
\]
The integer perimeters have ratio $125:6$, so for an integer $t>0$,
\[
2L+c=125t,\qquad2w+c=6t.
\]
Let $z=c/t$. Substitution into the squared-length identity gives
\[
250(6-z)^2=4z^2(125-z),
\qquad(2z-5)(z^2-60z-900)=0.
\]
Because $0<z<6$, only $z=5/2$ is allowed; the other roots are $30\pm30\sqrt2$. Thus
\[
c=5t/2,\quad w=7t/4,\quad L=245t/4.
\]
All lengths are integers exactly when $4\mid t$. The minimum is $t=4$, giving sides $245,245,10$ and $AI=CI=7$. Hence $AB_{\min}=\boxed{245}$.

## Problem 24

**Answer: 143**

Put $K=10^{2024}$ and $R_j=1+1000+\cdots+1000^{j-1}$. Repeating a three-digit number $d$ exactly $j$ times produces $dR_j$.

Among all three-digit $d\ne n$, there are two consecutive integers, so their gcd is $1$. The stated condition therefore implies $n\mid R_K$ and $n\mid R_{K+2}$. The identity
\[
R_{K+2}=1000^2R_K+1001
\]
implies $n\mid1001$. Since $K$ is even, $1001=R_2$ divides both $R_K$ and $R_{K+2}$, so every divisor of $1001$ satisfies the repetition condition.

Now $1001=7\cdot11\cdot13$. Its only three-digit divisor is $\boxed{143}$.

## Problem 25

**Answer: 32951**

As in the floor-counting calculation, summing over $i$ gives
\[
f(n)=\sum_{j\le n}j^{1024}\lfloor n/j\rfloor,
\quad f(n)-f(n-1)=\sum_{d\mid n}d^{1024}.
\]
For $n=M^{15}$, this divisor sum is a product of six geometric sums, one for each prime dividing $M$. The factor for $2$ is odd. For every odd prime $q$, putting $u=q^{1024}\equiv1\pmod8$ gives
\[
v_2(1+u+\cdots+u^{15})=v_2(u+1)+v_2(16)-1=4.
\]
Thus $k=5\cdot4=20$, and $2^{20}\bmod5^7=\boxed{32951}$.

## Problem 26

**Answer: 81**

There are $9!$ choices for the first row. By relabeling, fix it to $1,2,\ldots,9$.

Group the digits according to their first-row blocks. A digit cannot occur in that same block in row two. The $3\times3$ matrix of counts sent from original groups to row-two blocks has zero diagonal and all row and column sums $3$. Its off-diagonal entries must alternate between $k$ and $3-k$, for $k=0,1,2,3$.

For each $k$, choosing which digits go to which allowed blocks gives $\binom3k^3$ choices. Within each row-two block the chosen digits can be ordered in $3!$ ways. Row three then has its three-digit set in each block forced, and each set again has $3!$ orders. Each digit occurs in exactly one of these row-three sets, so row three automatically has nine distinct digits.

The total is
\[
9!(3!)^6\sum_{k=0}^3\binom3k^3
=9!6^6(56)=2^{16}3^{10}5^1 7^2.
\]
The requested weighted sum is $2(16)+3(10)+5(1)+7(2)=\boxed{81}$.

## Problem 27

**Answer: 223**

The length-$10$ and length-$18$ edges must be opposite: each belongs to two faces, and no face contains both. Choose coordinates
\[
A=(5,0,0),\ B=(-5,0,0),\ C=(0,9,12),\ D=(0,-9,12).
\]
Then $AB=10$, $CD=18$, and the other four edges have length $\sqrt{25+81+144}=5\sqrt{10}$.

Symmetry puts the circumcenter at $S=(0,0,z)$. Equating its squared distances to $A$ and $C$ gives
\[
25+z^2=81+(12-z)^2,\qquad z=25/3.
\]
The incenter likewise has form $R=(0,0,t)$. Its distances to the two types of face planes are $3t/5$ and $(60-5t)/13$. Equating them gives $t=75/16$, which lies inside the tetrahedron.

Thus $RS=25/3-75/16=175/48$, already reduced, and $m+n=\boxed{223}$.

## Problem 28

**Answer: 580**

Set $g(t)=f(t-1)$. As in Problem 14, the functions are exactly
\[
g(t)=\sum_p v_p(t)w_p,\qquad w_p\in\mathbb Z_{\ge1}.
\]
The bound now applies to $2\le t\le1001$. From $3^6=729$ and $5^4=625$ we obtain
\[
1\le u=w_3\le166,\qquad1\le v=w_5\le250.
\]
Every pair is feasible by assigning all other prime weights $1$. To check this simultaneously, use the largest weights $u=166$, $v=250$. For $t=3^a5^b r\le1001$, with $r$ coprime to $15$, its value is at most $166a+250b+\lfloor\log_2(1001/(3^a5^b))\rfloor$. For $b=0,1,2,3,4$, the respective maxima over allowed $a$ are $996,915,998,917,1000$, all within the bound.

Since $2025=3^4 5^2$, we have $f(2024)=4u+2v=2(2u+v)$. For each $u$, the quantity $2u+v$ fills the interval $[2u+1,2u+250]$. These intervals overlap and together cover every integer from $3$ through $582$. Therefore the number of different values is $582-3+1=\boxed{580}$.

## Problem 29

**Answer: 32193**

For a base-$b$ digit expansion $m=\sum a_kb^k$, let $s=\sum a_k$. Then
\[
2s-m=a_0+\sum_{k\ge1}a_k(2-b^k)\le1.
\]
Indeed, $a_0\le b-1$, at least one higher digit is nonzero because $b\le m$, and its contribution is at most $2-b$; all other higher contributions are nonpositive. Thus $s\le\lceil m/2\rceil$.

This upper bound is attainable at every $m>1$: for $m=2$, use base $2$; for $m=2t$ with $t\ge2$, base $t+1$ gives digit sum $t$; for $m=2t+1$, base $t+1$ gives digit sum $t+1$.

After $j$ moves the number is at most $\lceil n/2^j\rceil$, and the bound can be attained at each move. Hence the maximum number of moves from $n$ is $\lceil\log_2 n\rceil$. Over the stated range,
\[
M=\left\lceil100000\log_2 10\right\rceil=332193.
\]
This integer was also checked exactly by computing the bit length of $10^{100000}$. The required remainder is $\boxed{32193}$.

## Problem 30

**Answer: 751**

Put $B=(0,0)$, $C=(108,0)$ and $A=(u,v)$. The angle-bisector theorem gives
\[
AX:XC=39:108=13:36,\qquad XC=648/7.
\]
Write the circumcircle of $ABX$ as $x^2+y^2+\alpha x+\beta y=0$, since it passes through $B$. Its power at $C$ is both
\[
108^2+108\alpha\quad\text{and}\quad CA\cdot CX=126(648/7)=108^2.
\]
Thus $\alpha=0$.

The points $X,Y$ also lie on the circle centered at $C$ with radius $CX$. Their common chord line is the radical axis. If it meets the $x$-axis at $E=(e,0)$, equality of powers there gives
\[
e^2=(e-108)^2-(648/7)^2.
\]
So $BE=e=(108^2-(648/7)^2)/216=702/49$. This fraction is reduced, and $m+n=\boxed{751}$.

## Problem 31

**Answer: 16**

Every term contributes either its positive value or its negative value to the left-to-right result. If the sums of added and subtracted terms are $P,Q$, then
\[
P+Q=12,\qquad P-Q=-8,
\]
so $P=2$ and $Q=10$.

Every odd term is added. Having only one added term of value $2$ cannot work: the first running total would be even, and a subtraction could never start. Thus the added terms must be exactly two $1$s. The first term is $1$, the last term is $1$, and all intervening terms are positive even numbers totaling $10$. Conversely, every such sequence works: the running total stays odd between the two $1$s, so each intervening term is subtracted.

Dividing the intervening terms by $2$ identifies them with compositions of $5$. There are $2^{5-1}=\boxed{16}$.

## Problem 32

**Answer: 145040**

Summing the floor over $i$ gives
\[
f(n)=\sum_{j\le n}j^{445}\lfloor n/j\rfloor,
\qquad f(n)-f(n-1)=\sum_{d\mid n}d^{445}.
\]
For $n=M^{143}$, the factor for $2$ in this divisor sum is odd. For an odd prime $q$, set $u=q^{445}$. The geometric factor has $144$ terms, so
\[
v_2(1+u+\cdots+u^{143})=v_2(u+1)+v_2(144)-1=v_2(q+1)+3.
\]
Here the last equality uses the odd exponent $445$. For $q=3,5,7,11,13$, the values $v_2(q+1)$ are $2,1,3,2,1$. Hence $k=9+5(3)=24$.

The required remainder is $2^{24}\bmod22^4=\boxed{145040}$.

## Problem 33

**Answer: 821**

There are $11!!=10395$ equally likely pairings. The final word is the pair whose smaller letter is largest.

If $G$ is paired with one of $H,I,J,K,L$, there are five choices for its partner. For this to be the last word, the remaining four letters above $G$ must each pair with one of $A,\ldots,F$. There are $6\cdot5\cdot4\cdot3=360$ such assignments; the remaining two lower letters pair together. This gives $1800$ pairings.

If $G$ is the larger letter in the final word, its partner must be $F$. Pairing it with $E$ or an earlier letter would leave more higher letters than available lower partners. With pair $FG$, the five letters $H,\ldots,L$ must be matched bijectively with $A,\ldots,E$, giving $5!=120$ pairings.

The probability is $(1800+120)/10395=128/693$. Thus $m+n=\boxed{821}$.

## Problem 34

**Answer: 81**

The example differs from Problem 26, but the constraints are identical, so the answer is unchanged. For completeness, fix the first row after choosing its $9!$ possible permutations. The ways to distribute each original block's digits between the other two blocks in row two total
\[
\sum_{k=0}^3\binom3k^3=56.
\]
The digits can be ordered in each of row two's three blocks in $(3!)^3$ ways. Row three's block sets are then forced, with another $(3!)^3$ orders. Therefore the number of grids is
\[
9!6^6\cdot56=2^{16}3^{10}5^1 7^2,
\]
and the requested sum is $2(16)+3(10)+5+7(2)=\boxed{81}$.

## Problem 35

**Answer: 2193**

The digit-sum argument in Problem 29 gives the exact maximum $\lceil m/2\rceil$ after one move from $m$, attained by choosing a base near $m/2$. Iterating this attainable upper bound shows that the maximum number of moves from $n$ is $\lceil\log_2 n\rceil$.

Thus for $n\le10^{100000}$,
\[
M=\left\lceil100000\log_2 10\right\rceil=332193.
\]
The only change from Problem 29 is the modulus. Here $332193\bmod10000=\boxed{2193}$.

## Problem 36

**Answer: 42**

Write $a=BC$, $b=CA$, $c=AB$, with $b>c$. The points $B,D,E$ all lie on the circle centered at $A$ with radius $c$.

Suppose the second common point $Y$ lies on line $AD$. The power of $A$ with respect to circle $CED$ gives the directed relation
\[
AC\cdot AE=AD\cdot AY,\qquad bc=c\,AY,
\]
so $Y$ is on the ray $AD$ with $AY=b$. Applying power of $A$ to circle $BXD$ then gives $AB\cdot AX=AD\cdot AY$, hence $AX=b$ on the ray $AB$. Conversely, if $AX=b$, both circles meet line $AD$ again at the point with $AY=b$, so this condition is sufficient as well.

Take $A$ as the vector origin. Then $C=(b/c)E$ and $X=(b/c)B$. Intersecting $BC$ with $EX$ gives
\[
D=\frac{b}{b+c}(B+E).
\]
Since $|B|=|E|=|D|=c$, writing $\theta=\angle BAC$ yields
\[
2(1+\cos\theta)=\frac{(b+c)^2}{b^2}.
\]
Substituting into the cosine rule for $a$ gives
\[
a^2=(b+c)^2\frac{b-c}{b}.
\]
Therefore $a/(b+c)=p/q$ for relatively prime positive integers $p<q$, and
\[
\frac cb=\frac{q^2-p^2}{q^2}.
\]
Integer $b,c$ imply $b=dq^2$, $c=d(q^2-p^2)$ for a positive integer $d$. Then
\[
a=\frac{dp(2q^2-p^2)}q.
\]
Because the numerator factor $p(2q^2-p^2)$ is coprime to $q$, integrality requires $q\mid d$. Thus all candidates have
\[
(a,b,c)=k\bigl(p(2q^2-p^2),\ q^3,\ q(q^2-p^2)\bigr)
\]
for a positive integer $k$.

The smallest denominator is $q=2$, forcing $p=1$, and $k=1$ gives $(a,b,c)=(7,8,6)$ with perimeter $21$. This triangle is acute since $8^2<7^2+6^2$, and the required $D$ lies strictly inside $BC$: its fraction of the way from $B$ to $C$ is $c/(b+c)$. The construction above supplies $X$ and $Y$, so it satisfies every condition. For $q\ge3$, already $b=kq^3\ge27$, exceeding this entire perimeter; for $q=2$, any larger scale increases the perimeter. The minimum is therefore unique.

Finally $abc=7\cdot8\cdot6=336\equiv\boxed{42}\pmod{49}$.
