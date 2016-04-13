## Summary
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 488f8e65fffd12bb67fe53dc9c7b2697103e8c65
Prosper Marketplace is America's first peer-to-peer lending marketplace, with more than 2.2 million members and over $5 billion in funded loans. 
Borrowers request personal loans on Prosper and investors (individual or institutional) can fund anywhere from $2,000 to $35,000 per loan request. 
In addition to credit scores, ratings, and histories, investors can consider borrowers’ personal loan descriptions, endorsements from friends, and community affiliations. 
Prosper handles the servicing of the loan and collects and distributes borrower payments and interest back to the loan investors (Wikipedia). Prosper also make available its loans' data to the public for research. 
Using Prosper data, I categorize each Prosper loan on the basis of its rating. Then I visualize the risk and return trade off of each rating category and comapre them with some of the most popular mutual funds in the market. 

## Design
First, loans are grouped base on their rating. There are total of 6 ratings, from safest to riskiest: AA, A, B, C, D, E, HR. 
<<<<<<< HEAD

Estimated loss of all loans in a specific rating group are averaged and used for risk metric. 
Estimated loss is the estimated principal loss on charge-offs. 

Return is calculated as the average of estimated effective yield of all the loans in each specific rating group. 
Effective yield is equal to the borrower interest rate minus the servicing fee rate, minus estimated uncollected interest on charge-offs, plus estimated collected late fees. 

Both risk and return are expressed as a percentage of initial investment. 

For mutual funds, standard deviation is used to measure risk. Standard deviation is the average change in return over a specified time frame, expressed as a percentage of initial investment.
For example, a portfolio with annualized (average yearly) return of 5% and standard deviation of 10% over a 3-year period would mean that the annual return of the portfolio can go as high as 15% or as low as -5%, over that 3 year.
In our chart, average total return is used instead of annual return. For example, for 3-year period, return is calculated as the return the investor would receive today if he/she had put the money in the portfolio in the previous 3 years.
Then ten samples of 3-year period is used to calculate the average of total return for 3-year periods. The same method is applied for standard deviation. For each term category (3-year, 5-year), 10 samples are drawn, and average standard deviation is
calculated for each sample.

Therefore, a portfolio with total return of 5% and standard deviation of 10% over 3-year period would mean that if the investor would have had the money in this porfolio for 3 years, then after this period of time,
the investor can earn as much as 10%, or as low as -5%, on average. In quantitative finance, standard deviation is one of the most widely used metric to quantify risk.

The reason standard deviation is used to quantify risk for other portfolios in this chart is because standard deviation in this context behaves like default probability of a loan. When an investor put money in a portfolio with
total return of 5% and standard deviation of 10% over 3-year, after this period, if investors experience a loss, then this loss on average will be -5%. On the other hand, if investor invests in a Prosper loan with 
estimated effective yield of 5% and estimated loss of 10% over the same period, then after 3 year, if the loan defauls, his return will be -5%, on average (estimated return is the difference between estimated total yield
and estimated loss). Because Prosper loans return and risk are all estimated, avrages of return and standard deviation (over samples of 10) of other portfolios are used as an estimate for future risk and return.
  
Since standard deviation is calculated based on annualized return, it only makes sense to use standard deviation to measure portfolio risk over periods of more than one year.
Prosper loan is different. Loans are simple financial products, with their risk is the probability that the borrower will default on the loan. Thus, loans' risk calculation is based on the data
of other similar loans in the past, not on the loan itself. The loan's term is not part of the formula for this calculation, as in other portfolio's standard deviation.
This explains why for 1-year period, risk data is only available for Prosper loans, not for other portfolios.

The Sharpe Ratio is a measure for calculating risk-adjusted return, and this ratio has become the industry standard for such calculations. It was developed by Nobel laureate William F. Sharpe. In simple term, Sharpe ratio
measures how much investors are rewarded for each unit of risk taken. In this chart, Sharpe ratio calculation is simplified, which assumes risk free rate is 0. Higher Sharpe ratio is better, because investors are rewarded more for same level of risk. The color hue is used to represent the value of Sharpe ratio.
The darker the color hue, the higher the Sharpe ratio of the portfolio.

