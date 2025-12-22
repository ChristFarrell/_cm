# NOTES

All of this project 

## [GrowthDensity]()

On first program, this program will find the growth and density from Indonesia. In general, this program will collect population per province and provincial area data. For the growth, we calculate using the rule:<br>

$$
Growth = \frac{P_{after} - P_{before}}{P_{before}} \times 100
$$

Notes:
- $P_{before}$  : The mean of last year.
- $P_{after}$   : The mean of that year.

For the density, we calculate using the rule:<br>
$$Density = \frac{Population}{Area}$$

As the result shown, there also showing the graph of growth and density.
1. For the growth, for year 2020-2022 Kepualuan Riau is the highest province of growth, however in 2023 Maluku take place as the highest province of growth. For the lowest province of growth, sequentially from 2020-2021, 2021-2022, 2022-2023 are Jakarta, (Jakarta and Jawa Timur), and the last is Kepualaun Riau.

2. For the density, the result more stable from 2020-2023. Province with the most densely populated is Jakarta. Province with the lowest densely populated is Kalimantan Utara.

In conclution, this indicates that population growth rates do not always correlate directly with regional density. Such as the Kepulauan Riau and Maluku experienced high growth, but both was not becoming the most densely populated regions. Conversely, Jakarta remains the most densely populated region despite relatively low population growth, indicating limited space and high urbanization pressures.

## [Correlation]()

On second program, this program identifies correlations to classify worker income based on different age groups. The list group including 15-24 years old worker, 25-54 years old worker, and 55+ years old worker. For the correlation, we calculate using the rule:<br>
$$Cr = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

Notes:
- $x_i$     : Number of Variable 1.
- $\bar{x}$ : The mean of Variable 1 across all provinces.
- $y_i$     : Number of Variable 2.
- $\bar{y}$ : The mean of Variable 2 across all provinces.

From the result output, there are 4 conclusion from 2020-2023
1. Correlation on Year 2020
    - Strong correlation between ages 25–54 and 55+.
    - Ages 15–24 are positively correlated with other groups.
    - Population structure is relatively consistent across provinces.

2. Correlation on Year 2021
    - A strong correlation remains, but it is weakening.
    - The income gap between young and old is declining.
    - The demographic impact of the pandemic is evident.

3. Correlation on Year 2022
    - Strong correlation for every group ages (15-55+).
    - Population structure is start to stabilizing again in this year.
    - The lifting of pandemic policies has shown a positive impact on all ages.

4. Correlation on Year 2023
    - Correlation remains high, but there is a weakening across age groups.
    - Productive age is the center of population structure.
    - One of the causes because economic growth that decreased (5.31% to 5.05%).

## [InferentialStatistics]()