Initially, I have two charts on my page, one displaying the risk/return trade off; the other one shows how many loans of each term are in each specific rating category. 
The first chart is a scatter plot, while the second chart is a combination of scatter plot and pie charts. Scatter plot is used because we want to project each loan on two dimensions (risk and return); 
therefore, the easiest way to do this is using scatter plot with x and y axis.
In the second chart, scatter plot shows the risk/return of each type of Prosper loan, 
while the pie chart shows how many of each types are 12, 36, and 60 months term. Scatter plots can only be used to express two features, thus I think I can express another feature using another chart on top
of scater plot, and pie chart seems to be a good one. However, after collecting feedback, I realized that the second chart is redundant, 
and decided to update only one the first chart. Thus, the new chart not only displays scatter plots, 
=======

Estimated loss of all loans in a specific rating group are averaged and used for risk metric. 
Estimated loss is the estimated principal loss on charge-offs. 

Return is calculated as the average of estimated effective yield of all the loans in each specific rating group. 
Effective yield is equal to the borrower interest rate minus the servicing fee rate, minus estimated uncollected interest on charge-offs, plus estimated collected late fees. 

Both risk and return are expressed as a percentage of initial investment. 

For mutual funds, standard deviation is used to measure risk. Standard deviation is the average change in return over a specified time frame, expressed as a percentage of initial investment.
For example, a portfolio with annualized (average yearly) return of 5% and standard deviation of 10% over a 3-year period would mean that the annual return of the portfolio can go as high as 15% or as low as -5%, over that 3 year.
In our chart, average total return is used instead of annual return. For example, for 3-year period, return is calculated as the return the investor would receive today if he/she had put the money in the portfolio in the previous 3 years.
Then ten samples of 3-year period is used to calculate the average of total return for 3-year periods. The same method is applied for standard deviation. For each term category (3-year, 5-year), 10 samples are drawn, and average standard deviation is
calculated for each sample.

Therefore, a portfolio with total return of 5% and standard deviation of 10% over 3-year period would mean that if the investor would have had the money in this porfolio for 3 years, then after this period of time,
the investor can earn as much as 10%, or as low as -5%, on average. In quantitative finance, standard deviation is one of the most widely used metric to quantify risk.

The reason standard deviation is used to quantify risk for other portfolios in this chart is because standard deviation in this context behaves like default probability of a loan. When an investor put money in a portfolio with
total return of 5% and standard deviation of 10% over 3-year, after this period, if investors experience a loss, then this loss on average will be -5%. On the other hand, if investor invests in a Prosper loan with 
estimated effective yield of 5% and estimated loss of 10% over the same period, then after 3 year, if the loan defauls, his return will be -5%, on average (estimated return is the difference between estimated total yield
and estimated loss). Because Prosper loans return and risk are all estimated, avrages of return and standard deviation (over samples of 10) of other portfolios are used as an estimate for future risk and return.
  
Since standard deviation is calculated based on annualized return, it only makes sense to use standard deviation to measure portfolio risk over periods of more than one year.
Prosper loan is different. Loans are simple financial products, with their risk is the probability that the borrower will default on the loan. Thus, loans' risk calculation is based on the data
of other similar loans in the past, not on the loan itself. The loan's term is not part of the formula for this calculation, as in other portfolio's standard deviation.
This explains why for 1-year period, risk data is only available for Prosper loans, not for other portfolios.

The Sharpe Ratio is a measure for calculating risk-adjusted return, and this ratio has become the industry standard for such calculations. It was developed by Nobel laureate William F. Sharpe. In simple term, Sharpe ratio
measures how much investors are rewarded for each unit of risk taken. In this chart, Sharpe ratio calculation is simplified, which assumes risk free rate is 0. Higher Sharpe ratio is better, because investors are rewarded more for same level of risk. The color hue is used to represent the value of Sharpe ratio. The darker the color hue, the higher the Sharpe ratio of the portfolio.

Initially, I have two charts on my page, one displaying the risk/return trade off; the other one shows how many loans of each term are in each specific rating category. 

The first chart is a scatter plot, while the second chart is a combination of scatter plot and pie charts. Scatter plot is used because we want to project each loan on two dimensions (risk and return); therefore, the easiest way to do this is using scatter plot with x and y axis.

In the second chart, scatter plot shows the risk/return of each type of Prosper loan, while the pie chart shows how many of each types are 12, 36, and 60 months term. Scatter plots can only be used to express two features, thus I think I can express another feature using another chart on top of scater plot, and pie chart seems to be a good one. However, after collecting feedback, I realized that the second chart is redundant, and decided to update only the first chart. Thus, the new chart not only displays scatter plots, 
>>>>>>> 488f8e65fffd12bb67fe53dc9c7b2697103e8c65
but also tool tips to show the details of each portfolio, separate colors to distiguish between Prosper loans and other portfolios, 
and color hue to show the magniutde of Sharpe ratio. Color hue is used because it can be used on top of scatter plot to express more information without making the chart confusing or messy.

## Feedback

###yan_24332845395244373d: 

What do you notice in the visualization?
I see return/risk ratings for various Prosper loans, as well as for several conventional investment choices.

What questions do you have about the data?
Not clear what units for the return and risk ratings.

What relationships do you notice?
Return and risk seem positively correlate: higher return is associated with higher risk.

What do you think is the main takeaway from this visualization?
Some Prosper investments are better than those listed conventional investment, because the Prospers carry same risks but offer better return.

Is there something you don’t understand in the graphic?
Choice of colors for various Prospers don't seem so clear to me. Are they diverging colors?


###yavigol3d:

What do you notice in the visualization?
* (Chart1): Risk for the funds is usually higher than for prosper loans for the same return level
* (Chart2): Term structure of loans by Prosper rating
* (Chart2): For all Prosper ratings, 3-year term loans have largest share with 5- and 1-year loans being second and third by the share

What questions do you have about the data?

(Chart1): It is not clear why there is no information on funds when 1-year option selected
(Chart1, 2): What time the data relates to?
What relationships do you notice?

(Chart1): Higher risk Prosper loans generate higher returns
(Chart2): For all Prosper ratings, 3-year term loans have largest share with 5- and 1-year loans being second and third by the share
What do you think is the main takeaway from this visualization?

Prosper loans are relatively less risky than funds
Higher risk loans typically generate higher returns
Is there something you don’t understand in the graphic?
Everything is quite clear

Some suggestions
Chart1

I would put a header to this chart
It is also possible to create tooltips showing risk and return values for each circle
Finance theory says that return depends on risk. Therefore it can be better to plot return along y axis and risk - along x axis
When 3 year loans are selected, MSIQX circle is located to the left from y axis and, therefore, covers the axis value. It can be a good idea to move y axis to the left so the circle gets to the right side from the axis
You can also segregate Prosper related circles from other funds visually (e.g. same fill or line color)
You can indicate somewhere what time period the data relates to
Label values can be converted from decimal to % format
Chart2

Information on return vs. risk is reflected on the first chart already. It can be better to focus on the term structure part of the data here and to use some other chart type (e.g. bar charts) to show the structure
I would put a header to this chart
I would show color coding in a legend box separately and would leave only numerical values in tooltips


###chris_286663:

Hi Long,

I want to give you some overall feedback since the last two reviews focused specifically on the questions asked. I think this might help in making the visualization easier for the casual reader (rather than the informed reader) since I'm not familiar with the prosper loan data set.

First, I think it might help to add an additional sentence on what a prosper loan is. I could guess from the chart but I'm not exactly sure.

Initially, it isn't apparent that there are buttons on the left until I do some exploring. Maybe add some kind of styling so that it is more clear that they are buttons to facet the chart.

I think it also might help to add a legend on the right of the first chart as well. It seems to me that you are comparing prosper loans to some mutual funds. Maybe color each prosper loan individually and have one color for all other mutual funds even though there are several in the chart. Hovering over each mutual fund will give detailed info if the viewer wants more. This would give more emphasis to those prosper loans.

There is one mutual fund that has a negative return in the first chart that goes off the x-axis. Maybe extend the x-axis to include a negative range so that it doesn't go off the chart.

On the second chart I was at first unsure of what is being communicated after reading. Because position (X, Y) is one of the primary ways people perceive information, my initial thought is that we are looking at the correlation between risk and return. It seems from the description that we might be focusing more on the number of loans in each category? If so the second chart seems a little redundant to the first. Maybe change the visual representation to emphasize that you want to focus on the number of loans in each category across term duration.

I hope this helps! Great job on your first iteration!

## Resources
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.eventArgs
https://github.com/mbostock/d3/wiki/Transitions
http://stackoverflow.com/questions/24989128/why-is-my-d3-tip-not-working
<<<<<<< HEAD
https://www.udacity.com/course/viewer#!/c-ud507-nd/l-3069149263/m-3071138983
=======
https://www.udacity.com/course/viewer#!/c-ud507-nd/l-3069149263/m-3071138983
<<<<<<< HEAD
>>>>>>> e0c7f49015ac1f6ec3ced1114b70263f21166f02
=======
https://www.udacity.com/course/viewer#!/c-ud507-nd/l-3069149263/m-3071138983
>>>>>>> 488f8e65fffd12bb67fe53dc9c7b2697103e8c65
